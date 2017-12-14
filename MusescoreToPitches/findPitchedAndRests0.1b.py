from xml.dom import minidom
																														#
notesDict = {55: 196, 56: 208, 57: 220, 58: 233, 59: 247, 60: 261, 61: 277, 62: 293, 63: 311, 64: 329, 65: 349, 66: 370, 
			 67: 392, 68: 415, 69: 440, 70: 466, 71: 494, 72: 523, 73: 554, 74: 587, 75: 622, 76: 659, 77: 698, 78: 740,
			 79: 784, 80: 830, 81: 880}

durationDict = {"measure": "4", "half": "2", "quarter": "1", "eighth": "0.125", "16th": "0.0625", "32th": "0.03125",
				 "64th": "0.015625"}

file = 'C:\\Users\\crack\\Documents\\GithubProjects\\PythonProj\\MusescoreToPitches\\data\\asd.mscx'

f = open("C:\\Users\\crack\\Documents\\GithubProjects\\PythonProj\\MusescoreToPitches\\data\\output\\canon.ino","w")

xmldoc = minidom.parse(file)

measurelist = xmldoc.getElementsByTagName("Measure")

bpin = input("*PIN CONNECTED TO BUZZER: ")
tempo = input("*SELECT TEMPO(in ms): ")
a = 0
f.write("#define BPIN %s\n\nint tempo = %s;\n\nvoid melody() {\n" % (bpin, tempo))
for measure in measurelist:
	for child1 in measure.childNodes:
		if child1.nodeType != child1.TEXT_NODE:
			if "Chord" in child1.tagName or "Rest" in child1.tagName:
				duration = str(child1.getElementsByTagName("durationType")[0].firstChild.nodeValue)
				if "Chord" in child1.tagName:
					note = int(child1.getElementsByTagName("Note")[0].getElementsByTagName("pitch")[0].firstChild.nodeValue)
					print("tone(BPIN, {}, {}*tempo);\n".format(notesDict[note], durationDict[duration]))
					f.write("	tone(BPIN, {}, {}*tempo);\n	delay({}*tempo);\n".format(notesDict[note], durationDict[duration], durationDict[duration]))
					pass
				if "Rest" in child1.tagName:
					print("delay({}*tempo);\n".format(durationDict[duration]))
					f.write("	delay({}*tempo);\n".format(durationDict[duration]))
					pass
f.write("}\n\nvoid setup() {\n\n}\n\nvoid loop() {\nmelody();\n}")
f.close()
print("\n\n---------DONE!----------")