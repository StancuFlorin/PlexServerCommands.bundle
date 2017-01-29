import commands
import platform
import os

import server_commands

OS = platform.system()

APPLICATIONS_PREFIX = "/applications/plexservercommands"

NAME = L('Title')

ART  = 'art-default.jpg'
ICON = 'icon-default.png'
	
####################################################################################################

def Start():
    Plugin.AddPrefixHandler(APPLICATIONS_PREFIX, ApplicationsMainMenu, NAME, ICON, ART)

    Plugin.AddViewGroup("InfoList", viewMode="InfoList", mediaType="items")
    Plugin.AddViewGroup("List", viewMode="List", mediaType="items")

def ApplicationsMainMenu():
	oc = ObjectContainer(title1 = NAME)
	
	commands = ["Shutdown", "Reboot", "Hibernate", "Suspend"]
	for command in commands:
		oc.add(
			DirectoryObject(
				key = Callback(
					YesOrNo, 
					function = command, 
					title = L("Menu" + command)
				),
				title = L("Menu" + command),
				thumb = R("icon-" + command.lower() + ".png"),
				art = R(ART)
			)
		)

	return oc
	
def YesOrNo(function, title):
	oc = ObjectContainer(title1 = title)

	oc.add(
		DirectoryObject(
			key = Callback(getattr(server_commands, function)),
			title = L('MenuYes'),
			thumb = R('icon-yes.png'),
			art = R(ART)
		)
	)
	
	oc.add(
		DirectoryObject(
			key = Callback(ApplicationsMainMenu),
			title = L('MenuNo'),
			thumb = R('icon-no.png'),
			art = R(ART)
		)
	)
	
	return oc
	
def Shutdown():
	if OS == 'Windows':
		Log(os.system('shutdown -s'))
	else:
		Log(commands.getoutput('shutdown -h now'))
	return MessageContainer(L('MenuShutdown'), L('LogShutdown'))

def Reboot():
	if OS == 'Windows':
		Log(os.system('shutdown -r'))
	else:
		Log(commands.getoutput('shutdown -r -h now'))
		
	return MessageContainer(L('MenuReboot'), L('LogReboot'))

def Hibernate():
	if OS == 'Windows':
		Log(os.system('shutdown -h'))
	else:
		Log(commands.getoutput('pm-hibernate'))

	return MessageContainer(L('MenuHibernate'), L('LogHibernate'))

def Suspend():
	if OS == 'Windows':
		Log(os.system('shutdown -h'))
	else:
		Log(commands.getoutput('pm-suspend'))

	return MessageContainer(L('MenuSuspend'), L('LogSuspend'))
