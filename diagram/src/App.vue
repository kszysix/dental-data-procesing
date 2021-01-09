<template>
  <div id="app">

    <b-tabs content-class="mt-3" class="mt-1">

      <b-tab title="Dane osobowe" active>
        <personal-form ref="personal-form" @setPerson="setPerson" @getTeeth="getTeeth"/>
      </b-tab>

      <b-tab title="Diagram zębowy">
        <dental-diagram ref="dental-diagram"/>
      </b-tab>
      
    </b-tabs> 

  </div>
</template>

<script>
import PersonalForm from './components/personalForm'
import DentalDiagram from './components/dentalDiagram'
export default {
  name: 'App',
  components: {
    PersonalForm,
    DentalDiagram
  },
  methods: {
    getTeeth(person) {
      this.$refs["dental-diagram"].showTeethData(person);
    },
    setPerson() {
      var teeth = this.$refs["dental-diagram"].saveTeeth();
      this.$refs["personal-form"].saveData(teeth);
    }
  }
}
</script>

<style src="./appStyles.css"></style>