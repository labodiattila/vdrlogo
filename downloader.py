#!/usr/bin/python
import urllib2,json,time,vdrlogo,os

def lyngsat_download(country_list):
	#Download logo HTML
	code_list = country_list.split(",")

	for num in range(0,len(code_list)):
		vdrlogo.run_cmd("wget -q " + vdrlogo.lyngsat_logo_URL + code_list[num] + ".html -O out.html")
		vdrlogo.run_cmd('cat out.html | grep "\\../logo/tv" >> work.html')
		vdrlogo.run_cmd("rm out.html")
	
	f = open("work.html")
	source = f.readlines()
	f.close()

	get_urls(source)

	#delete temp files
	vdrlogo.run_cmd("rm *.html")

def get_urls(source):

	for num in range(0,len(source)):
		if(source[num].find("../logo")):
			firstposition = source[num].index("../logo")
			lastposition =source[num].index(".png")
			dirtypath=source[num][firstposition:lastposition+4]

			#Cleaning
			source[num]=source[num][firstposition:lastposition+4].replace("..","http://www.lyngsat-logo.com")

			#Download
			lastslashposition = source[num].rindex("/") +1
			filename = source[num][lastslashposition:len(source[num])]

			#Cleaning tools
			if not(filename.find("_hu") == -1):
				filename = filename.replace("hu","")
			elif not(filename.find("_ro") == -1):
				filename = filename.replace("ro","") 
			elif not(filename.find("_eu")) == -1:
				filename = filename.replace("eu","")
			elif not(filename.find("_us")) == -1:
				filename = filename.replace("us","")
			elif not(filename.find("_ce")) == -1:
				filename = filename.replace("ce","")

			filename = filename.replace(" ","")
			filename = filename.replace("_"," ")
			filename = filename.replace(" .",".")

			vdrlogo.run_cmd('wget -q '+source[num]+' -O "'+vdrlogo.workfoldername+filename.lower()+'"')
			

def google_download(channel_name):
	print(channel_name)
	url = ('https://ajax.googleapis.com/ajax/services/search/images?' + 'v=1.0&q='+channel_name+'&as_filetype=png&as_sitesearch=http://www.lyngsat-logo.com')
	request = urllib2.Request(url, None)
	response = urllib2.urlopen(request)

	# Process the JSON string.
	results = json.load(response)
	# now have some fun with the results...
	try:
		pix_url = results['responseData']['results'][0]['url']
		if pix_url is not None:
			print("Downloaded with googlesearch: " +channel_name)
			return pix_url	
		else:
			return vdrlogo.not_found_URL
		
	except IndexError:
		print("Not found on Google")
		return vdrlogo.not_found_URL


