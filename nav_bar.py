# this script is the single point of truth for the navigation bar of my personal website

import html_preprocessor
import os

keywords = ["<nav>", "</nav>"]

text = '\n\
			<ul>\n\
	    		<li><a href="index.html">About</a></li>\n\
	    		<li><a href="resume.html">Resume</a></li>\n\
	    		<li><a href="portfolio.html">Projects</a></li>\n\
			</ul>\n\
		'

#main script - cycle through directory and update files as needed
for file in os.listdir(os.chdir(os.getcwd())):
	if file.endswith(".html"):
		html_preprocessor.preprocess(file, keywords, text)
