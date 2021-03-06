<b>vdrlogo</b>
=======

Automated Channel logo downloader for VDR, and XBMC.

<b>Main features:</b>
- Download logos, specified to your country from lyngsat.
- Download missing channel logos from google
- Resize logos to standard 132x99px and create white, none transparented background for them.
- Rename it to match your VDR channel name.

<b>Requirements:</b>

<b>Platforms:</b>
- Debian, Ubuntu
- CentOS, Red Hat, Fedora

<b>Component requirements:</b>
- Python 3+
- Python URLlib2 package
- imagemagick package <code>sudo apt-get install imagemagick</code>
- VDR channels.conf file (VDR and XBMC is not required!)

<b>Functions:</b>

- <code>-h | --help</code>
- <code>-c | --channels /path/to/channels.conf</code> <b>Required</b> Path to the VDR generated channels.conf file.
- <code>-o | --outputpath /path/to/out/folder</code> <b>Required</b> Path to the output folder.
- <code>-C | --country de|de,hu,it...</code> <b>Required</b> Country code for the lyngsat download.
- <code>-l | --lyngsatdownl yes|no </code> <b>Required</b> Enable, or disable downloading logos from lyngsat-logo.com.
- <code>-g | --googledwnl yes|no </code> <b>Required</b> Enable, or disable downloading logos with Google picture search API.
- <code>-c | --channels /path/to/channels.conf</code> <b>Required</b> Path to the VDR generated channels.conf file.
- <code>-e | --endline "last channel name"</code> <b>Optional</b> Download logos until this channel. 
- <code>-n | --notfoundurl "www.path.to.dummy.pics"</code> <b>Optional</b> Use this logo, if the searching method not found the channel.
- <code>-s | --size 132x99</code> <b>Optional</b> Set channel logo size.
- <code>-d | --delay Delay between two google search. It is necessary, because Google blocking the request. The recommended value is 10-20sec

<b>Example:</b>

<code>./vdrlogo.py -c channels.conf -o output/ -C ro,hu -l yes -g yes -s 132x99 -d 20 -e "DIGI FILM"</code>

I'm not a professional programer, so use at your own risk! :)
