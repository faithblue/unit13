import requests
import urllib

f = open("file.txt", "r")

for x in f:
  x = x.strip('\n')
  response = requests.get(x)
  print(response.headers)
  server = response.headers.get("Server")
  #print(server)
  newFile = open("url.txt", "a")
  newFile.write('URL: ' + x + ', Server: ' + server + '\n')
  newFile.close()

#response = requests.get("https://www.mccd.edu")
#server = response.headers.get("Server")
#print(response.headers)
#print(server)

f.close()