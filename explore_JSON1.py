import json

infile = open("eq_data_1_day_m1.json", "r")
outfile = open("readable_eq_data.json", "w")

# load helps the information and places it in the correct file type but with indents
eq_data = json.load(infile)


json.dump(eq_data, outfile, indent=5)
