#!/usr/bin/env python3

import subprocess
import os
import xml.etree.ElementTree as ET
import requests

# cheat block
url = 'https://twxworld.jamfcloud.com/dbfileupload'
path = '/Users/Shared/AUTOPKG/AdobeCreativeCloudInstaller-4.8.1.435.pkg'
user = 'xworld'
pwd = 'passwd'

# get the name of the package
fname = os.path.basename(path)

headers = {
	'DESTINATION': '0',
	'OBJECT_ID': '-1',
	'FILE_TYPE': '0',
	'FILE_NAME': fname,
}

files = {'file': open(path, 'rb')}

r = requests.post(url, auth=(user, pwd), headers=headers, files=files)
packid = ET.fromstring(r.text).findtext('id')

## curl subprocess way

# Curl expects auth information as a ':' delimited string.
auth = '{}:{}'.format(user, pwd)

command =  ["curl", "-u", auth, '-s']
command += ['-X', 'POST', 'https://suncorp.jamfcloud.com/dbfileupload']
command += ['--header', 'DESTINATION: 0']
command += ['--header', 'OBJECT_ID: -1' ]
command += ['--header', 'FILE_TYPE: 0'  ]
command += ['--header', 'FILE_NAME: {}'.format(fname) ]
command += ['--upload-file', path ]

output = subprocess.check_output(command)

packid = ET.fromstring(output).findtext('id')


