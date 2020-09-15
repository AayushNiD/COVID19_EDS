import csv
import json
infile = open("https://api.covid19api.com/all","r")
outfile = open("https://api.covid19api.com/all2.csv","w")
writer = csv.writer(outfile)
for row in json.loads(infile.read()):
	writer.writer(row)
