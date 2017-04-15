# script to test website status
# looking for status 200
__author__ = "Luis Nunez"
__license__ = "GPLv3"
__version__ = "0.1.1"
__maintainer__ = "Luis Nunez"
__status__ = "Prototype"


from sys import argv
import requests
import socket



print 'Version:', __version__


# Colors
Red = '\033[91m'
CEnd = '\033[0m'
Blink = '\33[5m'
BlinkEnd = '\33[6m'

def main(File):
    UrlFile = open(File)
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
                #prn_code_str= '\33[5m'+Red + code_str + '\33[6m'+CEnd
                prn_code_str= Blink +Red + code_str + BlinkEnd + CEnd
                print prn_code_str, x, fqdn, aka[2]
            else:
                prn_code_str = code_str
                print prn_code_str, x, fqdn, aka[2]
        except:
            print Red + "Exception" + CEnd ,x

if __name__ == '__main__':
    main(argv[1])

