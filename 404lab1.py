import requests

print(requests.__version__)

#google = requests.get("http://www.google.com")
#print(google)

var = requests.get("https://raw.githubusercontent.com/XiaoleZ/404W20-ualberta/master/404lab1.py")
print(var.content)
