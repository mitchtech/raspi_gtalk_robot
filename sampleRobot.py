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
# This is an sample PyGtalkRobot that serves to set the show type and status text of robot by receiving message commands.
#

import sys
import time

from PyGtalkRobot import GtalkRobot

############################################################################################################################
class GNoteBot(GtalkRobot):
    #Pattern Tips:
    # I or IGNORECASE <=> (?i)      case insensitive matching
    # L or LOCALE <=> (?L)          make \w, \W, \b, \B dependent on the current locale
    # M or MULTILINE <=> (?m)       matches every new line and not only start/end of the whole string
    # S or DOTALL <=> (?s)          '.' matches ALL chars, including newline
    # U or UNICODE <=> (?u)         Make \w, \W, \b, and \B dependent on the Unicode character properties database.
    # X or VERBOSE <=> (?x)         Ignores whitespace outside character sets

    #command_ is the command prefix, 001 is the priviledge num, setState is the method name
    def command_001_setState(self, user, message, args):
        """(available|online|on|busy|dnd|away|idle|out|off|xa)\s+(.*)$(?i)"""
        show = args[0]
        status = args[1]
        jid = user.getStripped()
        # Verify if the user is the Administrator of this bot
        if jid == 'ldmiao@gmail.com':
            print jid, " ---> ",bot.getResources(jid), bot.getShow(jid), bot.getStatus(jid)
            self.setState(show, status)
            self.replyMessage(user, "状态设置成功！")

    def command_002_justSave(self, user, message, args):
        """(.*?\n.*)(?s)(?m)"""
        #self.replyMessage(user, "\n"+message + "\n多行内容！")
        self.replyMessage(user, "\n"+args[0] + "\n多行内容！")
        self.replyMessage(user, time.strftime("%Y-%m-%d %a %H:%M:%S", time.gmtime()))
    
    def command_100_default(self, user, message, args):
        """.*?(?s)(?m)"""
        self.replyMessage(user, time.strftime("%Y-%m-%d %a %H:%M:%S", time.gmtime()))

############################################################################################################################
if __name__ == "__main__":
    bot = GNoteBot()
    #bot = GNoteBot(debug=['always'])
    bot.start("PyGtalkRobot@gmail.com", "PyGtalkRobotByLdmiao", "Simple Gtalk Robot")
