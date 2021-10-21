import csv
import sys

csv_file = open(sys.argv[1],'r')
csv_reader = csv.reader(csv_file, delimiter = ',')
with open(sys.argv[2],'w') as txt_file:
	for row in csv_reader:
		txt_file.write(row[0] + ' ' + row[1] + '\n')