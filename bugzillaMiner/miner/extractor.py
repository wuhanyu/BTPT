#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Created on 2013-3-12

@author: Simon
'''

import commonFunc
import gl
from dateutil.parser import parse
from dateutil.relativedelta import *
from dataobject import *

#class SequenceExtractor(object):
#    IS_FINAL_OUTPUT = False
#    def __init__(self):
#        pass
#    
#    def getSequence(self, modifications):
#        line = ''
#        status = None
#        for modi in modifications:
#            if (cmp(modi.content, "Status") == 0):
#                if (not status):
#                    line += "NEW"
#                    status = "NEW"
#                if (status and cmp(modi.remove, status) == 0):
#                    line += '-' + modi.add
#                else:
#                    line += '-' + modi.remove + '-' + modi.add
#                status = modi.add
#        flag = True
#        for modi in reversed(modifications):
#            if (cmp(modi.content, "Resolution") == 0):
#                if (modi.add):
#                    line += ":" + modi.add
#                else:
#                    line += ":None"
#                flag = False
#                break
#        if (flag): line += ':None'
#        return line
#    
#    def getCountBeforeTime(self, list, time, isUnique=False):
#        count = 0
#        if (not isUnique):
#            for item in list:
#                if (item.time < time): count += 1
#                else: break
#        else:
#            timeindex = list[0].time
#            count = 1
#            for item in list:
#                if (item.time < time):
#                    if (item.time > timeindex):
#                        count += 1
#                        timeindex = item.time
#                else:
#                    break
#        return count
#    
#    def processFile(self, dom, hdom, output=None):
#        reportStartTime = commonFunc.getReportStartTime(dom)
#    #    print reportStartTime
#        comments = commonFunc.getComments(dom)
#        title = commonFunc.getTitle(dom).split(u' – ')[0][4:]
#        
#        #==================history==================
#        modifications = commonFunc.getModifications(hdom)
#        
#        line = self.getSequence(modifications)
#        if (len(line) > 0):
#            reportStartTime = commonFunc.getReportStartTime(dom)
#            start_time = parse(reportStartTime)
#            end_time = None
#            for modi in reversed(modifications):
#                if (cmp(modi.content, "Status") == 0):
#                    end_time = modi.time
#                    break
#            if (not end_time): return
#            elapsed_days = (end_time - start_time).days
#            elapsed_comments = self.getCountBeforeTime(comments, end_time)
#            elapsed_modifications = self.getCountBeforeTime(modifications, end_time)
#            elapsed_unique_modifications = self.getCountBeforeTime(modifications, end_time, True)
#            line += '\t' + str(elapsed_days) + '\t' + str(elapsed_comments)
#            line += '\t' + str(elapsed_modifications)
#            line += '\t' + str(elapsed_unique_modifications)
#        if (gl.DEBUG): print line
#        if (output):
#            output.writelines([title + '\t' + line + '\n'])
#        pass
#    
#    def __str__(self):
#        result = ''
#        return result
#    
#    def outputCount(self, filepath):
#        file_object = open(filepath, 'w')    
#        file_object.close()
#        return

class TransitionExtractor(object):
    IS_FINAL_OUTPUT = False
    def __init__(self):
        pass
    
    def getFromStarttimeDays(self, starttime):
        return (starttime - gl.startTime).days + 1
    
    def processFile(self, dom, hdom, output=None):
        reportStartTime = commonFunc.getReportStartTime(dom)
        if (gl.startTime == None): gl.startTime = parse(reportStartTime)
    #    print reportStartTime
        comments = commonFunc.getComments(dom)
        title = commonFunc.getTitle(dom).split(u' – ')[0][4:]

        #==================history==================
        modifications = commonFunc.getModifications(hdom)
        c_index = 0
        time = parse(reportStartTime)
        m_index = 0
        count = 1
        md_index = 0
        dcount = 1
        if (len(modifications) <= 0): return
        dtime = modifications[0].time
        tmplines = []
        
        for modi in modifications:
            if (modi.time > dtime):
                dcount += 1
                dtime = modi.time
            if (cmp(modi.content, "Status") == 0):
                line = ''
                resolution = 'NONE'
                p = count - 1
                while (p >= 0 and modifications[p].time == modi.time):
                    if (cmp(modifications[p].content, "Resolution") == 0 and modifications[p].add):
                        resolution = modifications[p].add
                    p -= 1
                p = count + 1
                while (p < len(modifications) and modifications[p].time == modi.time):
                    if (cmp(modifications[p].content, "Resolution") == 0 and modifications[p].add):
                        resolution = modifications[p].add
                    p += 1
                
#                line += modi.remove + '-' + modi.add + ':' + resolution + '\t'
                line += modi.remove + '-' + modi.add + '\t'
                p = c_index 
                while (len(comments) > 0 and comments[p].time <= modi.time and p < len(comments) - 1):
                    p += 1
                line += str(p - c_index + 1) + '\t'
                c_index = p
                line += str((modi.time - time).days) + '\t'
                time = modi.time
                line += str(count - m_index - 1) + '\t'
                m_index = count
                line += str(dcount - md_index - 1) + '\t'
                md_index = dcount
                dtime = modi.time
                fsdays = self.getFromStarttimeDays(dtime)
                line += str(fsdays) + '\t'
                if (gl.DEBUG): print line
                tmplines.append(title + '\t' + line + '\n')
            count += 1
        if (output):
            output.writelines(tmplines)
        pass
    
    def __str__(self):
        result = ''
        return result
    
    def outputCount(self, filepath):
        file_object = open(filepath, 'w')    
        file_object.close()
        return
    
class NewSequenceExtractor(object):
    IS_FINAL_OUTPUT = False
    def __init__(self):
        pass
    
    def getSequence(self, modifications):
        line = ''
        status = None
        for modi in modifications:
            if (cmp(modi.content, "Status") == 0):
                if (not status):
                    line += "NEW"
                    status = "NEW"
                if (status and cmp(modi.remove, status) == 0):
                    line += '-' + modi.add
                else:
                    line += '-' + modi.remove + '-' + modi.add
                status = modi.add
        flag = True
        for modi in reversed(modifications):
            if (cmp(modi.content, "Resolution") == 0):
                if (modi.add):
                    resolution = modi.add
                else:
                    resolution = "NONE"
                flag = False
                break
        if (flag): resolution = 'NONE'
        return line,resolution
    
    def getCountBeforeTime(self, list, time, isUnique=False):
        count = 0
        if (not isUnique):
            for item in list:
                if (item.time < time): count += 1
                else: break
        else:
            timeindex = list[0].time
            count = 1
            for item in list:
                if (item.time < time):
                    if (item.time > timeindex):
                        count += 1
                        timeindex = item.time
                else:
                    break
        return count
    
    def getReputation(self, reporter, resolution):
        if (not gl.reporterDict.has_key(reporter)): gl.reporterDict[reporter] = 0
        if (not gl.reporterFixDict.has_key(reporter)): gl.reporterFixDict[reporter] = 0
        gl.reporterDict[reporter] += 1
        if (cmp(resolution, "FIXED") == 0): gl.reporterFixDict[reporter] += 1
        return float(gl.reporterFixDict[reporter]) / (gl.reporterDict[reporter] + 1)
    
    def getFromStarttimeDays(self, starttime):
        starttime = parse(starttime)
        return (starttime - gl.startTime).days + 1
    
    def processFile(self, dom, hdom, output=None):
        reportStartTime = commonFunc.getReportStartTime(dom)
        if (gl.startTime == None): gl.startTime = parse(reportStartTime)
    #    print reportStartTime
        comments = commonFunc.getComments(dom)
        title = commonFunc.getTitle(dom).split(u' – ')[0][4:]
        
        #==================history==================
        modifications = commonFunc.getModifications(hdom)
        seq, resolution = self.getSequence(modifications)
        attachnumber = commonFunc.getAttachsNumber(dom)
        developernumber = commonFunc.getCCNumber(dom)
        dependencynumber = commonFunc.getDependencyNum(dom)
        blocknumber = commonFunc.getBlockNum(dom)
        reporter = commonFunc.getReporter(dom)
        reputation = self.getReputation(reporter, resolution)
        severity = commonFunc.getBugSeverity(dom)
        fsdays = self.getFromStarttimeDays(reportStartTime)
        product = commonFunc.getProduct(dom)
        line = seq + '\t' + resolution
        if (len(line) > 0):
            reportStartTime = commonFunc.getReportStartTime(dom)
            start_time = parse(reportStartTime)
            end_time = None
            for modi in reversed(modifications):
                if (cmp(modi.content, "Status") == 0):
                    end_time = modi.time
                    break
            if (not end_time): return
            elapsed_days = (end_time - start_time).days
            elapsed_comments = self.getCountBeforeTime(comments, end_time)
            elapsed_modifications = self.getCountBeforeTime(modifications, end_time)
            elapsed_unique_modifications = self.getCountBeforeTime(modifications, end_time, True)
            line += '\t' + str(elapsed_days) + '\t' + str(elapsed_comments)
            line += '\t' + str(elapsed_modifications)
            line += '\t' + str(elapsed_unique_modifications)
            line += '\t' + str(attachnumber)
            line += '\t' + str(developernumber)
            line += '\t' + str(severity)
            line += '\t' + str(dependencynumber)
            line += '\t' + str(blocknumber)
            line += '\t' + ("%d" % int(reputation * 100))
            line += '\t' + str(fsdays)
            line += '\t' + product
        if (gl.DEBUG): print line
        if (output):
            output.writelines([title + '\t' + line + '\n'])
        pass
    
    def __str__(self):
        result = ''
        return result
    
    def outputCount(self, filepath):
        file_object = open(filepath, 'w')    
        file_object.close()
        return

class Sample(object):
    def __init__(self):
        pass
    
    def processFile(self, dom, hdom):
        pass
    
    def __str__(self):
        result = ''
        return result
    
    def outputCount(self, filepath):
        file_object = open(filepath, 'w')    
        file_object.close()
        return