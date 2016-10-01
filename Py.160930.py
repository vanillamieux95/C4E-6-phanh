import urllib.request
with urllib.request.urlopen('http://dantri.com.vn/') as response:
   html = response.read()
print (html)
