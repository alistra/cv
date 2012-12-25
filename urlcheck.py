#!/usr/bin/env python3
import fileinput, re, sys
import urllib.request, urllib.error, urllib.parse

urls = []

for line in fileinput.input():
    urls += re.findall('\\href\{(http.*?)\}', line)

for url in urls:
    try:
        connection = urllib.request.urlopen(url)
        if connection.getcode() != 200:
            exit(url + " http response not 200")
        connection.close()
    except:
        exit("problem with " + url)
