#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pyttsx3
import os
pyttsx3.speak('welcome to the computer you can interact with this by typping numbers of programme name itself')

while True:
    print("if you want app suggestions then type yes otherwise type  name of the programme which you want to execute")
    #print("do you want app suggestion to run")
    a = input()
    a = a.lower()
    if ('yes' in a) or ('yeah' in a) or ('y' in a ):
        # web browsing app
        print('**********web browsing apps**********')
        print("1. chrome")
        print("2. internet explorer")
        print('\n')
        
        
        print("**********editors*********** ")
        print("3. arduino")
        print("4. notepad")
        print('5. pycharm')
        print('\n')

        
        
        
        print("**********media player**********")
        print("6. mspalyer")
        print('\n')
        
        print("**********paint**********")
        print("6. paint")
        
        
        
    if ('run' in a) and  (('chrome' in a) or ('goolgle chrome' in a)):
        os.system('chrome')
        print('chrome is started')
    elif ('run' in a)and(('explorer' in a) or ('internet explorer' in a)or ('msedge' in a)):
        os.system('msedge')
        print('msedge is started')
    elif (('run' in a)and('pycharm' in a)) or ('pycharm64' in a):
        os.system('pycharm64')
        print('pycharm is started')
    elif ('run' in a)and(('paint' in a) or ('paint' in a) or  ('mspaint' in a)):
        os.system('paint')
        print('paint is started')
    elif ('run' in a)and(('mspalyer' in a) or ('video' in a) or  ('videoplayer' in a)):
        os.system('mspalyer')
        print('msplayer is started')
    elif ('run' in a)and(('arduino' in a) or ('ardiuno' in a) or  ('arduino ide' in a)):
        os.system('arduino')
        print('arduino is started')
    elif ('run' in a)and(('notepad' in a) or ('editor' in a) ):
        os.system('notepad is started')
    elif("don't run" in a):
        print("please make a choice to run from the following program")
        print("if you want to exit from the menu then print type exit")
        
        print('**********web browsing apps**********')
        print("1. chrome")
        print("2. internet explorer")
        print('\n')
        
        print("**********editors*********** ")
        print("3. arduino")
        print("4. notepad")
        print('5. pycharm')
        print('\n')

        print("**********media player**********")
        print("6. mspalyer")
        print('\n')
        
        print("**********paint**********")
        print("6. paint")
    elif("exit" in a) or ('stop' in a) or ('end' in a):
        exit()
        
        


# In[ ]:




