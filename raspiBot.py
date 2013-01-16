#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# PyGtalkRobot: A simple jabber/xmpp bot framework using Regular Expression Pattern as command controller
# Copyright (c) 2008 Demiao Lin <ldmiao@gmail.com>
#
# RaspiBot: A simple software robot for Raspberry Pi based on PyGtalkRobot
# Copyright (c) 2013 Michael Mitchell <michael@mitchtech.net>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# PyGtalkRobot Homepage: http://code.google.com/p/pygtalkrobot/
# RaspiBot Homepage: http://code.google.com/p/pygtalkrobot/
#
import time
import subprocess
import RPi.GPIO as GPIO
from PyGtalkRobot import GtalkRobot

BOT_GTALK_USER = 'bot_username@gmail.com'
BOT_GTALK_PASS = 'password'
BOT_ADMIN = 'admin_username@gmail.com'

GPIO.setmode(GPIO.BOARD) # or GPIO.setmode(GPIO.BCM)
############################################################################################################################

class RaspiBot(GtalkRobot):
    
    #Regular Expression Pattern Tips:
    # I or IGNORECASE <=> (?i)      case insensitive matching
    # L or LOCALE <=> (?L)          make \w, \W, \b, \B dependent on the current locale
    # M or MULTILINE <=> (?m)       matches every new line and not only start/end of the whole string
    # S or DOTALL <=> (?s)          '.' matches ALL chars, including newline
    # U or UNICODE <=> (?u)         Make \w, \W, \b, and \B dependent on the Unicode character properties database.
    # X or VERBOSE <=> (?x)         Ignores whitespace outside character sets
    
    #"command_" is the command prefix, "001" is the priviledge num, "setState" is the method name.
    #This method is used to change the state and status text of the bot.
    def command_001_setState(self, user, message, args):
        #the __doc__ of the function is the Regular Expression of this command, if matched, this command method will be called. 
        #The parameter "args" is a list, which will hold the matched string in parenthesis of Regular Expression.
        '''(available|online|busy|dnd|away|idle|out|xa)( +(.*))?$(?i)'''
        show = args[0]
        status = args[1]
        jid = user.getStripped()

        # Verify if the user is the Administrator of this bot
        if jid == BOT_ADMIN:
            print jid, " ---> ",bot.getResources(jid), bot.getShow(jid), bot.getStatus(jid)
            self.setState(show, status)
            self.replyMessage(user, "State settings changed！")

    #This method turns on the specified GPIO pin
    def command_003_pinOn(self, user, message, args):
        '''(pinon|pon|on|high)( +(.*))?$(?i)'''
        print "GPIO pin on\n"
        pin_num = args[1]
        GPIO.setup(int(pin_num), GPIO.OUT)
        GPIO.output(int(pin_num), True)
        self.replyMessage(user, "\nPin on: "+ pin_num +" at: "+time.strftime("%Y-%m-%d %a %H:%M:%S", time.gmtime()))

    #This method turns off the specified GPIO pin
    def command_003_pinOff(self, user, message, args):
        '''(pinoff|poff|off|low)( +(.*))?$(?i)'''
        print "GPIO pin off\n"
        pin_num = args[1]
        GPIO.setup(int(pin_num), GPIO.OUT)
        GPIO.output(int(pin_num), False)
        self.replyMessage(user, "\nPin off: "+ pin_num +" at: "+time.strftime("%Y-%m-%d %a %H:%M:%S", time.gmtime()))

    #This method writes to the specified GPIO pin
    def command_003_write(self, user, message, args):
        '''(write|w)( +(.*))?$(?i)'''
        print "GPIO pin write\n"
        arg_str = args[1]
        aargs = arg_str.split()
        pin_num = aargs[0]
        state = aargs[1]

        if int(state) == 1:
            GPIO.output(int(pin_num), True)
            self.replyMessage(user, "Pin on: "+ pin_num +" at: "+time.strftime("%Y-%m-%d %a %H:%M:%S", time.gmtime()))
        elif int(state) == 0:
            GPIO.output(int(pin_num), False)
            self.replyMessage(user, "Pin off: "+ pin_num +" at: "+time.strftime("%Y-%m-%d %a %H:%M:%S", time.gmtime()))

    #This method reads the value of the specified GPIO pin
    def command_003_read(self, user, message, args):
        '''(read|r)( +(.*))?$(?i)'''
        print "GPIO pin read\n"
        pin_num = args[1]
        GPIO.setup(int(pin_num), GPIO.IN)
        pin_value = GPIO.input(int(pin_num))
        self.replyMessage(user, "\nPin read: "+ pin_num + " value: " + str(pin_value) + " at: "+time.strftime("%Y-%m-%d %a %H:%M:%S", time.gmtime()))
    
    #This executes the shell command argument after 'shell' or 'bash'
    def command_003_shell(self, user, message, args):
        '''(shell|bash)( +(.*))?$(?i)'''
        cmd = args[1]
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = ""
        for line in p.stdout.readlines():
            output += line
            print line,
        retval = p.wait()
        self.replyMessage(user, output +" at: "+time.strftime("%Y-%m-%d %a %H:%M:%S", time.gmtime()))
    
    #This method is the default response
    def command_100_default(self, user, message, args):
        '''.*?(?s)(?m)'''
        self.replyMessage(user, time.strftime("%Y-%m-%d %a %H:%M:%S", time.gmtime()))

############################################################################################################################
if __name__ == "__main__":
    bot = RaspiBot()
    bot.setState('available', "Raspi Gtalk Robot")
    bot.start(BOT_GTALK_USER, BOT_GTALK_PASS)
