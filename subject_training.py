import pyHook
import pythoncom
import ctypes
import sys
sys.path.append("C:/Users/Megan/Documents/PhDSecondYear/Touchscreen/Matlab_Vowels")
import matlab.engine
eng = matlab.engine.start_matlab()
import winsound
import time
from random import randrange, uniform
import datetime


def onupperleft(event):
	print("upper left click detected")
	pos = event.Position
	print(pos)
	
	#Input limited to upper 1/12 of the screen. Otherwise, loop essentially continues
	if ((pos[0]) >= (2*1920/3)) and ((pos[1]) >= (3*1080/4)):
		#Click is in lower-right-hand corner, allow to proceed 
		winsound.PlaySound('Break_cue_right.wav',winsound.SND_FILENAME)
		
		#Break after one input in the correct area
		ctypes.windll.user32.PostQuitMessage(0)
		#print (pos)
	else:
		print ("incorrect reset")
	
	return True

def onupperleft(event):
	print("upper left click detected")
	pos = event.Position
	print(pos)
	
	#Input limited to upper 1/12 of the screen. Otherwise, loop essentially continues
	if ((pos[0]) >= (2*1920/3)) and ((pos[1]) >= (3*1080/4)):
		#Click is in lower-right-hand corner, allow to proceed 
		winsound.PlaySound('Break_cue_right.wav',winsound.SND_FILENAME)
		
		#Break after one input in the correct area
		ctypes.windll.user32.PostQuitMessage(0)
		#print (pos)
	else:
		print ("incorrect reset")
	
	return True

def onlowerright(event):
	print("lower right click detected")
	pos = event.Position
	print(pos)
	
	#Input limited to upper 1/12 of the screen. Otherwise, loop essentially continues
	if ((pos[0]) >= (2*1920/3)) and ((pos[1]) >= (3*1080/4)):
		#Click is in lower-right-hand corner, allow to proceed 
		winsound.PlaySound('Break_cue_right.wav',winsound.SND_FILENAME)
		
		#Break after one input in the correct area
		ctypes.windll.user32.PostQuitMessage(0)
		#print (pos)
	else:
		print ("incorrect reset")
	
	return True

def onupperright(event):
	print("upper right click detected")
	pos = event.Position
	print(pos)
	
	#Input limited to upper 1/12 of the screen. Otherwise, loop essentially continues
	if ((pos[0]) >= (2*1920/3)) and ((pos[1]) <= (1*1080/4)):
		#Click is in lower-right-hand corner, allow to proceed 
		winsound.PlaySound('Break_cue_right.wav',winsound.SND_FILENAME)
		
		#Break after one input in the correct area
		ctypes.windll.user32.PostQuitMessage(0)
		#print (pos)
	else:
		print ("incorrect reset")
	
	return True

def onupperleft(event):
	print("upper left click detected")
	pos = event.Position
	print(pos)
	
	#Input limited to upper 1/12 of the screen. Otherwise, loop essentially continues
	if ((pos[0]) <= (1*1920/3)) and ((pos[1]) >= (3*1080/4)):
		#Click is in lower-right-hand corner, allow to proceed 
		winsound.PlaySound('Break_cue_right.wav',winsound.SND_FILENAME)
		
		#Break after one input in the correct area
		ctypes.windll.user32.PostQuitMessage(0)
		#print (pos)
	else:
		print ("incorrect reset")
	
	return True

def onlowerleft(event):
	print("lower left click detected")
	pos = event.Position
	print(pos)
	
	#Input limited to upper 1/12 of the screen. Otherwise, loop essentially continues
	if ((pos[0]) <= (1*1920/3)) and ((pos[1]) <= (1*1080/4)):
		#Click is in lower-right-hand corner, allow to proceed 
		winsound.PlaySound('Break_cue_right.wav',winsound.SND_FILENAME)
		
		#Break after one input in the correct area
		ctypes.windll.user32.PostQuitMessage(0)
		#print (pos)
	else:
		print ("incorrect reset")
	
	return True	
	
	
def hook_setup_upperleft():
	print("Setting up the test")
	
	#Create hook manager
	hm = pyHook.HookManager()
	
	print("starting corner callback")
	
	hm.MouseAll = onupperleft
	
	#Set the hook
	hm.HookMouse()
	
	#Set the keyboard hook (that doesn't have a callback so I'm never going to use it) because otherwise it whines at me
	hm.HookKeyboard()
	
	pythoncom.PumpMessages()
	return hm

def hook_setup_upperright():
	#setting up the hook only to catch the reset cue indicating the subject is ready for the next trial
	print("Setting up the test")
	
	#Create hook manager
	hm = pyHook.HookManager()
	
	print("starting corner callback")
	
	#play the alternate oncluc which only accepts lower-right-hand reset presses
	hm.MouseAll = onupperright
	
	#Set the hook
	hm.HookMouse()
	
	#Set the keyboard hook (that doesn't have a callback so I'm never going to use it) because otherwise it whines at me
	hm.HookKeyboard()
	
	pythoncom.PumpMessages()
	return hm
	
def hook_setup_lowerleft():
	#setting up the hook only to catch the reset cue indicating the subject is ready for the next trial
	print("Setting up the test")
	
	#Create hook manager
	hm = pyHook.HookManager()
	
	print("starting corner callback")
	
	#play the alternate oncluc which only accepts lower-right-hand reset presses
	hm.MouseAll = onlowerleft
	
	#Set the hook
	hm.HookMouse()
	
	#Set the keyboard hook (that doesn't have a callback so I'm never going to use it) because otherwise it whines at me
	hm.HookKeyboard()
	
	pythoncom.PumpMessages()
	return hm

def hook_setup_lowerright():
	#setting up the hook only to catch the reset cue indicating the subject is ready for the next trial
	print("Setting up the test")
	
	#Create hook manager
	hm = pyHook.HookManager()
	
	print("starting corner callback")
	
	#play the alternate oncluc which only accepts lower-right-hand reset presses
	hm.MouseAll = onlowerright
	
	#Set the hook
	hm.HookMouse()
	
	#Set the keyboard hook (that doesn't have a callback so I'm never going to use it) because otherwise it whines at me
	hm.HookKeyboard()
	
	pythoncom.PumpMessages()
	return hm


	
if __name__== '__main__':
	
	#Start off by calling the hook a few times to get rid of the lag at the beginning
	hm_temp = hook_warmup()
	
	#Run a test block
	test_session(3,24)
	
	#Wait for key press for next trial block to continue
	print("Press any key to continue")
	msvcrt.getch()
	#Give me 5 seconds to switch back to the waiting screen
	time.sleep(5)
		
	for cur_block in range (0,full_trial_blocks):
		#Calling the hook once per trial in trial block
		train_session(3,120)
		
		#Wait for key press for next trial block to continue
		print("Press any key to continue")
		msvcrt.getch()
		#Give me 5 seconds to switch back to the waiting screen
		time.sleep(5)
	
	for cur_short_block in range (0,5):
		#Alternate between training and testing for the final block
		#run a training session
		train_session(3,24)
		
		#run a test session
		test_session(5,5)