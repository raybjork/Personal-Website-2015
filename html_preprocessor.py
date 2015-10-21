# HTML Preprocessor
# purpose: replace html files when keywords are found

import os, re, fileinput

#look through html file and replace text between keywords
def preprocess(file, keywords, replace): 
	with open(file, 'r+') as f:
		text = re.sub("(?<=%s).*(?=%s)" % (keywords[0], keywords[1]), 
			replace, f.read(), flags=re.DOTALL)
		f.seek(0)
		f.write(text)
		f.truncate()
		f.close()

#scrape important parts from file, save in another file
#NOTE: requires file to be in compressed html to use - having difficulty
#	getting this part to work.  It is broken for now.  
def scrape(source, keywords, output):
	with open(source, 'r') as f:
		replace = re.search("(?=%s)(.*?)(?=%s)"%(keywords[2], keywords[3]),
			f.read()).group(0)		
		f.close()
		print(replace)
		preprocess(output, keywords, replace)

#this section is currently broken
#if "resume_raw" in file:
#	for i in range(len(resume.keywords)):
#		scrape(file, resume.keywords[i], resume.outputs[i])
