'''
Created on 2013-3-12

@author: Simon
'''
error_count = 0
error_list = []
filecount = 1
TASK_TYPE = "NewSequenceExctractor"
#    if (cmp(TASK_TYPE, "TimeStatistic")==0):
#        processor = statistician.TimeStatistician()
#    elif (cmp(TASK_TYPE, "SequenceStatistic")==0):
#        processor = statistician.SequenceStatistician()
#    elif (cmp(TASK_TYPE, "SequenceExctractor")==0):
#        processor = extractor.SequenceExtractor()
#    elif (cmp(TASK_TYPE, "TransitionExctractor")==0):
index = 0
DEBUG = False
startTime = None
BUG_SERVERITY = {"blocker":7, "critical":6, "major":5, "normal":4, "minor":3, "trivial":2, "enhancement":1}
reporterDict = {}
reporterFixDict = {}