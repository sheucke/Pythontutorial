import requests

response = requests.get('https://google.com/')

print(response.status_code)
print(response.reason)
print(response.url)
print(response.ok)
print(response.is_redirect)
print(response.request.headers)
print(response.headers['content-encoding'])
print(response.content)
print(response.text)

s = requests.Session()
s.get("https://google.com")

response = s.get("https://google.com/preferences")

print(response)
