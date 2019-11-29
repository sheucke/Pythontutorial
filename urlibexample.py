from urllib.request import urlopen
import urllib.error

try:
    response = urlopen("https://codeloop.org/page")

    print(response)
    print(response.readline())
    print(response.read(200))
    print(response.status)

except urllib.error.HTTPError as e:
    print("Status: ", e.code)
    print("Reason: ", e.reason)
    print("Url: ", e.url)
