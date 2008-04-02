#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

section_f = """F('mod','BDUThIgoQ3P7h55Aj',1207103509297);
B('BDUThIgoQ3P7h55Aj','good',1207103422300,1207103427645,1207103708101,{},0,0,0,'',
    [
        S('SDUThIgoQ3f7h55Aj',[],'',0,1207103422307),
        S('SDQcjSgoQm6bn55Aj',
            [
                N('NDSeIIwoQ7rPk55Aj','010. Hello from GNotebook.py!','PyGtalkRobot@gmail.com',['http://code.google.com/p/pygtalkrobot/','GNotebook 010'],null,[],1207103461870,1207103461873,0),
                N('NDQGpIgoQkKHk55Aj','009. Hello from GNotebook.py!','PyGtalkRobot@gmail.com',['http://code.google.com/p/pygtalkrobot/','GNotebook 009'],null,[],1207103459472,1207103459475,0),
                N('NDRteIgoQxo3k55Aj','008. Hello from GNotebook.py!','PyGtalkRobot@gmail.com',['http://code.google.com/p/pygtalkrobot/','GNotebook 008'],null,[],1207103456966,1207103456975,0),
                N('NDQGpIgoQwvrj55Aj','007. Hello from GNotebook.py!','PyGtalkRobot@gmail.com',['http://code.google.com/p/pygtalkrobot/','GNotebook 007'],null,[],1207103454530,1207103454586,0),
                N('NDSUCIwoQ8OXj55Aj','006. Hello from GNotebook.py!','PyGtalkRobot@gmail.com',['http://code.google.com/p/pygtalkrobot/','GNotebook 006'],null,[],1207103451888,1207103451913,0),
                N('NDQ7QIgoQhdPj55Aj','005. Hello from GNotebook.py!','PyGtalkRobot@gmail.com',['http://code.google.com/p/pygtalkrobot/','GNotebook 005'],null,[],1207103449477,1207103449449,0),
                N('NDSD6IgoQyrzj55Aj','004. Hello from GNotebook.py!','PyGtalkRobot@gmail.com',['http://code.google.com/p/pygtalkrobot/','GNotebook 004'],null,[],1207103446602,1207103446604,0),
                N('NDSGpIgoQk6rj55Aj','003. Hello from GNotebook.py!','PyGtalkRobot@gmail.com',['http://code.google.com/p/pygtalkrobot/','GNotebook 003'],null,[],1207103444243,1207103444245,0),
                N('NDQqRIwoQhJjj55Aj','002. Hello from GNotebook.py!','PyGtalkRobot@gmail.com',['http://code.google.com/p/pygtalkrobot/','GNotebook 002'],null,[],1207103441924,1207103441923,0),
                N('NDQ9jIgoQ2oTj55Aj','001. Hello from GNotebook.py!','PyGtalkRobot@gmail.com',['http://code.google.com/p/pygtalkrobot/','GNotebook 001'],null,[],1207103439450,1207103439455,0)
            ],
        'section11111111111111111111',0,1207103509297)
    ],
    []
);
"""

section0 = """F('mod','BDUThIgoQ3P7h55Aj',1207103509297);"""
section1 = """B('BDUThIgoQ3P7h55Aj','good',1207103422300,1207103427645,1207103708101,{},0,0,0,'',[S('SDUThIgoQ3f7h55Aj',[],'',0,1207103422307),S('SDQcjSgoQm6bn55Aj',[N('NDSeIIwoQ7rPk55Aj','010. Hello from GNotebook.py!','PyGtalkRobot@gmail.com',['http://code.google.com/p/pygtalkrobot/','GNotebook 010'],null,[],1207103461870,1207103461873,0),N('NDQGpIgoQkKHk55Aj','009. Hello from GNotebook.py!','PyGtalkRobot@gmail.com',['http://code.google.com/p/pygtalkrobot/','GNotebook 009'],null,[],1207103459472,1207103459475,0),N('NDRteIgoQxo3k55Aj','008. Hello from GNotebook.py!','PyGtalkRobot@gmail.com',['http://code.google.com/p/pygtalkrobot/','GNotebook 008'],null,[],1207103456966,1207103456975,0),N('NDQGpIgoQwvrj55Aj','007. Hello from GNotebook.py!','PyGtalkRobot@gmail.com',['http://code.google.com/p/pygtalkrobot/','GNotebook 007'],null,[],1207103454530,1207103454586,0),N('NDSUCIwoQ8OXj55Aj','006. Hello from GNotebook.py!','PyGtalkRobot@gmail.com',['http://code.google.com/p/pygtalkrobot/','GNotebook 006'],null,[],1207103451888,1207103451913,0),N('NDQ7QIgoQhdPj55Aj','005. Hello from GNotebook.py!','PyGtalkRobot@gmail.com',['http://code.google.com/p/pygtalkrobot/','GNotebook 005'],null,[],1207103449477,1207103449449,0),N('NDSD6IgoQyrzj55Aj','004. Hello from GNotebook.py!','PyGtalkRobot@gmail.com',['http://code.google.com/p/pygtalkrobot/','GNotebook 004'],null,[],1207103446602,1207103446604,0),N('NDSGpIgoQk6rj55Aj','003. Hello from GNotebook.py!','PyGtalkRobot@gmail.com',['http://code.google.com/p/pygtalkrobot/','GNotebook 003'],null,[],1207103444243,1207103444245,0),N('NDQqRIwoQhJjj55Aj','002. Hello from GNotebook.py!','PyGtalkRobot@gmail.com',['http://code.google.com/p/pygtalkrobot/','GNotebook 002'],null,[],1207103441924,1207103441923,0),N('NDQ9jIgoQ2oTj55Aj','001. Hello from GNotebook.py!','PyGtalkRobot@gmail.com',['http://code.google.com/p/pygtalkrobot/','GNotebook 001'],null,[],1207103439450,1207103439455,0)],'section11111111111111111111',0,1207103509297)],[]);"""

class F:
    def __init__(self, mod, fid, timeint):
        self.mod, self.fid, self.timeint = mod, fid, timeint
    
    def __str__(self):
        return str((self.mod, self.fid, self.timeint))


class B:
    def __init__(self, bid, bname, timeint1, timeint2, timeint3, dict1, int1, int2, int3, str1, sectionlist, list2):
        self.bid, self.bname, self.timeint1, self.timeint2, self.timeint3, self.dict1, self.int1, self.int2, self.int3, self.str1, self.sectionlist, self.list2 = bid, bname, timeint1, timeint2, timeint3, dict1, int1, int2, int3, str1, sectionlist, list2
    
    def __str__(self):
        return str((self.bid, self.bname, self.timeint1, self.timeint2, self.timeint3, self.dict1, self.int1, self.int2, self.int3, self.str1, self.sectionlist, self.list2))

class S:
    def __init__(self, sid, notelist, sname, int1, timeint1):
        self.sid, self.notelist, self.sname, self.int1, self.timeint1 = sid, notelist, sname, int1, timeint1
    
    def __str__(self):
        return str((self.sid, self.notelist, self.sname, self.int1, self.timeint1))


class N:
    def __init__(self, nid, content, email, url_titlelist, nullvalue, list1, timeint1, timeint2, int1):
        self.nid, self.content, self.email, self.url_titlelist, self.nullvalue, self.list1, self.timeint1, self.timeint2, self.int1 = nid, content, email, url_titlelist, nullvalue, list1, timeint1, timeint2, int1
    
    def __str__(self):
        return str((self.nid, self.content, self.email, self.url_titlelist, self.nullvalue, self.list1, self.timeint1, self.timeint2, self.int1))


#print section0.replace(";","")
print eval(section0.replace(";", ""))
notebook = eval(section1.replace(";", "").replace("null", "None"))
print notebook.sectionlist
for section in notebook.sectionlist:
    print section.sname, "-----"
    for note in section.notelist:
        print note.nid, note.url_titlelist[0], note.url_titlelist[1], note.content



