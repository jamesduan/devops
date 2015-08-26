# encoding:utf8

import os

import xml.etree.ElementTree as ET
from colors import red

class XMLParse(object):
	
	def __init__(self, xml_file_path=""):

		if xml_file_path=="" or xml_file_path ==None:
			print red("please add xml file path.")

		if not os.path.exists(xml_file_path):
			print red("xml file is not exists! please check over it!")

		self.xml_file_path = xml_file_path

	def query(self, element_name="", attr_name=""):
		root = ET.parse(self.xml_file_path)
		element = root.findall(".//" + element_name)
		return element

