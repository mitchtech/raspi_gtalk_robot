#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import time
from PyGtalkRobot import GtalkRobot

############################################################################################################################
class GNoteBot(GtalkRobot):
    def command_01_setState(self, user, message):
        """available|online|on|busy|dnd|away|idle|out|xa"""
        jid = user.getStripped()
        print jid, " ---> ",bot.getResources(jid), bot.getShow(jid), bot.getStatus(jid)
        bot.replyMessage(user, "状态设置成功！")
        self.setState(message, None)

    def command_02_saveInHistory(self, user, message):
        """.*?\n.*"""
        self.replyMessage(user, "已保存！")
        self.replyMessage(user, time.strftime("%Y-%m-%d %a %H:%M:%S", time.gmtime()))
    
    
    
    def command_99_default(self, user, message):
        """.*?"""
        self.replyMessage(user, time.strftime("%Y-%m-%d %a %H:%M:%S", time.gmtime()))

############################################################################################################################
if __name__ == "__main__":
    bot = GNoteBot()
    bot.start("account_name@gmail.com", "xxxxxxxxxxxxx", "Simple Gtalk Robot")