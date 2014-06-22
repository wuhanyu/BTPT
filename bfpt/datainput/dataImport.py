import pymongo
import datetime

connection = pymongo.Connection('127.0.0.1',27017)
db = connection.bfpt_development
bugreports = db.bugreports

fp = open("input.txt","r")
lines = fp.readlines()
for line in lines:
	tmp = line.strip().split('\t')
	bt = {"bid":int(tmp[0]), "seq":tmp[1], "resolution":tmp[2], "elapsedday":int(tmp[3]),
	"commentnumber":int(tmp[4]), "modinumber":int(tmp[5]),"umodinumber":int(tmp[6]),
	"attachnumber":int(tmp[7]),"devnumber":int(tmp[8]),"severity":int(tmp[9]),
	"dependencynumber":int(tmp[10]), "blocknumber":int(tmp[11]),"reputation":int(tmp[12]),
	"fsday":int(tmp[13]),
	"created_at": datetime.datetime.utcnow()}
	print bt
	bugreports.insert(bt)