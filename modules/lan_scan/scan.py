#!/usr/bin/env python3
import re
import requests
import os
from scapy.all import ARP, Ether, srp
import mysql.connector
from datetime import datetime
import socket
from geopy.geocoders import Nominatim
import configparser

def load_config():
    print('Loading config...')
    config = configparser.ConfigParser()
    config_path=os.path.expanduser('~/program_data/database.config')
    config.read(config_path)
    return config['mysql']

def scan_devices(ip):
    print('Scanning network for avialable devices...')
    arp_request = ARP(pdst=ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp_request
    result = srp(packet, timeout=3, verbose=0)[0]

    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    return devices

def get_vendor(mac_address):
    print('Getting vendor information...')
    if not mac_address or not re.match(r"([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})", mac_address):
        return None
    oui = mac_address[:8].replace(":", "").upper()

    # Query a MAC OUI database to get the vendor information
    # You can replace the URL with a different MAC OUI database if needed
    oui_url = f"https://macvendors.com/api/{oui}/companyname"
    try:
        response = requests.get(oui_url)
        if response.status_code == 200:
            return response.json()['result']['company']
    except Exception as e:
        print(f"Error getting vendor information: {e}")

    return None

def get_hostname(ip_address):
    print('Getting hostname...')
    try:
        hostname, _, _ = socket.gethostbyaddr(ip_address)
        return hostname
    except socket.herror:
        return None

def port_scan(ip_address):
    print('Scanning ports...')
    from scapy.all import sr, IP, TCP
    open_ports = []
    for port in range(1, 1025):  # Scan common ports
        packet = IP(dst=ip_address) / TCP(dport=port, flags="S")
        response = sr(packet, timeout=1, verbose=0)[0]
        if response and response[0][1].haslayer(TCP) and response[0][1][TCP].flags == 18:  # Check for TCP SYN-ACK
            open_ports.append(port)
    return open_ports

def get_geolocation(ip_address):
    print('Getting geolocation information...')
    geolocator = Nominatim(user_agent="your_app_name")
    location = geolocator.geocode(ip_address)
    if location:
        return location.address
    else:
        return None

def update_database(devices, config):
    print('Submitting update to the database...')
    connection = mysql.connector.connect(
        host=config['host'],
        user=config['user'],
        password=config['password'],
        database=config['database']
    )
    cursor = connection.cursor()

    for device in devices:
        # Retrieve additional information
        vendor = get_vendor(device['mac'])
        hostname = get_hostname(device['ip'])
        open_ports = port_scan(device['ip'])
        geolocation = get_geolocation(device['ip'])

        # Insert device information into the MySQL table
        query = (
            "INSERT INTO lan_devices (ip, mac, timestamp, vendor, hostname, open_ports, geolocation) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)"
        )
        values = (
            device['ip'],
            device['mac'],
            datetime.now(),
            vendor,
            hostname,
            str(open_ports),
            geolocation
        )
        cursor.execute(query, values)

    connection.commit()
    connection.close()

# Example usage
network_ip = "192.168.1.1/24"
config = load_config()
devices = scan_devices(network_ip)
update_database(devices, config)
