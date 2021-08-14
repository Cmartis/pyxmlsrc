#!/usr/bin/python3
import xml.etree.cElementTree as ET
import xml.dom.minidom

root = ET.Element("root")
doc = ET.SubElement(root, "doc")

ET.SubElement(doc, 'field1', name = 'blah').text = 'some value1'
ET.SubElement(doc, "field2", name = "asdfasd").text = "some value2"

tree = ET.ElementTree(root)


tree.write("filename.xml")








