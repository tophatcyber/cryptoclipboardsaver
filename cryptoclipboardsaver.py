#!/bin/python
#
# Crypto Clipboard Saver v0.2.0
# Keep your BitCoin wallet safe from those pesky ScR1p7 K1dd13$
#
# Simple script that checks your clipboard either automatically
# or every so many seconds that you choose.
#
# Written by: Brad Nelson
# @redsquirrel_7
#
# Written for: Top Hat Cyber
#
# Uses pyperclip module: https://github.com/asweigart/pyperclip

from modules.pyperclip import paste
from time import sleep

# Get amount of time from user
def timed_notify():
    time = input('Enter the amount of time in seconds before the clipboard is checked: ')
    if len(time) == 0:
        print("You didn't enter anything.")
        timed_notify()
    else:
        time = int(time)
        check_clipboard(time)

# Read clipboard and see if it changed after 10 seconds
def check_clipboard(seconds):
    prev_clipboard = paste()
    sleep(seconds)
    new_clipboard = paste()
    if new_clipboard == prev_clipboard:
        print('Your clipboard has not changed in the past %s seconds.' % seconds)
        check_clipboard(seconds)
    else:
        print('Your clipboard has changed!')
        print('Previous clipboard: %s' % prev_clipboard)
        print('Current clipboard: %s' % new_clipboard)
        check_clipboard(seconds)

# Automatically check clipboard every 0.1 seconds
def auto_notify():
    prev_clipboard = paste()
    sleep(0.1)
    new_clipboard = paste()
    if new_clipboard == prev_clipboard:
        auto_notify()
    else:
        print('Your clipboard has changed!')
        print('Previous clipboard: %s' % prev_clipboard)
        print('Current clipboard: %s' % new_clipboard)
        auto_notify()

# Let user decide what mode to use
print('Keep your clipboard safe during BitCoin transactions.')
print('0 - Automatically notify me if my clipboard changes')
print('1 - Let me choose how long before checking the clipboard')
choice = input('Please choose an option (Default 0): ')
if choice == 0 or len(choice) == 0:
    print('Starting automatic mode...')
    auto_notify()
elif int(choice) == 1:
    timed_notify()

