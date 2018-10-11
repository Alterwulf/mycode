#!/usr/bin/env python3
######## EXPLORE READ ##########
## create file object in "r"ead mode
configfile = open('vlanconfig.cfg', 'r')

print("here is what read does")
print(configfile.read())
configfile.close()


configfile = open('vlanconfig.cfg', 'r')
print("here is what readlines does")
print(configfile.readlines())
configfile.close()

print("here is what strip does")
x = "             text      sdf    "
print(x.strip())



## display file to the screen - .read()
#print(configfile.read().splitlines())

## close file
#configfile.close()

######## EXPLORE READLINES ##########
## re-create file object to explore new method
configfile = open('vlanconfig.cfg', 'r')

## make a list of file lines - .readlines()
configlist = configfile.readlines()


## Iterate thrhough configlist
for x in configlist:
#    print(x, end="")
    print(x.strip())
## Always close your file
configfile.close()
