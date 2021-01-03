<template>
  <div id="app">

    <b-tabs content-class="mt-3">

      <b-tab title="Dane osobowe" active>
        
        <div class="col sm">
          <label for="person-pesel">Podaj pesel:</label>
          <b-form-input id="person-pesel" ref="person-pesel" v-model="personPesel" type="text" :state="personPeselState"></b-form-input>
        </div>
        <div>
          <b-button v-on:click="showPersonData()">Wybierz osobę</b-button>
          <p id="notExists" v-if="notExists">Nie ma takiego PESELu w bazie.</p>
        </div>

        <personal-form ref="personal-form"/>

        <div>
          <p id="saveState" v-if="cannotSaveState">Nie zapisano danych - dane niekompletne.</p>
          <p id="saveState" v-if="confirmSaveState">Zapisano dane do bazy.</p>
          <b-button v-on:click="savePersonData()">Zapisz dane</b-button>
        </div> 
      </b-tab>

      <b-tab title="Diagram zębowy">
        <div>
          <div class="row mt-5 text-center tooth-row">

            <tooth id='tooth-18' ref="tooth-18" shape='square'/>
            <tooth id='tooth-17' ref="tooth-17" shape='square'/>
            <tooth id='tooth-16' ref="tooth-16" shape='square'/>
            <tooth id='tooth-15' ref="tooth-15" shape='square'/>
            <tooth id='tooth-14' ref="tooth-14" shape='square'/>
            <tooth id='tooth-13' ref="tooth-13" shape='rectangle'/>
            <tooth id='tooth-12' ref="tooth-12" shape='rectangle'/>
            <tooth id='tooth-11' ref="tooth-11" shape='rectangle'/>

            <tooth id='tooth-21' ref="tooth-21" shape='rectangle'/>
            <tooth id='tooth-22' ref="tooth-22" shape='rectangle'/>
            <tooth id='tooth-23' ref="tooth-23" shape='rectangle'/>
            <tooth id='tooth-24' ref="tooth-24" shape='square'/>
            <tooth id='tooth-25' ref="tooth-25" shape='square'/>
            <tooth id='tooth-26' ref="tooth-26" shape='square'/>
            <tooth id='tooth-27' ref="tooth-27" shape='square'/>
            <tooth id='tooth-28' ref="tooth-28" shape='square'/>

          </div>
          <div class="row mt-3 text-center tooth-row">

            <tooth id='tooth-48' ref="tooth-48" shape='square'/>
            <tooth id='tooth-47' ref="tooth-47" shape='square'/>
            <tooth id='tooth-46' ref="tooth-46" shape='square'/>
            <tooth id='tooth-45' ref="tooth-45" shape='square'/>
            <tooth id='tooth-44' ref="tooth-44" shape='square'/>
            <tooth id='tooth-43' ref="tooth-43" shape='rectangle'/>
            <tooth id='tooth-42' ref="tooth-42" shape='rectangle'/>
            <tooth id='tooth-41' ref="tooth-41" shape='rectangle'/>

            <tooth id='tooth-31' ref="tooth-31" shape='rectangle'/>
            <tooth id='tooth-32' ref="tooth-32" shape='rectangle'/>
            <tooth id='tooth-33' ref="tooth-33" shape='rectangle'/>
            <tooth id='tooth-34' ref="tooth-34" shape='square'/>
            <tooth id='tooth-35' ref="tooth-35" shape='square'/>
            <tooth id='tooth-36' ref="tooth-36" shape='square'/>
            <tooth id='tooth-37' ref="tooth-37" shape='square'/>
            <tooth id='tooth-38' ref="tooth-38" shape='square'/>

          </div>
        </div>
		
		<div>
			<b-button v-on:click="mic()">Say command!</b-button>
		</div>
		
      </b-tab>
      
    </b-tabs> 

  </div>
</template>

<script>
import Tooth from './components/tooth';
import PersonalForm from './components/personalForm'
export default {
  name: 'App',

  data() {
    return {
      personPesel: null,
      notExists: false,
      cannotSaveState: false,
      confirmSaveState: false
    }
  },
  computed:{
    personPeselState(){
      if(this.personPesel){
          return this.personPesel.length == 11 ? true : false;
      }else{
          return null;
      }
    }
  },

  methods: {
    savePersonData(){
      var person = {};
      var personalDetails = this.$refs["personal-form"].savePersonalDetails();
      if(personalDetails == null){
        this.cannotSaveState = true;
        this.confirmSaveState = false;
        return;
      }else{
        this.cannotSaveState = false;
        this.confirmSaveState = true;
      }
      var contactDetails = this.$refs["personal-form"].saveContactDetails();
      person.personalDetails = personalDetails;
      person.contactDetails = contactDetails;

      var permanentTeeth = {}
      for(var i = 1;i<5;i++){
        for(var j = 1;j<9;j++){
          var id = i.toString()+j.toString();
          var ref = "tooth-" + id;
          permanentTeeth[id] = this.$refs[ref].saveTooth();

        }
      }
      person.permanentTeeth = permanentTeeth;

      var primaryTeeth = {};
      person.primaryTeeth = primaryTeeth;

      var request = new XMLHttpRequest();
      request.open('POST', 'http://127.0.0.1:5000/savePersonData', false);
      request.send(JSON.stringify(person));

      var confirmation = request.response;
    },

    showPersonData(){
      this.cannotSaveState = false;
      this.confirmSaveState = false;
      if(this.personPeselState){
        var request = new XMLHttpRequest();
        request.open('POST', 'http://127.0.0.1:5000/getPersonData', false);
        request.send(this.personPesel);
        if(request.response == "0"){
          console.log("Pesel: "+this.personPesel+" does not exist in mongoDatabase.")
          this.notExists = true;
          return;
        }else{
          this.notExists = false;
        }
        var person = JSON.parse(request.response);

        this.$refs["personal-form"].showPersonData(request.response)
        // zęby stałe
        var i = 1;
        var teeth = person.permanentTeeth;
        for(;i<5;i++){
          var j = 1;
          for(;j<9;j++){
            var id = i.toString()+j.toString();
            var ref = "tooth-" + id;
            this.$refs[ref].setColor('A', teeth[id]['A']);
            this.$refs[ref].setColor('B', teeth[id]['B']);
            this.$refs[ref].setColor('C', teeth[id]['C']);
            this.$refs[ref].setColor('D', teeth[id]['D']);
            this.$refs[ref].setColor('E', teeth[id]['E']);
          }
        }

        // TODO : zęby mleczne
      }
    },

    getMicCommand(){
      var request = new XMLHttpRequest();
      request.open('GET', 'http://127.0.0.1:5000/mic', false);
      request.send();
      return JSON.parse(request.response);
    },

    useCommand(obj){
      var ref = "tooth-" + obj.toothId;
      this.$refs[ref].setColor(obj.toothPart, obj.toothAilment);
    },

  	mic() {
  		var obj = this.getMicCommand();
      if(obj.next == 0){
        return;
      }else if (obj.next == 1){
        console.log("id: " + obj.toothId+"  part: "+obj.toothPart+"  ailment: "+obj.toothAilment);
        this.useCommand(obj);
      }else if (obj.next == 2){
        console.log("Please, repeat command:")
      }
      while(obj.next == 1 || obj.next == 2){
        obj = this.getMicCommand();
        if(obj.next == 0){
          return;
        }else if (obj.next == 1){
          console.log("id: " + obj.toothId+"  part: "+obj.toothPart+"  ailment: "+obj.toothAilment);
          this.useCommand(obj);
        }else if (obj.next == 2){
          console.log("Please, repeat command:");
        }
      }
  	}
  },

  components: {
    PersonalForm,
    Tooth
  }
}
</script>

<style src="./appStyles.css"></style>