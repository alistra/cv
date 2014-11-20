#!/usr/bin/env python
import fileinput, re, sys
import urllib2

urls = []

for line in fileinput.input():
    urls += re.findall('\\href\{(http.*?)\}', line)

for url in urls:
    try:
        req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
        connection = urllib2.urlopen(req)
        if connection.getcode() > 400:
            exit(url + " FAIL http response not 200")
        connection.close()
        print(url + " OK")
    except urllib2.HTTPError, e:
        print e.fp.read()

    except Exception as e:
        exit(url + " FAIL exception")
