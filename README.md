# README

## 0. Git:
  > Download repository

## 1. MongoDB:

  > Download MongoDB Commutnity Server: https://www.mongodb.com/try/download/community
  
  > To install MongoDB Commutnity Server and Robo3T, and start them, follow: https://stackoverflow.com/questions/20796714/how-do-i-start-mongo-db-from-windows
  
  > MongoDB server should be started in first console/terminal.
  
## 2. Python:

    Download and install Python > 3.6 : https://www.python.org/downloads/

    pip install speech_recognition
  
    pip install sounddevice
  
    pip install soundfile
  
    pip install re
  
    pip install json
  
    pip install pymongo
  
    pip install pipwin
  
    pipwin install pyaudio
    
## 3. Flask (python 3):

> Flask server should be started in second console/terminal.

    pip install Flask
  
    pip install flask-cors
  
    cd \dental-data-procesing\test_env
  
    set FLASK_APP = app.py
  
    set FLASK_DEBUG = 1
  
    python app.py
    
## 4. VueJS:

> NodeJS (front) should be started in third console/terminal.

> install NPM with NodeJS: https://www.npmjs.com/get-npm 

``` bash


cd \dental-data-procesing\diagram

npm run dev

# it possible that nodeJs will be asking you to install some dependecies (like 'moment' or 'axios')
# install all dependencies that are required by nodeJs
# there will be instruction, in terminal, how to do it

```

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).

## 5. Application:

> At this point you should have opened 3 terminals: MongoDB (port 27017), Flask (port 5000), Node (port 8080)

> Open browser (Chrome, Firefox, Safari, Edge, Opera, Brave or Vivaldi), go to:
    http://localhost:8080
    
> To open example person data, set "Dodaj pesel" to

87101912345

> and click "Wybierz osobę"

## 6. Additional notes:

> 6.1 Voice interface is working on default system devices (microphone and speakers), make sure that you have correct devices settings.

> 6.2 Something isn't working? Create GitHub Issue or write mail to kjsobkowiak@gmail.com
