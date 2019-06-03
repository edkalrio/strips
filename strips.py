#!/usr/bin/env python3

import datetime
import re

import requests

url_list = [
	"https://www.gocomics.com/garfieldespanol/",
	"https://www.gocomics.com/peanuts-espanol/",
	"https://www.gocomics.com/calvinandhobbesespanol/",
	"https://www.gocomics.com/dilbert-en-espanol/"
]

now = datetime.datetime.utcnow().isoformat() + "Z"
gocomics_date = datetime.date.today().strftime("%Y/%m/%d")
hash_regex = re.compile(r'assets.amuniversal.com/(.*)\"')
hash_list = []

for url in url_list:
	url += gocomics_date
	res = requests.get(url)
	mo = hash_regex.search(res.text)
	hash_list.append(mo.group(1))

atom = f"""<?xml version="1.0" encoding="utf-8"?>
<?xml-stylesheet type="text/xsl" href="strips.xsl"?>
<feed xmlns="http://www.w3.org/2005/Atom">

	<title>Gocomics</title>
	<link rel="self" href="https://copype.ga/gocomics.xml/"/>
	<updated>{now}</updated>
	<id>https://copype.ga/gocomics.xml/</id>

	<entry>
		<id>{hash_list[0]}</id>
		<author>
			<name>Garfield</name>
			<uri>https://www.gocomics.com/garfieldespanol</uri>
		</author>
		<updated>{now}</updated>
		<title>Garfield</title>
		<link rel="alternate" href="https://www.gocomics.com/garfieldespanol/{gocomics_date}/"/>
		<content type="html"><![CDATA[<img src="https://assets.amuniversal.com/{hash_list[0]}/">]]></content>
	</entry>

	<entry>
		<id>{hash_list[1]}</id>
		<author>
			<name>Peanuts</name>
			<uri>https://www.gocomics.com/peanuts-espanol/</uri>
		</author>
		<updated>{now}</updated>
		<title>Peanuts</title>
		<link rel="alternate" href="https://www.gocomics.com/peanuts-espanol/{gocomics_date}/"/>
		<content type="html"><![CDATA[<img src="https://assets.amuniversal.com/{hash_list[1]}/">]]></content>
	</entry>

	<entry>
		<id>{hash_list[2]}</id>
		<author>
			<name>Calvin and Hobbes</name>
			<uri>https://www.gocomics.com/calvinandhobbesespanol/</uri>
		</author>
		<updated>{now}</updated>
		<title>Calvin and Hobbes</title>
		<link rel="alternate" href="https://www.gocomics.com/calvinandhobbesespanol/{gocomics_date}/"/>
		<content type="html"><![CDATA[<img src="https://assets.amuniversal.com/{hash_list[2]}/">]]></content>
	</entry>

	<entry>
		<id>{hash_list[3]}</id>
		<author>
			<name>Dilbert</name>
			<uri>https://www.gocomics.com/dilbert-en-espanol/</uri>
		</author>
		<updated>{now}</updated>
		<title>Dilbert</title>
		<link rel="alternate" href="https://www.gocomics.com/dilbert-en-espanol/{gocomics_date}/"/>
		<content type="html"><![CDATA[<img src="https://assets.amuniversal.com/{hash_list[3]}/">]]></content>
	</entry>
</feed>"""

print(atom)