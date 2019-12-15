import socket
from urllib.request import urlopen, URLError, HTTPError

socket.setdefaulttimeout( 23 )  # timeout in seconds

url = 'http://localhost:3000/monitoring/ping/'
try :
    response = urlopen( url )
except HTTPError as e:
    print ('The server couldn\'t fulfill the request. Reason:', str(e.code))
except URLError as e:
    print ('We failed to reach a server. Reason:', str(e.reason))
else :
    html = response.read()
    print ('got response!')
    # do something, turn the light on/off or whatever