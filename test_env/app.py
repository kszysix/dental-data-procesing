#
# HOW TO START:
# https://flask.palletsprojects.com/en/1.0.x/quickstart/
#
# cd C:\aakris\repos\dental\test_env
# set FLASK_APP = hello.py
# set FLASK_DEBUG=1
# flask run
#
#
# PostgreSQL server port: 5432
#
import speech_recognition as sr
import pyaudio
import sounddevice as sd
import soundfile as sf

import re
import json

import pymongo

from bson.json_util import dumps, loads 

from flask import Flask, jsonify,make_response
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 	@ - in progress
#	TODO:
#
#	0. PRACA PISEMNA
#
#	1. Osobna funkcja do łączenia z mongo + walidacja jeśli coś nie istnieje?
# @ 2. Zapis przez mikrofon w czasie rzeczywistym 
#	3. Zęby mleczne
#	4. Opis numeryczny zębów - front
#	5. Legenda chorób - front
#	6. XMLHttp - deprecated - backend
#	7. README.md - jak uruchomić aplikację - github
#	8. Przenoszenie bazy mongo
#	9. Walidacja połączenia z Flask'iem - front
#	10. Dodawanie komend przez usera
#	11. Nazewnictwo powierzchni zęba?
#	12. 

#	device_index=3

@app.route('/mic', methods=['GET'])
def mic():
	r = sr.Recognizer()
	with sr.Microphone(device_index=3) as source:
		print("Say something!")
		filename = 'startMic.wav'
		data, fs = sf.read(filename, dtype='float32')  
		sd.play(data, fs)

		audio = r.listen(source)

		filename = 'endMic.wav'
		data, fs = sf.read(filename, dtype='float32')  
		sd.play(data, fs)

	response = {
		'command': 'Problem with Speech Recognition.',
		'toothId':0,
		'toothPart':0,
		'toothDesease':0,
		'next':2
	}

	try:
		command = r.recognize_google(audio,language="pl-PL")
		print("Speech Recognition thinks you said " + command)
		response = createCommandJson(command)
	except sr.UnknownValueError:
	    print("Speech Recognition could not understand audio")
	    response = json.dumps(response)
	except sr.RequestError as e:
	    print("Could not request results from Speech Recognition service; {0}".format(e))
	    response = json.dumps(response)
	

	response = json.loads(response)
	if(response["next"] == 2):
		filename = 'repeat.wav'
		data, fs = sf.read(filename, dtype='float32')  
		sd.play(data, fs)
		status = sd.wait()

	return response


def createCommandJson(command):
	response = {
		'command': command,
		'toothId':0,
		'toothPart':0,
		'toothDesease':0,
		'next':2
	}
	if(command == "stop" or command == "100"):
		response["next"] = 0
		return json.dumps(response)

	i = 0
	toothId = ""
	toothPart = ""
	toothDesease = ""

	while i < len(command):
		if(command[i] == " "):
			i = i + 1 
			continue
		elif(len(toothId)<2 and re.match('[1-8]', command[i])):
			toothId = toothId + command[i]
		elif(len(toothPart) == 0 and re.match('[a-zA-Z,ó,ż,ź,ę,ą,ł,ń,ś]', command[i])):
			while i < len(command) and command[i] != " ":
				toothPart = toothPart + command[i]
				i = i + 1

		elif(re.match('[a-zA-Z,ó,ż,ź,ę,ą,ł,ń,ś]', command[i])):
			toothDesease = toothDesease + command[i]
		i = i + 1 

	print(toothPart)
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
	dblist = myclient.list_database_names()
	mydb = myclient["mydatabase"]
	mycol = mydb["parameters"]

	# Tooth parts
	myquery = { "name": "toothParts" }
	exist = mycol.find(myquery).count() > 0
	if(exist):
		cursor = mycol.find(myquery)
		list_cur = list(cursor)
		a = dumps(list_cur, indent = 2) 
		b = json.loads(str(a))
		partExists = False
		for item in b[0]["parts"]:
			if(item["translation"] == toothPart):
				toothPart = item["part"]
				partExists = True
		if(not partExists):
			toothPart = ""
	else:
		print("Error: can't find parameter in mongo database")
		toothPart = ""

	# Tooth desease
	myquery = { "name": "deseases" }
	exist = mycol.find(myquery).count() > 0
	if(exist):
		cursor = mycol.find(myquery)
		list_cur = list(cursor)
		a = dumps(list_cur, indent = 2) 
		b = json.loads(str(a))
		deseaseExists = False
		for item in b[0]["deseases"]:

			if(item["translation"] == toothDesease):
				toothDesease = item["desease"]
				deseaseExists = True
		if(not deseaseExists):
			toothDesease = ""
	else:
		print("Error: can't find parameter in mongo database")
		toothDesease = ""


	if (len(toothId) == 2 and
		len(toothPart) > 0 and
		len(toothDesease) > 4):
		response["next"] = 1
		response["command"] = command
		response["toothId"] = toothId
		response["toothPart"] = toothPart
		response["toothDesease"] = toothDesease
		return json.dumps(response)
	else:
		response["next"] = 2
		return json.dumps(response)


@app.route('/getPersonData', methods=['POST'])
def getPersonData():
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
	dblist = myclient.list_database_names()
	mydb = myclient["mydatabase"]
	mycol = mydb["customers"]
	pesel = str(request.data.decode('UTF-8'))
	myquery = { "personalDetails.pesel": pesel }
	exist = mycol.find(myquery).count() > 0
	if(exist):
		cursor = mycol.find(myquery)
		list_cur = list(cursor)
		a = dumps(list_cur, indent = 2) 
		b = json.loads(str(a))
		return b[0]
	else:
		return "0"


@app.route('/savePersonData', methods=['POST'])
def getSaveData():
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
	mydb = myclient["mydatabase"]
	mycol = mydb["customers"]

	person = request.data.decode('UTF-8')
	person = json.loads(person)

	myquery = { "personalDetails.pesel": person["personalDetails"]["pesel"] }
	cursor = mycol.find(myquery)
	duplicated = (mycol.find(myquery).count()) > 0

	if(duplicated):
		mycol.update_one(myquery, {"$set": person}, upsert=False)
	else:
		mycol.insert_one(person)
	

	return "conf"