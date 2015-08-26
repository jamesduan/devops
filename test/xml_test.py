# encoding:utf8

import xml.etree.ElementTree as ET

root = ET.parse("../conf/Target.xml")

for element in root.findall(".//Targets/Target[@SpecName='apigw']"):
	print element.attrib


