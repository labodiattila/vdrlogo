#!/usr/bin/python
import vdrlogo,struct

def convert_img(logopath):
	print(logopath)
	with open(logopath, 'rb') as f:
		data = f.read()
	
	#get size
	w, h = struct.unpack('>LL', data[16:24])
	
	#create white png
	vdrlogo.run_cmd("convert -size " + str(w) + "x" + str(h) + " xc:white bckgr.png")

	#flatten pngs
	vdrlogo.run_cmd('convert -flatten bckgr.png "' + logopath + '" temp.png')
	
	#resize to 132x99
	vdrlogo.run_cmd('convert -resize 132x99 temp.png "' + logopath +'"')
