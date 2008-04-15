#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib

class AIAssistantWeb:
    def sendRequest(self, url, data):
        params = urllib.urlencode(data)
        nf = urllib.urlopen(url, data=params, proxies=None)
        if nf:
            #f = open("chat.html", 'w')
            #f.write(nf.read())
            #f.close()
            return True
        return False

    def addChat(self, email, message):
        return self.sendRequest('http://aiassistant.appspot.com/chat/add/', {'email': email, 'message': message, } )
