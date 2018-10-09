# Chris Web Access.

# This command imports sys for exit command used later and open webbrowser.
import sys
import webbrowser


# This section defines name and password values.
myName = 'Chris'
myPassword = 'dogs'
response = 'exit'


# This section prompts for username. If username is valid prompts for PW.
print ('What is your name?')
myName = input()
if myName == 'Chris':
    print ('Hello Chris, What is your password?')
else:
    sys.exit()
myPassword = input()
if myPassword == 'dogs':
    webbrowser.open ('https://www.google.com')    
    print ('Access Granted')
    sys.exit()
else:
    print ('Try Again')
myPassword = input()
if myPassword == 'dogs':
    webbrowser.open ('https://www.google.com')    
    print ('Access Granted')
    sys.exit()
else:
    print ('Last Chance. You are not very good at remembering your password.')
    print ('You will be logged out if you are wrong')
myPassword = input()
if myPassword == 'dogs':
    webbrowser.open ('https://www.google.com')    
    print ('Access Granted')
    sys.exit()
    print ('3 strikes and you are out')
