'''
Created on 2013-5-2

@author: Simon@itechs
'''
import memfunc

if __name__ == '__main__':
    finname = '../result/seqsample-thunderbird.txt'
    fin = open(finname, 'r')
    data = fin.read()
    fin.close()
    linecount = data.count('\n')
    fin = open(finname, 'r')
    foutname = fin.name.replace(".txt", "-fs.txt")
    fout = open(foutname, 'w')
    lcount = 0
    for line in fin:
        lcount += 1
        if (lcount % 10000 == 0): print "%d lines processed(%.1f%%, %d)" % (lcount, float(lcount)/ linecount * 100, linecount)
        tmp = line.split("\t")
        outputline = ''
        tmp = tmp[3:-1]
        for i, item in enumerate(tmp):
            outputline += memfunc.getMembershipPair(memfunc.labels[i][0], item, memfunc.labels[i][1])
        fout.write(outputline[:-1] + "\n")
    fin.close()
    fout.close()
    print "member finish"
    #schema breaker
    labeldict = {}
    indexdict = {}
    count = 1
    finname = foutname
    fin = open(finname, 'r')
    foutname = fin.name.replace(".txt", "-i.txt")
    fschemaoutname = fin.name.replace(".txt", "-i.schema")
    fout = open(foutname, 'w')
    lcount = 0
    for line in fin:
        lcount += 1
        if (lcount % 10000 == 0): print "%d lines processed(%.1f%%, %d)" % (lcount, float(lcount)/ linecount * 100, linecount)
        newline = ''
        list = []
        tokens = line[1:-2].split("> <")
        for token in tokens:
            tmp = token.split(",")
            label = tmp[0]
            value = tmp[1]
            if (not labeldict.has_key(label)):
                labeldict[label] = count
                indexdict[count] = label
                count += 1
            index = labeldict[label]
            list.append((index, "<%s,%s> " % (str(index), value)))
        list = sorted(list, key=lambda element : element[0])
        for item in list: newline += item[1]
        fout.write(newline[:-1] + "\n")
    fout.close()
    fout = open(fschemaoutname, 'w')
    for i in range(1, count):
        fout.write(indexdict[i] + "\n")
    fout.close()
    fin.close()
    print "finish"