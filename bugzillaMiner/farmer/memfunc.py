'''
Created on 2013-5-3

@author: Simon@itechs
'''
mf_edays = [["Short", 0, 1],
         ["Middle", 0, 0, 0, 1, 50, 58],
         ["Long", 0, 0, 50, 58]
         ]

mf_comments = [["Small", 1, 2],
         ["Middle", 0, 0, 1, 2, 4, 6],
         ["Large", 0, 0, 4, 6]
         ]

mf_modis = [["Small", 1, 2],
         ["Middle", 0, 0, 1, 2, 3, 5],
         ["Large", 0, 0, 3, 5]
         ]

mf_umodis = [["Small", 0, 1],
         ["Middle", 0, 0, 0, 1, 1, 3],
         ["Large", 0, 0, 1, 3]
         ]

mf_atn = [["DontHave", 0, 1],
         ["Have", 0, 0, 1]
         ]

mf_dev = [["Small", 0, 1],
         ["Middle", 0, 0, 0, 1, 1, 3],
         ["Large", 0, 0, 1, 3]
         ]

mf_severity = [["Low", 0, 1],
         ["Normal", 0, 0, 3, 4, 4, 5],
         ["High", 0, 0, 4, 5]
         ]

mf_depend = [["DontHave", 0, 1],
         ["Have", 0, 0, 1]
         ]

mf_block = [["DontHave", 0, 1],
         ["Have", 0, 0, 1]
         ]

mf_reputation = [["Low", 25, 41],
         ["Middle", 0, 0, 25, 41, 41, 52],
         ["High", 0, 0, 41, 52]
         ]

mf_fsdays = [["BeforeOpen", 1600, 1825],
         ["DuringOpen", 0, 0, 1600, 1825, 1825, 2190],
         ["AfterOpen", 0, 0, 1825, 2190]
         ]

labels = [
          #["LS", None],
          #["Resolution", None],
          ["ElapseDays", mf_edays], 
          ["CommentNum", mf_comments],         
          ["ModiNum", mf_modis],
          ["UniModiNum", mf_umodis],
          ["Attachment", mf_atn],
          ["DevNum", mf_dev],
          ["Severity", mf_severity],
          ["Depend", mf_depend],
          ["Block", mf_block],
          ["Reputation", mf_reputation],
          ["Stage", mf_fsdays],
          ]

def getMembershipValue(value, memfunc):
    count = 1
    isFlat = True
    begin = 1
#   print value, memfunc
    while (count < len(memfunc) and value >= memfunc[count]):
        count += 1
        isFlat = not isFlat
        if (count % 2 != 0): begin = (begin + 1) % 2
    if (isFlat):
        return begin
    elif (count == len(memfunc)):
        return memfunc[-1]
    else:
        end = (begin + 1) % 2
        return float(begin) + float((end - begin) * (value - memfunc[count - 1])) / (memfunc[count] - memfunc[count - 1])
    
def getMembershipPair(label, value, memfuncs):
    result = ""
    if (memfuncs == None):
        return "<%s_%s,%.2f> " % (value, label, 1)
    value = int(value)
    for memfunc in memfuncs:
        tvalue = getMembershipValue(value, memfunc)
        if (tvalue >= 0.01):
            result += "<%s_%s,%.2f> " % (memfunc[0], label, tvalue)
    return result

def getMember(label, value, memfuncs):
    result = ""
    if (memfuncs == None):
        return "%s_%s" % (value, label)
    value = int(value)
    for memfunc in memfuncs:
        tvalue = getMembershipValue(value, memfunc)
        if (tvalue >= 1.0):
            result += "%s_%s" % (memfunc[0], label)
    return result