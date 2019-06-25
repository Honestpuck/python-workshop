#!/usr/bin/env python3

import requests
import xml.etree.ElementTree as ET

user = 'api_test'
pwd = 'complex'
auth = (user, pwd)
url = 'https://example.jamfcloud.com/JSSResource/computergroups/id/8'

grp = requests.get(url, auth=auth)

grp.text
root = ET.fromstring(grp.text)

root.findtext('name')
root.findall('name')
root.findall('name')[0].text
root.findall('computers/computer')

for computer in root.findall('computers/computer'):
	print(computer.findtext('name'))
