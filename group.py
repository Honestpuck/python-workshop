#!/usr/bin/env python3

import requests
import xml.etree.ElementTree as ET

user = ''
pwd = ''
auth = (user, pwd)
url = ''

grp = requests.get(url, auth=auth)

grp.text
root = ET.fromstring(grp.text)

root.findtext('name')
root.findall('name')
root.findall('name')[0].text
root.findall('computers/computer')

for computer in root.findall('computers/computer'):
	print(computer.findtext('name'))
