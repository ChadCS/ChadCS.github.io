import os
import PIL
from PIL import Image

chadTechOnline =  '''

<html>
	<head>
		<title>ChadTech Online</title>
	</head>
	<body>
	<body bgcolor=#"000000">
	<img src="onebar.PNG" style= "position:absolute; top: 0px;left: 2px;"/>
	<img src="chadtechonline.PNG" style= "position:absolute; top: 4px;left: 2px;"/>'
	<img src="twobar.PNG" style= "position:absolute; top: 150px;left: 2px;"/>'

'''

os.chdir(os.getcwd()+'//images')

nextXPos, nextYPos = 0,162

for directoryNumber in range(len(os.listdir(os.getcwd()))):
	beginin = '<img src='+'"./images/'+str(len(os.listdir(os.getcwd()))-1-directoryNumber)
	os.chdir(os.getcwd()+'\\'+str(len(os.listdir(os.getcwd()))-1-directoryNumber))
	imX,imY=0,0

	for imageInDir in os.listdir(os.getcwd()):
		if imageInDir.endswith('.PNG'):
				chadTechOnline+=beginin+'/'+imageInDir+'" style= "position:absolute; top:'+str(nextYPos)+'px;left: 2px;"/>'
				im = Image.open(imageInDir)
				imX,imY = im.size
				nextYPos+=imY
				chadTechOnline+='<img src="onebar.PNG" style= "position:absolute; top:'+str(nextYPos)+ 'px;left: 2px;"/>'
				nextYPos+=4

	os.chdir(os.path.dirname(os.getcwd()))

for yit in range(nextYPos-2):
	chadTechOnline+='<img src="vbar.PNG" style= "position:absolute;  top:'+str(yit)+ 'px; left: 1004px;"/>'
for yit in range(nextYPos-2):
	chadTechOnline+='<img src="vbar.PNG" style= "position:absolute;  top:'+str(yit)+ 'px; left: 0px;"/>'

os.chdir(os.path.dirname(os.getcwd()))
chadTechOnline+='''	</body></html>'''

mainpage = open('index.html','w')
mainpage.write(chadTechOnline)
mainpage.close()