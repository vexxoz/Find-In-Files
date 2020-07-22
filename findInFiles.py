import os
path = "" #path of the starting directory
substrings = [] #list of things to search for
fileCount = 0

for root,d_names,f_names in os.walk(path):
	for f in f_names: #for file name
		with open(os.path.join(root, f), 'r', errors='ignore') as fp:#open file
			line = fp.readline() #read line by line
			while line:# for each line in file
				for listItem in substrings:
					if listItem in line: #check if line contains our search value
						print(os.path.join(root, f)) #print it was found in which file
				line = fp.readline() #go to next line in file
			fileCount+=1#increment the number of files read
print(str(fileCount) + " Files read!")#print how many files read
