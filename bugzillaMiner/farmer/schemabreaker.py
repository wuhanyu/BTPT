'''
Created on 2013-5-4

@author: Simon@itechs
'''

if __name__ == '__main__':
    labeldict = {}
    indexdict = {}
    count = 1
    finname = '../result/TransitionExctractor_2013-05-02 1542-fs.txt'
    fin = open(finname, 'r')
    foutname = fin.name.replace(".txt", "-i.txt")
    fschemaoutname = fin.name.replace(".txt", "-i.schema")
    fout = open(foutname, 'w')
    for line in fin:
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