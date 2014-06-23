'''
Created on 2013-5-2

@author: Simon@itechs
'''
import memfunc

if __name__ == '__main__':
    #read rule
    frule = {}
    ffrule = {}
    finname = '../result/farrule01.txt'
    fin = open(finname, 'r')
    for line in fin:
        tmp = line.split("}  ->  {")
        condition = tmp[0].split("{")[-1].split(" ")
        result = tmp[1].split("}")[0]
        print condition, result
        if (len(condition) == 1):
            frule[condition[0]] = result
        else:
            condition = sorted(condition)
            ffrule[condition[0] + '-' + condition[1]] = result
    print frule
    print ffrule
    #match
    finname = '../result/seqsample-thunderbird.txt'
    fin = open(finname, 'r')
    data = fin.read()
    fin.close()
    linecount = data.count('\n')
    fin = open(finname, 'r')
    foutname = fin.name.replace(".txt", "-ro.txt")
    fout = open(foutname, 'w')
    lcount = 0
    for line in fin:
        lcount += 1
        if (lcount % 10000 == 0): print "%d lines processed(%.1f%%, %d)" % (lcount, float(lcount)/ linecount * 100, linecount)
        tmp = line.split("\t")
        conditions = []
        tmp = tmp[3:-1]
        for i, item in enumerate(tmp):
            conditions.append(memfunc.getMember(memfunc.labels[i][0], item, memfunc.labels[i][1]))
        flag = True
        for con in conditions:
            if (frule.has_key(con)): 
                flag = False
                break
        if (flag):
            for con in conditions:
                for ccon in conditions:
                    if (ffrule.has_key(con + '-' + ccon)):
                        flag = False
                        break
                if (not flag): break
        if (flag): fout.write(line)
    fin.close()
    fout.close()
    print "member finish"