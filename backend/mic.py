#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class
import speech_recognition as sr
import pyaudio
print(sr.Microphone.list_microphone_names())
# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone(device_index=3) as source:
	print("Say something!")
	audio = r.listen(source)
	p = pyaudio.PyAudio()
	stream = p.open(rate = audio.sample_rate , channels = 1, format = p.get_format_from_width(audio.sample_width ),output=True)
	stream.write(audio.get_raw_data())
	stream.close()
	p.terminate()

	# chunk = 1024
	# # Open the sound file 
	# wf = audio.get_wav_data()#wave.open(, 'rb')

	# # Open a .Stream object to write the WAV file to
	# # 'output = True' indicates that the sound will be played rather than recorded
	# stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
	#                 channels = wf.getnchannels(),
	#                 rate = wf.getframerate(),
	#                 output = True)

	# # Read data in chunks
	# data = wf.readframes(chunk)

	# # Play the sound by writing the audio data to the stream
	# while data != '':
	#     stream.write(data)
	#     data = wf.readframes(chunk)

	# # Close and terminate the stream
	# stream.close()
	# p.terminate()
# recognize speech using Sphinx
#try:
 #   print("Sphinx thinks you said " + r.recognize_sphinx(audio))
#except sr.UnknownValueError:
 #   print("Sphinx could not understand audio")
#except sr.RequestError as e:
 #   print("Sphinx error; {0}".format(e))

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    temp = r.recognize_google(audio,language="pl-PL")
    print("Google Speech Recognition thinks you said " + temp)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

