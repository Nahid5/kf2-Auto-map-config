#Author: Nahid Sarker
#Date created: 10/8/2017
#Date modified: 10/30/2017
#Purpose: Looks in current directory for all kf2 map files and writes it in the format of:
'''
[MAPNAME.kfm KFMapSummary]
MapName=MAPNAME
MapAssociation=2
ScreenshotPathName=UI_MapPreview_TEX.UI_MapPreview_Placeholder
'''
#Created on: Windows 10 using Pycharm
#Tested on: Windows 10

import os

f = open("maps.txt", "w+")
arr_txt = [x for x in os.listdir('.') if x.endswith(".kfm")]
for map in arr_txt:
    f.write("[%s KFMapSummary]\n" % (map))
    f.write("MapName=%s\n" % (map.rsplit('.', 1)[0]))
    f.write('MapAssociation=2\n')
    f.write('ScreenshotPathName=UI_MapPreview_TEX.UI_MapPreview_Placeholder\n')
    f.write('\n')
f.close()
