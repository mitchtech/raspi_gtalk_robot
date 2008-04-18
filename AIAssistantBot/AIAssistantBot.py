#!/usr/bin/python
# -*- coding: utf-8 -*-

# PyGtalkRobot: A simple jabber/xmpp bot framework using Regular Expression Pattern as command controller
# Copyright (c) 2008 Demiao Lin <ldmiao@gmail.com>
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
# Homepage: http://code.google.com/p/pygtalkrobot/
#

#
# This is an sample PyGtalkRobot
#

import sys
import time
import ConfigParser

from PyGtalkRobot import GtalkRobot
from config import config
from AIAWeb import AIAssistantWeb

#############################################################################################################################

def utf8(onestr):
    newstr = onestr
    try:
        newstr = unicode(newstr, 'cp936', 'ignore')
    except:
        pass
    return newstr.encode('utf-8', 'ignore')
#############################################################################################################################

class AIABot(GtalkRobot):

    #########################################################################################################################
    aiaweb = None
    
    def addChat(self, email, message):
        if not self.aiaweb:
            self.aiaweb = AIAssistantWeb()
        
        return self.aiaweb.addChat(email, message)

    #########################################################################################################################
    cfg = config("cfg.ini")
    
    def getCfgValue(self, section, option, type="str"):
        return self.cfg.get(section, option, type)

    def setCfgValue(self, section, option, value):
        return self.cfg.set(section, option, value)
    
    #########################################################################################################################
    #Pattern Tips:
    # I or IGNORECASE <=> (?i)      case insensitive matching
    # L or LOCALE <=> (?L)          make \w, \W, \b, \B dependent on the current locale
    # M or MULTILINE <=> (?m)       matches every new line and not only start/end of the whole string
    # S or DOTALL <=> (?s)          '.' matches ALL chars, including newline
    # U or UNICODE <=> (?u)         Make \w, \W, \b, and \B dependent on the Unicode character properties database.
    # X or VERBOSE <=> (?x)         Ignores whitespace outside character sets

    #command_ is the command prefix, 001 is the priviledge num, setState is the method name
    def command_001_setState(self, user, message, args):
        """(available|online|on|busy|dnd|away|idle|out|off|xa)( +(.*))?$(?i)"""
        show = args[0]
        status = args[1]
        if status:
            status = status.strip();
        jid = user.getStripped()
        # Verify if the user is the Administrator of this bot
        if jid == 'ldmiao@gmail.com':
            print jid, " ---> ",bot.getResources(jid), bot.getShow(jid), bot.getStatus(jid)
            self.setState(show, status)
            show, status = self.getState()
            self.saveState(show, status)
            self.replyMessage(user, "状态设置成功！")
    def command_002_saveToAIAWeb(self, user, message, args):
        """[h|help|how](?i)"""
        helpMsg = "Artifical Intelligence Assistant (AIA)\n"
        helpMsg = helpMsg + "AIA is an assistant that can do tasks like keeping accounts, arranging TODOs and so on intelligently.\n"
        helpMsg = helpMsg + "All Chats will be Saved in http://aiassistant.appspot.com/chat/"
        
        self.replyMessage(user, helpMsg)
        
    def command_003_saveToAIAWeb(self, user, message, args):
        """(.*)(?s)(?m)"""
        jid = user.getStripped()
        content = args[0]
        #print content
        
        if self.addChat(jid, content):
            replyMsg = "Chat Saved in http://aiassistant.appspot.com/chat/"
        else:
            replyMsg = "Error occured."
        replyMsg = replyMsg + " ["+time.strftime("%Y-%m-%d %a %H:%M:%S", time.localtime())+"]"
        
        self.replyMessage(user, replyMsg)

    #########################################################################################################################
    def saveState(self, show, status):
        self.setCfgValue('init_param', 'show', show)
        self.setCfgValue('init_param', 'status', status)
    
    #########################################################################################################################
    #overriden
    def start(self):
        name = self.getCfgValue('account', 'name')
        pwd = self.getCfgValue('account', 'pwd')
        show = self.getCfgValue('init_param', 'show')
        status = self.getCfgValue('init_param', 'status')
        self.setState(show, status)
        
        GtalkRobot.start(self, name, pwd)
    
    #########################################################################################################################
    
############################################################################################################################
if __name__ == "__main__":
    bot = AIABot()
    #bot = AIABot(debug=['always'])
    bot.start()

