#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Created on 2013-3-6

@author: Simon@itechs
'''
import miner
import datetime
import gl
import commonFunc

if __name__ == '__main__':
    gl.TASK_TYPE = "NewSequenceExctractor"
    gl.DEBUG = False
    '''
    Test script for the miner
    '''
    starttime = datetime.datetime.now()
#    src = '/media/DATA/mozilla.bugs/'
#    src = 'D:\\mozilla.bugs.test\\'
    src = 'D:\\sample\\'
#    print src
    
    processor = commonFunc.getProcessorFromTaskType(gl.TASK_TYPE)
    output = commonFunc.getOutput(processor)
    commonFunc.initHeader(output, commonFunc.getHeaderFromTaskType(gl.TASK_TYPE))
    begin = 240000
    end = 252450
#    begin = 248115
#    end = begin + 1
    filecount = 0
    for i in range(begin, end):
 #        print '*' * 40
#        i = 251446
        filename = src + str(i) + '.html'
        
        if (miner.processFile(filename, processor, output)):
            filecount = filecount + 1
            print filename + '\t(' + str(filecount) + ')'
#            break
    print processor
    
    commonFunc.output(processor)
    if (output):
        output.close()
    endtime = datetime.datetime.now()
    print (endtime - starttime)
    print gl.error_count
    print gl.error_list