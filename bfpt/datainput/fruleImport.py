import pymongo
import datetime

connection = pymongo.Connection('127.0.0.1',27017)
db = connection.bfpt_development
frules = db.frules

fp = open("frule.txt","r")
lines = fp.readlines()
for line in lines:
	tmp = line.strip().split('  ')
	fr = {"fid":int(tmp[0][1:-1]), "pre":tmp[1][1:-1].split(' '), "cons":tmp[3][1:-1].split(' '), "conf":float(tmp[4]),
	"created_at": datetime.datetime.utcnow()}
	print fr
	frules.insert(fr)