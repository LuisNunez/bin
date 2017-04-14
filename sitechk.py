# script to test website status
# looking for status 200

import requests
import socket


version = '0.1.1'

print 'Version:', version


UrlFile = open('file.txt')

# Colors
Red = '\033[91m'
CEnd = '\033[0m'

for Url in UrlFile:
    #print Url
    #lenght = len(Url)
    # Remove ending character
    x = Url.strip()
    #print x
    try:
        Status = requests.get(x)
        fqdn = socket.getfqdn(x.replace('https://',''))
        aka = socket.gethostbyname_ex(x.replace('https://',''))
        code = Status.status_code
        code_str = str(code)
        if code_str != '200':
            prn_code_str= '\33[5m'+Red + code_str + '\33[6m'+CEnd
            print prn_code_str, x, fqdn, aka[2]
        else:
            prn_code_str = code_str
            print prn_code_str, x, fqdn, aka[2]
    except:
        print Red + "Exception" + CEnd ,x



