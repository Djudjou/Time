##############################################################
# Kunos Simulazioni
# AC Python tutorial 04 : Get data from AC
#
# To activate create a folder with the same name as this file
# in apps/python. Ex apps/python/tutorial01
# Then copy this file inside it and launch AC
#
# Source : http://www.racingfr.com/forum/index.php?showtopic=42199&st=2385
# Created : 21/11/2014
# Edit : Djudjou ACFR
# Version : 0.1
#############################################################

import ac
import acsys
import time

label1=0

# This function gets called by AC when the Plugin is initialised
# The function has to return a string with the plugin name
def acMain(ac_version):
    global label1

    appWindow=ac.newApp("Time")
    ac.setTitle(appWindow,'')
    ac.setSize(appWindow,180,30)
    ac.setPosition(appWindow,1500,50)
    label1=ac.addLabel(appWindow,"")
    ac.setPosition(label1,60,5)

    return "Time"
	
def acUpdate(deltaT):
    global label1

    ac.setText(label1,time.strftime('%H:%M:%S',time.localtime()))
    