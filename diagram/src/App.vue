<template>
  <div id="app">

    <b-tabs content-class="mt-3">

      <b-tab title="Dane osobowe" active>
        <personal-form/>
      </b-tab>

      <b-tab title="Diagram zębowy">
        <div>
          <div class="row mt-5 text-center tooth-row">

            <tooth id='tooth-18' shape='square'/>
            <tooth id='tooth-17' shape='square'/>
            <tooth id='tooth-16' shape='square'/>
            <tooth id='tooth-15' shape='square'/>
            <tooth id='tooth-14' shape='square'/>
            <tooth id='tooth-13' shape='rectangle'/>
            <tooth id='tooth-12' shape='rectangle'/>
            <tooth id='tooth-11' shape='rectangle'/>

            <tooth id='tooth-21' shape='rectangle'/>
            <tooth id='tooth-22' shape='rectangle'/>
            <tooth id='tooth-23' shape='rectangle'/>
            <tooth id='tooth-24' shape='square'/>
            <tooth id='tooth-25' shape='square'/>
            <tooth id='tooth-26' shape='square'/>
            <tooth id='tooth-27' shape='square'/>
            <tooth id='tooth-28' shape='square'/>

          </div>
          <div class="row mt-3 text-center tooth-row">

            <tooth id='tooth-48' shape='square'/>
            <tooth id='tooth-47' shape='square'/>
            <tooth id='tooth-46' shape='square'/>
            <tooth id='tooth-45' shape='square'/>
            <tooth id='tooth-44' shape='square'/>
            <tooth id='tooth-43' shape='rectangle'/>
            <tooth id='tooth-42' shape='rectangle'/>
            <tooth id='tooth-41' shape='rectangle'/>

            <tooth id='tooth-31' shape='rectangle'/>
            <tooth id='tooth-32' shape='rectangle'/>
            <tooth id='tooth-33' shape='rectangle'/>
            <tooth id='tooth-34' shape='square'/>
            <tooth id='tooth-35' shape='square'/>
            <tooth id='tooth-36' shape='square'/>
            <tooth id='tooth-37' shape='square'/>
            <tooth id='tooth-38' shape='square'/>

          </div>
        </div>
      </b-tab>
      
    </b-tabs> 

    <!-- <b-modal 
      v-model="ifShowModal"
      :title="toothName"
      size="sm"
      centered
      hide-footer>
      <div class="text-center">
        <b-button>A</b-button>
        <b-button>B</b-button>
        <b-button>C</b-button>
      </div>
        <div class="mt-2 text-center">
        <b-button>D</b-button>
        <b-button>E</b-button>
        <b-button>F</b-button>
      </div>
        <div class="mt-2 text-center">
        <b-button>G</b-button>
        <b-button>H</b-button>
        <b-button>I</b-button>
      </div>
    </b-modal> -->
  </div>
</template>

<script>
import Tooth from './components/tooth';
import PersonalForm from './components/personalForm'
export default {
  name: 'App',
  data() {
    return {
      // ifShowModal: false,
      // toothName: "nazwa zęba",
    }
  },
  methods: {
    // showModal() {
    //   this.ifShowModal = true;
    // }
  },
  components: {
    PersonalForm,
    Tooth
  }
}
</script>

<style src="./appStyles.css"></style>
