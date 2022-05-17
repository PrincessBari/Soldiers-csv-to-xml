import csv
from xml.etree.ElementTree import Element, SubElement, ElementTree
#our framework:
#
#<index>
#	<indexentry>
#		<name> [soldier name here] </name>
#		<note> [all of the extra data here] </note>
#		<ref> [the box and the folder here] </ref>
#</indexentry>

index = Element('index')

with open('mss_soldiers.csv','r') as mssfile:

	processed_csv = csv.reader(mssfile)

	
	for row in processed_csv:
		# this is where we're adding the child element:
		indexentry = SubElement(index,'indexentry')
		# index is the parent of indexentry
		

		name_field = row[1].strip() + ', ' + row[2].strip() 
		if row[3] != '':
			name_field = name_field + ' (alt name: ' + row[3].strip() + ')'

		if row[4] == '':
			unit_number = 'unknown'
		else:
			unit_number = row[4].strip()

		if row[5] == '':
			unit_state = 'unknown'
		else:
			unit_state = row[5].strip()

		if row[6] == '':
			unit_type = 'unknown'
		else:
			unit_type = row[6].strip()

		if row[7] == '':
			unit_letter = 'unknown'
		else:
			unit_letter = row[7].strip()

		if row[8] == '':
			rank = 'unknown'
		else:
			rank = row[8].strip()

		info = row[9].strip() + ' ' + row[10].strip() + ' ' + row[11].strip()
		info = info.strip()
		
		note_field = f"unit number: {unit_number}, unit state: {unit_state}, unit type: {unit_type}, unit letter: {unit_letter}, rank: {rank}, info: {info}  "
		# for notes, columns 4-11
		
		ref_field = f"Box: {row[12]}, Folder: {row[13]}"
		
		#print(name_field)
		#print(note_field)
		#print(ref_field)
		#print('--------')
		
		namefield_element = SubElement(indexentry, 'name')
		# indexentry is the parent of namefield
		namefield_element.text = name_field

		notefield_element = SubElement(indexentry, 'note')
		# indexentry is the parent of notefield
		notefield_element.text = note_field

		ref_element = SubElement(indexentry, 'ref')
		# indexentry is the parent of reffield
		ref_element.text = ref_field

ElementTree(index).write('mss_soldiers.xml')


	#0 = id
	#1 = last name
	#2 = first name
	#3 = other name
	#4 = unit number
	#5 = unit state
	#6 = unit type
	#7 = unit letter
	#8 = rank
	#9 = additional info
	#10 = alt info
	#11 = year
	#12 = box number
	#13 = folder number



