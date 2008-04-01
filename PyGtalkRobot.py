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

import sys
import xmpp
import urllib
import re
import inspect

"""A simple jabber/xmpp bot framework

This is a simple jabber/xmpp bot framework using Regular Expression Pattern as command controller.
Copyright (c) 2008 Demiao Lin <ldmiao@gmail.com>

To use, subclass the "GtalkRobot" class and implement "command_NUM_" methods 
(or whatever you set the command_prefix to), like sampleRobot.py.

"""

class GtalkRobot:

    ########################################################################################################################
    conn = None
    show = None
    status = None
    commands = None
    command_prefix = 'command_'

    ########################################################################################################################
    def command_999_default(self, user, message, args):
        """.*?"""
        self.replyMessage(user, message)

    ########################################################################################################################
    #show : xa,away---away   dnd---busy   available--online
    def setState(self, show, status_text):
        if self.conn:
            if show:
                show = lower(show)
            if show == "online" or show == "on" or show == "available":
                show = "available"
            elif show == "busy" or show == "dnd":
                show = "dnd"
            elif show == "away" or show == "idle" or show == "off" or show == "out" or show == "xa":
                show = "xa"
            else:
                show = "available"
            self.show = show

            if status_text:
                self.status = status_text
            
            pres=xmpp.Presence(priority=5, show=self.show, status=self.status)
            self.conn.send(pres)
        else:
            print "Connection lost!"
    
    def replyMessage(self, user, message):
        self.conn.send(xmpp.Message(user, message))
    
    def getRoster(self):
        return self.conn.getRoster()
    
    def getResources(self, jid):
        roster = self.getRoster()
        if roster:
            return roster.getResources(jid)
            
    def getShow(self, jid):
        roster = self.getRoster()
        if roster:
            return roster.getShow(jid)

    def getStatus(self, jid):
        roster = self.getRoster()
        if roster:
            return roster.getStatus(jid)

    ########################################################################################################################
    def initCommands(self):
        if self.commands:
            self.commands.clear()
        else:
            self.commands = list()
        for (name, value) in inspect.getmembers(self):
            if inspect.ismethod(value) and name.startswith(self.command_prefix):
                self.commands.append((value.__doc__, value))
        #print self.commands
        
    def controller(self, conn, message):
        text = message.getBody()
        user = message.getFrom()
        if not self.commands:
            self.initCommands()
        for (pattern, bounded_method) in self.commands:
            match_obj = re.match(pattern, text)
            if(match_obj):
                bounded_method(user, text, match_obj.groups())
                break

    def StepOn(self):
        global roster
        try:
            self.conn.Process(1)
        except KeyboardInterrupt: return 0
        return 1

    def GoOn(self):
        while self.StepOn(): pass

    ########################################################################################################################
    def start(self, gmail_account, password, status_text="Available"):
        jid=xmpp.JID(gmail_account)
        user, server, password = jid.getNode(), jid.getDomain(), password

        self.conn=xmpp.Client(server, debug=[])
        #talk.google.com
        conres=self.conn.connect( server=("gmail.com",5223) )
        if not conres:
            print "Unable to connect to server %s!"%server
            sys.exit(1)
        if conres<>'tls':
            print "Warning: unable to estabilish secure connection - TLS failed!"
        
        authres=self.conn.auth(user, password)
        if not authres:
            print "Unable to authorize on %s - check login/password."%server
            sys.exit(1)
        if authres<>"sasl":
            print "Warning: unable to perform SASL auth os %s. Old authentication method used!"%server
        
        self.conn.RegisterHandler("message", self.controller)
        self.conn.sendInitPresence()
        
        self.setState(None, status_text)
        
        print "Bot started."
        self.GoOn()
    ########################################################################################################################

############################################################################################################################
if __name__ == "__main__":
    bot = GtalkRobot()
    bot.start("account_name@gmail.com", "xxxxxxxxxxxxx", "Simple Gtalk Robot")
