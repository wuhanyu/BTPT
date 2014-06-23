'''
Created on 2013-3-8

@author: Simon@itechs
'''
from dateutil.parser import parse
import types

class Comment(object):
    '''
    Data jam for Comment Object, each is a comment posted by a DEV
    '''
    author = None
    time = None
    content = None
    def __init__(self, author, timestr, content):
        if (author):
            self.author = author
        if (timestr):
            time = parse(timestr)
            self.time = time
        if(content):
            self.content = content
        pass
    
            
    def __str__(self):
        result = str(self.author) + '\n'
        result += str(self.time) + '\n'
        result += str(self.content) + '\n'
        return result 
    
class Modification(object):
    '''
    Data jam for Modification Object, each is a modifications made by a core DEV
    '''
    author = None
    time = None
    content = None
    remove = None
    add = None
    def __init__(self, author, timestr, content, remove, add):
        if (author):
            self.author = author
        if (timestr):
            time = parse(timestr)
            self.time = time
        if (content):
            self.content = content
        if (remove):
            self.remove = remove
        if (add):
            self.add = add
        pass
    
    def __str__(self):
        result = str(self.author) + '\n'
        result += str(self.time) + '\n'
        result += str(self.content) + '\n'
        result += str(self.remove) + '\n'
        result += str(self.add) + '\n'
        return result

class Record(object):
    '''
    Data jam for an statistic record
    '''
    time = None
    recordtypeetype = None
    content = None
    def __init__(self, timestr, recordtype):
        if (timestr):
            if (type(timestr) is types.StringType):
                time = parse(timestr)
                self.time = time
            else:
                self.time = timestr
        if (recordtype):
            self.recordtype = recordtype
