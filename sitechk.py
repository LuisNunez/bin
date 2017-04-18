# script to test website status
# looking for status 200
from sys import argv
import requests
import socket
import sys
# Supress warning messages from certificate check 
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

__author__ = "Luis Nunez"
__license__ = "GPLv3"
__version__ = "0.1.1"
__maintainer__ = "Luis Nunez"
__status__ = "Prototype"


print 'Version:', __version__


# Colors
Red = '\033[91m'
CEnd = '\033[0m'
Blink = '\33[5m'
BlinkEnd = '\33[6m'


def main(File):
    UrlFile = open(File)
    for Url in UrlFile:
        x = Url.strip()
        try:
            Status = requests.get(x,verify=False)
            fqdn = socket.getfqdn(x.replace('https://', ''))
            aka = socket.gethostbyname_ex(x.replace('https://', ''))
            code = Status.status_code
            code_str = str(code)
            if code_str != '200':
                prn_code_str = Blink + Red + code_str + BlinkEnd + CEnd
                print prn_code_str, x, fqdn, aka[2]
            else:
                prn_code_str = code_str
                print prn_code_str, x, fqdn, aka[2]
        except Exception, Error:
            print Red + "Exception" + CEnd, x
            sys.stderr.write('ERROR: %s\n' % str(Error))

if __name__ == '__main__':
    main(argv[1])
