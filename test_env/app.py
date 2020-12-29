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
from flask import Flask, jsonify,make_response
from flask_cors import CORS
import mysql.connector
app = Flask(__name__)
CORS(app)

# mySQL:



@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello')
def hello():
    return 'Hello, Hello'

@app.route('/first', methods=['GET'])
def example():
	
	response = {'id':1,'title':'example'}
	app.logger.debug("main debug")
	app.logger.info("main info")
	app.logger.warning("main warning")
	app.logger.error("main error")
	app.logger.critical("main critical")
	return response

@app.route('/mic', methods=['GET'])
def mic():
	response = {'id':0,'result':'nope'}
	r = sr.Recognizer()
	with sr.Microphone(device_index=3) as source:
		print("Say something!")
		audio = r.listen(source)
		p = pyaudio.PyAudio()
		stream = p.open(rate = audio.sample_rate , channels = 1, format = p.get_format_from_width(audio.sample_width ),output=True)
		stream.write(audio.get_raw_data())
		stream.close()
		p.terminate()
	try:
	# for testing purposes, we're just using the default API key
	# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
	# instead of `r.recognize_google(audio)`
		result = r.recognize_google(audio,language="pl-PL")
		if(result == "stop"):
			response = {'id':1,'result':result,'next':0}
		else:
			response = {'id':1,'result':result,'next':1}
		print("Google Speech Recognition thinks you said " + result)

	except sr.UnknownValueError:
	    print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
	    print("Could not request results from Google Speech Recognition service; {0}".format(e))

	return response

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

