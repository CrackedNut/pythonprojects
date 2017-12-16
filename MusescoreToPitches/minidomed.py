from xml.dom import minidom

file = 'C:\\Users\\crack\\Documents\\GithubProjects\\Python\\MusescoreToPitches\\data\\asd.xml'

notesDict = {60: 261, 61: 277, 62: 293, 63: 311, 64: 329, 65: 349, 66: 370, 67: 392, 68: 415, 69: 440, 70: 466, 71: 494,
             72: 523, 73: 554, 74: 587, 75: 622, 76: 659, 77: 698, 78: 740, 79: 784, 80: 830, 81: 880}


def findNotes():
	xmldoc = minidom.parse(file)

	itemlist = xmldoc.getElementsByTagName('pitch')

	print(len(itemlist))

	outName = "C:\\users\\crack\\Desktop\\" + input("Enter the name for the new file: ") + ".txt"
	f = open(outName, "w")

	for s in itemlist:
   	 a = int(s.firstChild.nodeValue)
   	 f.write('tone(BPIN, {}, );\ndelay();\n'.format(notesDict[a]))

	f.close()
