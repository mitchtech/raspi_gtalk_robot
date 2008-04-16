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
        
    def editChat(self, email, msgkey, message):
        return self.sendRequest('http://localhost:8080/chat/edit/', {'email': email, 'msgkey': msgkey, 'message': message, } )
        
        
if __name__ == '__main__':
    print AIAssistantWeb().editChat("anonymous@gmail.com", 'agthaWFzc2lzdGFudHIOCxIHTWVzc2FnZRiEAQw', "java 12345678")
