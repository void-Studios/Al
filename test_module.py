import test

# Test the function
url = "http://192.168.196.42:11434"
test.check_url(url)
api = test.get_API()
print(f"API = {api}")