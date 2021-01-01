#
# HOW TO START:
# https://flask.palletsprojects.com/en/1.0.x/quickstart/
#
#cd C:\aakris\repos\dental\test_env
#set FLASK_APP = hello.py
#set FLASK_DEBUG=1
#flask run
#
#
# PostgreSQL server port: 5432
#
import speech_recognition as sr
import pyaudio
# from playsound import playsound
import simpleaudio as sa
import sounddevice as sd
import soundfile as sf

import re
import json

from flask import Flask, jsonify,make_response
from flask_cors import CORS

import mysql.connector


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


	# while i < len(command) and command[i] == " ":
	# 	i = i + 1 
	# if i < len(command):
	# 	return json.dumps(repeatResponse)

	# if re.match('[1-8]', command[i]) and re.match('[0-8]', command[i+1]):
	# 	toothId = command[i]+command[i+1]
	# 	i = i + 2
	# else:
	# 	return "repeat"
	# if i < len(command):
	# 	return json.dumps(repeatResponse)
	# while i < len(command) and command[i] == " ":
	# 	i = i + 1 
	# if i < len(command):
	# 	return json.dumps(repeatResponse)
	# if re.match('[a-fA-F]', command[i]):
	# 	toothPart = str(command[i]).upper()
	# 	i = i + 1
	# else:
	# 	return "repeat"
	# if i < len(command):
	# 	return json.dumps(repeatResponse)	
	# while command[i] == " ":
	# 	i = i + 1
	# if i < len(command):
	# 	return json.dumps(repeatResponse)

	# toothAilment = ""
	# while i < len(command) and re.match('[a-zA-Z,ó,ż,ź,ę,ą,ł,ń,ś]', command[i]):
	# 	toothAilment = toothAilment + command[i]
	# 	i = i + 1 
	# if toothAilment == "":
	# 	return "repeat"


	# response = {
	# 	'command':command,
	# 	'toothId':toothId,
	# 	'toothPart':toothPart,
	# 	'toothAilment':toothAilment,
	# 	'next':1
	# }
	# return json.dumps(response)


@app.route('/connectToDatabase', methods=['GET'])
def connectToDatabase():
	mydb = mysql.connector.connect(
	host="127.0.0.1",
	user="root",
	password="admin",
	database="dental"
	)
	print(mydb)
	app.logger.info("Connected to database Dental.")
	return {"log":"Connected to database Dental."}


@app.route('/createTable', methods=['POST'])
def createTable():
	
	mycursor = mydb.cursor()
	mycursor.execute("CREATE DATABASE test")




@app.route('/addElement', methods=['GET'])
def addElement():
	
	mycursor = mydb.cursor()
	mycursor.execute("CREATE DATABASE test")

