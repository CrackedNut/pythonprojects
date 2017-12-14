from xml.etree import ElementTree as ET

file = "C:\\Users\\crack\\Documents\\GithubProjects\\Python\\MusescoreToPitches\\data\\asd.xml"

dom = ET.parse(file)

print(dom)

notes = dom.find('Score/Part/Staff').firstChild

print(notes)
