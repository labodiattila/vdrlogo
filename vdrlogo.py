#!/usr/bin/python
import downloader, imagemagix, re, time, argparse, os
from subprocess import *
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

logo_width = 132
logo_height = 99
workfoldername = "work/"
lyngsat_logo_URL = "http://www.lyngsat-logo.com/tvcountry/"
not_found_URL = "http://www.gamescast.tv/press/media/tv.png"

acceptreplace_sem = True
lyngsat_sem = False
google_sem = False
show_differences = False

def main(vdrchannels,country_list,outputpath,endline,size,delay):
		#create work folder, and delete old tempfiles
		run_cmd("mkdir " + workfoldername)
		run_cmd("mkdir " + outputpath)
		run_cmd("rm work.html")

		#read vdr channels.conf file
		f = open(vdrchannels)
		channels = f.readlines()
		f.close()

		#if lyngsat sem is true, download them
		if(lyngsat_sem):
			downloader.lyngsat_download(country_list)

		clearing(channels,os.listdir(workfoldername),outputpath,endline,size,delay)


def clearing(channels,picons,outputpath,endline,size,delay):
	for num in range(0,len(channels)):

		if channels[num].find("->") == -1:
			position = channels[num].index(';')
			channel_name = channels[num][0:position].replace("/","")

			if channel_name == endline:
				break

			if search_and_find(channel_name,picons):
				if not show_differences:
					run_cmd("cp '" + workfoldername + channel_name.lower() + ".png' " + outputpath)
			else:
				print("Not Found: "+channel_name)
				if not show_differences:
					maybetrythis(channel_name,picons,outputpath,size,delay)

def search_and_find(channel_name,picons):
	for num in range(0,len(picons)):
		if picons[num] == channel_name.lower()+".png":
			return True
	return False

def maybetrythis(channel_name,picons,outputpath,size,delay):
	found = False

	for num in range(0,len(picons)):

		if not picons[num].lower().find(channel_name.lower())== -1:
			if(acceptreplace_sem):
				print("Copy best matched picon for: " + channel_name)
				run_cmd('cp "' + workfoldername +picons[num] + '" "' + outputpath + channel_name + '.png"')
				found = True
				break
			elif(not show_differences):
				print("Try this: "+picons[num][0:-1])

	if(not found and google_sem):
			googleURL = downloader.google_download(channel_name.replace(" ","+"))
			run_cmd('wget -q ' + googleURL + '  -O "' + outputpath + channel_name + '.png"')
			imagemagix.convert_img(outputpath + channel_name + ".png",size)
			time.sleep(int(delay))

def run_cmd(cmd):
	p = Popen(cmd, shell=True, stdout=PIPE)
	output = p.communicate()[0]
	return output

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='If you like it, please send some coins :) Paypal: labodiattila@gmail.com')
	parser.add_argument('-c','--channels', help='VDR channels.conf file path',required=True)
	parser.add_argument('-o','--outputpath', help='Output folder path', required=True)
	parser.add_argument('-C','--country', help='Country codes', required=True)
	parser.add_argument('-n','--notfoundurl', help='Not found image URL', required=False)
	parser.add_argument('-l','--lyngsatdwnl', help='Download from lyngsat', required=True)
	parser.add_argument('-g','--googledwnl', help='Download from google search', required=True)
	parser.add_argument('-e','--endline', help='Last channel name in the vdr channels.conf file', required=False)
	parser.add_argument('-s','--size', help='Set the logo size (Default: 132x99)', required=False)
	parser.add_argument('-d','--delay', help='Set the delay time(Between two google searching)', required=True)
	args = parser.parse_args()

	if(not args.notfoundurl == ""):
		not_found_URL = args.notfoundurl
	
	if(args.lyngsatdwnl.lower() == "yes"):
		lyngsat_sem = True

	if(args.googledwnl.lower() == "yes"):
		google_sem = True

	main(args.channels,args.country,args.outputpath,args.endline,args.size,args.delay)
