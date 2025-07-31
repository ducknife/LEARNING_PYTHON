import os
import xml.etree.ElementTree as ET

PATH = os.path.join(os.path.dirname(__file__), './A1.xml')

tree = ET.parse(PATH)
root = tree.getroot() #Project
print(root[2][0][0][1].get('useRefParam'))

