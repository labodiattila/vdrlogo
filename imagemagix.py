#!/usr/bin/python
import vdrlogo,sys,struct

def convert_img(logopath,size):
	try:
		vdrlogo.logo_width = int(size.split("x")[0])
		vdrlogo.logo_height = int(size.split("x")[1])
	except AttributeError:
		pass
	
	#create white png
	vdrlogo.run_cmd("convert -size " + str(vdrlogo.logo_width) + "x" + str(vdrlogo.logo_height) + " xc:white bckgr.png")

	#resize
	vdrlogo.run_cmd('convert -resize ' + str(vdrlogo.logo_width) + 'x' + str(vdrlogo.logo_height)+ ' "' + logopath +'" resized.png')

	with open("resized.png", 'rb') as f:
		data = f.read()
	
	#get size
	w, h = struct.unpack('>LL', data[16:24])

	#flatten pngs
	vdrlogo.run_cmd('convert -page +0+'+ str(vdrlogo.logo_height/2-(h/2)) +' -flatten bckgr.png resized.png "' + logopath + '"')
