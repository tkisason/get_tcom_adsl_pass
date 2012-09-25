#!/usr/bin/python

import requests
import re
import sys
import getpass


def return_ip(data):
    return re.findall('(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})',data)[-1]

def get_tcom_adsl_ip(user,passwd):
    credentials = {'username':user,'passwd':passwd}
    url = 'https://user.t-com.hr/index.php'
    r = requests.post(url,credentials)
    data = r.content
    return str(return_ip(data))


if (__name__=="__main__"):
    passwd = getpass.getpass("Enter ADSL Password: ")
    sys.stdout.write( get_tcom_adsl_ip(sys.argv[1],passwd))


