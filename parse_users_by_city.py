from __future__ import division
import os, json

DIR = "people_htmls/"

# get all the users from the file
def parse_file(filename):
	names = []
	with open(filename) as f:
		parsing = False
		for line in f:
			if line.startswith("More Options"):
				parsing = True
				continue
			if parsing:
				names.append(line.split(os.linesep)[0])
				parsing = False
	return names

if __name__ == "__main__":
    # get all the filenames from the directory
    filenames = os.listdir(DIR)
    for fn in filenames:
        names = parse_file(DIR + fn)
        # write users only to json file
        ix = fn.index(".html")
        with open(DIR + fn[:ix] + "_names.json", "w+") as fp:
            json.dump(names, fp)

