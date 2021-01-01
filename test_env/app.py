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



# mySQL:


@app.route('/mic', methods=['GET'])
def mic():
	r = sr.Recognizer()
	with sr.Microphone(device_index=3) as source:
		print("Say something!")
		# print (sd.query_devices())

		filename = 'startMic.wav'
		data, fs = sf.read(filename, dtype='float32')  
		sd.play(data, fs,device=8)

		audio = r.listen(source)

		filename = 'endMic.wav'
		data, fs = sf.read(filename, dtype='float32')  
		sd.play(data, fs,device=8)

	response = {
		'command': 'Problem with Google Speech Recognition.',
		'toothId':0,
		'toothPart':0,
		'toothAilment':0,
		'next':2
	}

	try:
		command = r.recognize_google(audio,language="pl-PL")
		print("Google Speech Recognition thinks you said " + command)
		response = createCommandJson(command)
	except sr.UnknownValueError:
	    print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
	    print("Could not request results from Google Speech Recognition service; {0}".format(e))
	
	response = json.loads(response)
	if(response["next"] == 2):
		filename = 'repeat.wav'
		data, fs = sf.read(filename, dtype='float32')  
		sd.play(data, fs,device=8)
		status = sd.wait()
	elif(response["next"] == 1):
		myclient = pymongo.MongoClient("mongodb://localhost:27017/")
		dblist = myclient.list_database_names()
		print(dblist)
		if "mydatabase" in dblist:
		 	print("The database exists.")
		else:
			mydb = myclient["mydatabase"]
			mycol = mydb["customers"]
			mydict = { "name": "John", "address": "Highway 37" }
			x = mycol.insert_one(mydict)
	return response


def createCommandJson(command):
	if(command == "stop"):
		response = {
		'command':command,
		'toothId':0,
		'toothPart':0,
		'toothAilment':0,
		'next':0
		}
		return json.dumps(response)

	i = 0
	toothId = ""
	toothPart = ""
	toothAilment = ""

	while i < len(command):
		if(command[i] == " "):
			i = i + 1 
			continue
		elif(len(toothId)<2 and re.match('[1-8]', command[i])):
			toothId = toothId + command[i]
		elif(len(toothPart)<1 and re.match('[a-fA-F]', command[i])):
			toothPart = str(command[i]).upper()
		elif(re.match('[a-zA-Z,ó,ż,ź,ę,ą,ł,ń,ś]', command[i])):
			toothAilment = toothAilment + command[i]
		i = i + 1 

	# TODO:
	# Sprawdzanie poprawności 'toothAilment' z bazą danych

	if (len(toothId) == 2 and
		len(toothPart) == 1 and
		len(toothAilment) > 4):
		response = {
			'command':command,
			'toothId':toothId,
			'toothPart':toothPart,
			'toothAilment':toothAilment,
			'next':1
		}
		return json.dumps(response)
	else:
		response = {
			'command': command,
			'toothId':0,
			'toothPart':0,
			'toothAilment':0,
			'next':2
		}
		return json.dumps(response)


@app.route('/getPersonData', methods=['POST'])
def getPersonData():
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
	dblist = myclient.list_database_names()
	mydb = myclient["mydatabase"]
	mycol = mydb["customers"]
	pesel = str(request.data.decode('UTF-8'))
	myquery = { "personalDetails.pesel": pesel }

	cursor = mycol.find(myquery)
	list_cur = list(cursor)
	a = dumps(list_cur, indent = 2) 
	b = json.loads(str(a))

	return b[0]