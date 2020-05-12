import csv

with open ("oui.csv") as input_csv:
	entries = csv.reader(input_csv, delimiter =',')
	output_txt = open("oui.txt", "w")

	#Create the starting part of the file
	output_txt.write("OUI/MA-L\nOrganization\ncompany_id\nOrganization\n\nAddress\n\n")

	first = True
	for row in entries:
		if first:
			first = False
			continue
		#Extract the relevant entries required from each row
		mac = row[1]
		vendor = row[2]
		address = row[3]
		
		#Recreate the text file based on the inputs
		output_txt.write(mac[0:2]+"-"+mac[2:4]+"-"+mac[4:6]+"   (hex)		"+vendor+"\n")
		output_txt.write(mac+"     (base 16)		"+vendor+"\n")
		output_txt.write("				"+address+"\n")
		output_txt.write("				"+address+"\n")
		output_txt.write("				"+address+"\n")
		output_txt.write("\n")
	output_txt.close()

