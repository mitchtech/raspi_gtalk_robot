#!/usr/bin/python
# -*- coding: utf-8 -*-


__version__ = "0.2"
__date__ = "2006-05-16"
__author__ = "Poly9 Group (google-notebook-api@poly9.com)"
__url__ = "http://www.poly9.com/developers/gnotebook/google-notebook-api.pys"

import random, re, socket, time, urllib, urllib2
import sys, codecs, re
from Cookie import SimpleCookie


class GLoginFailure(Exception):
    pass

class GNotebookRefreshError(Exception):
    pass

# Once again, standing on the shoulders of rancidbacon, aka follower@myrealbox.com
class CookieJar:

    def __init__(self):
        self._cookies = {}

    def extractCookies(self, response, nameFilter = None):
        for cookie in response.headers.getheaders('Set-Cookie'):
            name, value = (cookie.split("=", 1) + [""])[:2]
            if not nameFilter or name in nameFilter:
                self._cookies[name] = value.split(";")[0]


    def addCookie(self, name, value):
        self._cookies[name] = value

    def hasCookie(self, name):
        return self._cookies.has_key(name)

    def setCookies(self, request):
        request.add_header('Cookie',
                           "; ".join(["%s=%s" % (k,v)
                                     for k,v in self._cookies.items()]))

       
class GHTTPCookieProcessor(urllib2.BaseHandler):
    def __init__(self, cookieJar):
        self.cookies = cookieJar
        
    def https_response(self, request, response):
        self.cookies.extractCookies(response)
        return response

    def https_request(self, request):
        self.cookies.setCookies(request)
        return request

GHTTPCookieProcessor.http_request = GHTTPCookieProcessor.https_request
GHTTPCookieProcessor.http_response = GHTTPCookieProcessor.https_response

class GService:
    """
        An abstract class to access Google various services. Useful to handle login and subsequent cookie dance.
    """
    def __init__(self):
        self._cookies = CookieJar()
        
    def login(self, username, password, service, serviceURL):
        """
        A login method which can be used to log to Google
        """
        p = self._get_page("https://www.google.com/accounts/ServiceLoginAuth",
            post_data="continue=%s&service=%s&nui=1&Email=%s&Passwd=%s&submit=null&PersistentCookie=yes&rmShown=1" % (self._url_quote(serviceURL), service, username, password))
        p.close()
        if not self._cookies.hasCookie('LSID'):
            raise GLoginFailure, "1 Could not login to %s" % (service)
        
    def _get_page(self, url, post_data=None):
        """
        Gets the url URL with cookies enabled. Posts post_data.
        """
        f = None
        count = 1
        while count<5:
            try:
                req = urllib2.build_opener(GHTTPCookieProcessor(self._cookies))
                f = req.open(self._encode(url), data=self._encode(post_data))
                if f:
                    break
            except:
                count = count + 1
                print "waite 5 seconds for "+ str(count) +" try to get:\n  [" + url + "?"+ post_data + "]"
                time.sleep(5)

        if f and f.headers.dict.has_key('set-cookie'):
            self._cookies.extractCookies(f)

        return f


    def _url_quote(self, value): # This method is copyright (C) 2004, Adrian Holovaty
        """
        Helper method that quotes the given value for insertion into a query
        string. Also encodes into UTF-8, which Google uses, in case of
        non-ASCII characters.
        """
        value = self._encode(value)
        return urllib.quote_plus(value)

    def _encode(self, value): # This method is copyright (C) 2004, Adrian Holovaty
        """
        Helper method. Google uses UTF-8, so convert to it, in order to allow
        non-ASCII characters.
        """
        if isinstance(value, unicode):
            value = value.encode("utf-8", "ignore")
        return value

############################################################################################################################################################################################################################

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


############################################################################################################################################################################################################################


class NotebookObj:
    """
    A minimalistic notebook container.
    """
    def __init__(self, *args):
        self.key = args[0]
        self.name = args[1]
        self.entries = args[7]

class NotebookEntry:
    """
    A minimalistic notebook entry container
    """
    def __init__(self, *args):
        self.key = args[0]
        self.content = args[1]
        
# This is a wrapper function that we use to get the notebook entries
def extractEntries(*args):
    return args[3]

# Some obfuscation bindings. May not work in the future
N1 = NotebookEntry
S1 = extractEntries
B1 = NotebookObj

def chn(onestr):
    newstr = onestr
    try:
        newstr = unicode(newstr, 'utf8', 'ignore')
    except:
        pass
    return newstr.encode('gbk', 'ignore')

class GNotebook(GService):
    """
    A very simple Google Notebook API
    """
    def __init__(self, username, password):
        GService.__init__(self)
        self.token = ""
        self.notebooks = {}
        self.username = username
        self.password = password
        if self.username and self.password:
            self.login(username, password)
            

    def login(self, username, password):
        """
        Logs to Google Notebook as username, get a Notebook token and retrieves a list of notebooks
        Raises a GLoginFailure exception if the login is unsuccessful
        """
        GService.login(self, username, password, "notebook", "http://www.google.com/notebook")
        self._getToken()
        self._refreshNotebooks()
        
    def _getToken(self):
        """
        Get a notebook token. Used in every GN requests
        """
        #5083893976283701674
        p = self._get_page("http://www.google.com/notebook/token?&pv=5083893976283701674&ident=fp&tok=&cmd=")
        self.token = p.read().strip("/*").strip("*/")
        p.close()
    
    
    def _genNotebook(self, content):
        """
        
        """
        self.notebooks.clear()
        matched_objs = re.findall("""B\('(.*?)','(.*?)',[+|-]?\d+,[+|-]?\d+,[+|-]?\d+,\{.*?\},[+|-]?\d+,[+|-]?\d+,[+|-]?\d+,'.*?',""", content)
        #print matched_objs
        for matched_obj in matched_objs:
            nbid, nbname = matched_obj
            self.notebooks[nbname] = nbid
        
    def _refreshNotebooks(self):
        """
        Private method that refreshes the list of notebooks (for internal use)
        """
        url = "http://www.google.com/notebook/read?pv=5083893976283701674&ident=fp&tok=%s&cmd=u&start=0&num=20&zx=%d-1"%(self.token, int(time.time()*1000))
        #print url
        p = self._get_page(url)
        #http://www.google.com/notebook/read?pv=5083893976283701674&ident=fp&hl=zh-CN&tok=uTjoNWw0MnSxUgkFcXsp4uJufZ4%3D%3A1207056996303&cmd=u&start=0&num=20&zx=1207056991263-0
        content = p.read()
        p.close()
        
        self._genNotebook(content)
        

    def _getNotebookID(self, notebook):
        """
        Private method. Returns the internal id used by GN to identify a Notebook.
        Raises a GNotebookNotFound exception if notebook's key is not found
        """
        if not self.notebooks.has_key(notebook):
            print "Notebook '%s' not found."%notebook
            return None
        return self.notebooks[notebook]
          
    def getNotebooks(self, forceRefresh=False):
        """
        Returns a list of notebooks. Set forceRefresh to True if you want to retrieve the list from the server.
        """
        if forceRefresh:
            self._refreshNotebooks()
        return self.notebooks.keys()

    
    def _genNoteBook(self, content):
        matched_obj = re.search("""(B\(.*?\));""", content)
        notebookExpression = matched_obj.group(1)
        notebookExpression = notebookExpression.replace(";", "").replace("null", "None")
        
        notebook = eval(notebookExpression)
        return notebook
  
    def getNotebook(self, notebook):
        """
        """
        nbid = self._getNotebookID(notebook)
        if nbid:
            p = self._get_page("http://www.google.com/notebook/read?pv=5083893976283701674&ident=fp&tok=%s&cmd=b&nbid=%s&zx=%d-1"%(self.token, nbid, int(time.time()*1000)))
            content = unicode(p.read(), "utf8")
            p.close()
            notebook = self._genNoteBook(content)
            return notebook
        else:
            return None
    
    def _hasSection(self, nb, section):
        if nb:
            for s in nb.sectionlist:
                if section and section == s.sname:
                    return True
        else:
            return False
        return False
    
    def _getOrder(self, nb, section=None):
        order = nb.bid
        for s in nb.sectionlist:
            order = order + "." + s.sid
            if order.find('.X.')==-1:
                if not section or (section and section == s.sname):
                    order = order + ".X"
            for n in s.notelist:
                order = order + "." + n.nid
        #print order
        return order
        
    def _createNotebookIfNotExist(self, notebook):
        nb = self.getNotebook(notebook)
        if not nb:
            self.addNoteBook(notebook)
            nb = self.getNotebook(notebook)
        return nb
    
    def _createNotebookAndSectionIfNotExist(self, notebook, section):
        nb = self._createNotebookIfNotExist(notebook)
        
        if not self._hasSection(nb, section):
            self.addSection(notebook, section)
            nb = self.getNotebook(notebook)

        return nb
    
    def addNote(self, notebook, section, title, content, url=""):
        """
        Adds a note to section of notebook which contains 'content' and the url titled as title
        """
        nb =  self._createNotebookAndSectionIfNotExist(notebook, section)
        nbid = nb.bid
        
        order = self._getOrder(nb, section)
        
        data = "pv=5083893976283701674&ident=yj&nmeth=ctxt&client=gnotesff&tok=%s&cmd=n&nbid=%s&contents=%s&order=%s&attrt0=%s&attr0=%s"%(self.token, nbid, urllib.quote_plus(content), order, urllib.quote_plus(title), urllib.quote_plus(url))
        #data = "pv=5083893976283701674&ident=fp&nmeth=fp&tok=%s&cmd=n&nbid=%s&contents=%s&order=%s" % (self.token, nbid, content, self.entryOrder)
        #print data
        p = self._get_page("http://www.google.com/notebook/write", data)
        p.close()
        print "Note added to Section '%s' of Notebook '%s'!"%(chn(section), chn(notebook))

    def addSection(self, notebook, section_title):
        """
        Adds a section to head of the notebook whose tilte is 'title'
        """
        nb = self._createNotebookIfNotExist(notebook)
        
        order = self._getOrder(nb)
        nbid = nb.bid
        
        data = "pv=5083893976283701674&ident=fp&nmeth=fp&tok=%s&cmd=s&nbid=%s&contents=%s&order=%s"%(self.token, nbid, urllib.quote_plus(section_title), order)
        #print data
        
        p = self._get_page("http://www.google.com/notebook/write", data)
        p.close()
        print "Section '%s' added to Notebook '%s'!"%(chn(section_title), chn(notebook))
        
    def addNoteBook(self, notebook):
        """
        Adds a notebook
        """
        p = self._get_page("http://www.google.com/notebook/write", "pv=5083893976283701674&ident=fp&tok=%s&cmd=b&contents=%s"%(self.token, urllib.quote_plus(notebook)))
        p.close()
        print "Notebook '%s' added!"%chn(notebook)
        
        self._refreshNotebooks()

    def deleteNotebook(self, notebook):
        """
        Deletes a notebook
        """
        nbid = self._getNotebookID(notebook)
        p = self._get_page("http://www.google.com/notebook/write", "pv=5083893976283701674&ident=fp&nmeth=fp&tok=%s&cmd=d&nbid=%s&order=%s"%(self.token, nbid, self.token))
        p.close()


        
def urlEncode(onestr):
    return urllib.quote_plus(onestr)

if __name__ == "__main__":

    # Put your credentials here. Make sure that you are subscribed to Google Notebook
    username, password = "PyGtalkRobot@gmail.com", "PyGtalkRobotByLdmiao"
    g = GNotebook(username, password)

    
    #g.getNotebookEntries("good")
    #g.addSection("good", "section_001")
    
    i=6
    while(i<=10):
        j=1
        while(j<=5):
            g.addNote("good", "部分section___%d"%i, "笔记note_%d"%j, "%d.笔记内容_content"%j, "http://note.url")
            j = j+1
        i = i+1
        