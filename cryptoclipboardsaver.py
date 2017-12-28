#!/bin/python
# 
# Written by: Brad Nelson
# @redsquirrel_7
#
# Uses pyperclip module: https://github.com/asweigart/pyperclip

from modules.pyperclip import paste
from time import sleep

# Read clipboard and see if it changed after 10 seconds
prev_clipboard = paste()
sleep(10)
new_clipboard = paste()
if new_clipboard == prev_clipboard:
    print('Your clipboard has not changed in the past 10 seconds.')
else:
    print('Your clipboard has changed!')
    print('Previous clipboard: %s' % prev_clipboard)
    print('Current clipboard: %s' % new_clipboard)
