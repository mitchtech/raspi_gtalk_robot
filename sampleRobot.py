#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import time
from PyGtalkRobot import GtalkRobot

############################################################################################################################
class GNoteBot(GtalkRobot):
    def command_01_setState(self, user, message, args):
        """(available|online|on|busy|dnd|away|idle|out|xa)\s*?(.*)$"""
        show = args[0]
        status = args[1]
        jid = user.getStripped()
        print jid, " ---> ",bot.getResources(jid), bot.getShow(jid), bot.getStatus(jid)
        self.setState(show, status)
        bot.replyMessage(user, "状态设置成功！")

    def command_02_justSave(self, user, message, args):
        """.*?\n.*"""
        self.replyMessage(user, "已保存！")
        self.replyMessage(user, time.strftime("%Y-%m-%d %a %H:%M:%S", time.gmtime()))
    
    def command_98_default(self, user, message, args):
        """.*?"""
        self.replyMessage(user, time.strftime("%Y-%m-%d %a %H:%M:%S", time.gmtime()))

############################################################################################################################
if __name__ == "__main__":
    bot = GNoteBot()
    bot.start("account_name@gmail.com", "xxxxxxxxxxxxx", "Simple Gtalk Robot")