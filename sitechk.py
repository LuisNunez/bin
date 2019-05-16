# Sitechk.py is a script to test website status.  It uses the Requests module to form http requests.  
# The script reads a CSV file with the following headers as input for the http requests.
# Origin, host, staging.
# This script was developed to test and validate sites hosted on the Akamai staging and production.
 
# looking for status 200
# from sys import argv
import logging
logging.basicConfig(filename='sitechk.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

import requests
import socket
import sys
import csv
import argparse
# Supress warning messages from certificate check 
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

__author__ = "Luis Nunez"
__license__ = "GPLv3"
__version__ = "0.2.1"
__maintainer__ = "Luis Nunez"
__status__ = "Prototype"
__date_ = '04/19/2017'


# Colors
Red = '\033[91m'
CEnd = '\033[0m'
Blink = '\33[5m'
BlinkEnd = '\33[6m'


def main(File,Flag):
    print "Test Production"
    UrlFile = csv.DictReader(open(File,'rb'))
    for Url in UrlFile:
        x = Url['proto'] + Url[Flag].strip() + Url['path'].strip()
        try:
            Status = requests.get(x,verify=False)
            code = Status.status_code
            code_str = str(code)
            #fqdn = socket.getfqdn(Url['host'].replace('https://', ''))
            #aka = socket.gethostbyname_ex(x.replace('https://', ''))
            fqdn = socket.getfqdn(Url[Flag])
            aka = socket.gethostbyname_ex(Url[Flag])
            if code_str != '200':
                prn_code_str = Blink + Red + code_str + BlinkEnd + CEnd
                print prn_code_str, x, fqdn, aka[2]
            else:
                prn_code_str = code_str
                print prn_code_str, x, fqdn, aka[2]
        except Exception, Error:
            print Red + "Exception" + CEnd, x
            sys.stderr.write('ERROR: %s\n' % str(Error))

def SiteCheck(File,Flag):
    print "-----------------------------------------------------------"
    print "Testing: ", Flag
    UrlFile = csv.DictReader(open(File,'rb'))
    for Url in UrlFile:
        print "-----------------------------------------------------------"
        target = Url['proto'] + Url[Flag].strip() + Url['path'].strip()
        #headers = {'Host':Url['host']}
        headers = {'Host':Url['host'], 'user-agent':'MetLife-tvm','Accept-Encoding':'gzip'}
        print(Url['host'])
        try:
            Status = requests.get(target,headers= headers, verify=False)
            code = Status.status_code
            code_str = str(code)
            #fqdn = socket.getfqdn(Url['host'].replace('https://', ''))
            #aka = socket.gethostbyname_ex(x.replace('https://', ''))
            fqdn = socket.getfqdn(Url[Flag])
            aka = socket.gethostbyname_ex(Url[Flag])
            if code_str != '200':
                prn_code_str = Blink + Red + code_str + BlinkEnd + CEnd
                print prn_code_str, target, fqdn, aka[2]
            else:
                prn_code_str = code_str
                print prn_code_str, target, fqdn, aka[2]
        except Exception, Error:
            print Red + "Exception" + CEnd, target
            sys.stderr.write('ERROR: %s\n' % str(Error))
            #logging.info('EXCEPTION:%s' % str(Error))
            logging.info('EXCEPTION:%s %s %s', Flag, Url['host'], str(Error))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "Python HTTP check script")
    parser.add_argument('filename')
    parser.add_argument("-r", "--region", dest = 'region', action='store', default= 'All', help='Default is all')
    args = parser.parse_args()

    print 'Version:', __version__
    print 'Site Checking Script'
    logging.info('Script Site Checking Script version:%s', __version__ )
    main(args.filename,'host')
    SiteCheck(args.filename,'origin')
    #SiteCheck(args.filename,'staging_ip')
    SiteCheck(args.filename,'host')
    SiteCheck(args.filename,'staging')
    
