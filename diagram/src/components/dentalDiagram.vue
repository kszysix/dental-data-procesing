<template>
<div>
    <div>
        <h3 v-if='name != null' class='text-left mt-3 ml-3 mb-3'>{{ name }}</h3>
        <h5 v-if='name != null' class='text-left mt-3 ml-3'>Data wersji diagramu: {{ versionDate }}</h5>
    </div>
    <div v-if='name == null' class='mt-3 ml-3 mr-3 '>
        <b-alert show variant="danger">Wprowadź dane pacjenta w zakładce <i>Dane osobowe</i></b-alert>
    </div>

    <div v-if='name != null' class='mt-2 mb-4 mr-3 text-right'>
        <b-button class='text-right' v-on:click="showVersion('-1')" :disabled="oldestVersion">Starsza wersja</b-button>
        <b-button class='text-right' v-on:click="showVersion('1')" :disabled="newestVersion">Nowsza wersja</b-button>
    </div>

    <div class='mt-2 text-right ml-3 mr-3 dental-diagram'>

        <b-card class="mb-1">
            <b-card-header header-tag="header" class="p-1" role="tab">
                <b-button block v-b-toggle.accordion-1 variant="info">Zęby stałe</b-button>
            </b-card-header>
            

            <b-collapse id="accordion-1" visible accordion="my-accordion" role="tabpanel">
                <b-card-body>
                    <div class='diagram' id="printPrimaryDiagram">
                        
                        <div class="row text-center tooth-row mt-4">
                            <tooth ref="tooth-18" tooth-pos='1' tooth-id='8' shape='square'/>
                            <tooth ref="tooth-17" tooth-pos='1' tooth-id='7' shape='square'/>
                            <tooth ref="tooth-16" tooth-pos='1' tooth-id='6' shape='square'/>
                            <tooth ref="tooth-15" tooth-pos='1' tooth-id='5' shape='square'/>
                            <tooth ref="tooth-14" tooth-pos='1' tooth-id='4' shape='square'/>
                            <tooth ref="tooth-13" tooth-pos='1' tooth-id='3' shape='rectangle'/>
                            <tooth ref="tooth-12" tooth-pos='1' tooth-id='2' shape='rectangle'/>
                            <tooth ref="tooth-11" tooth-pos='1' tooth-id='1' shape='rectangle'/>
                            <tooth ref="tooth-21" tooth-pos='2' tooth-id='1' shape='rectangle'/>
                            <tooth ref="tooth-22" tooth-pos='2' tooth-id='2' shape='rectangle'/>
                            <tooth ref="tooth-23" tooth-pos='2' tooth-id='3' shape='rectangle'/>
                            <tooth ref="tooth-24" tooth-pos='2' tooth-id='4' shape='square'/>
                            <tooth ref="tooth-25" tooth-pos='2' tooth-id='5' shape='square'/>
                            <tooth ref="tooth-26" tooth-pos='2' tooth-id='6' shape='square'/>
                            <tooth ref="tooth-27" tooth-pos='2' tooth-id='7' shape='square'/>
                            <tooth ref="tooth-28" tooth-pos='2' tooth-id='8' shape='square'/>
                        </div>

                        <div class="row mt-3 text-center tooth-row">
                            <tooth ref="tooth-48" tooth-pos='4' tooth-id='8' shape='square'/>
                            <tooth ref="tooth-47" tooth-pos='4' tooth-id='7' shape='square'/>
                            <tooth ref="tooth-46" tooth-pos='4' tooth-id='6' shape='square'/>
                            <tooth ref="tooth-45" tooth-pos='4' tooth-id='5' shape='square'/>
                            <tooth ref="tooth-44" tooth-pos='4' tooth-id='4' shape='square'/>
                            <tooth ref="tooth-43" tooth-pos='4' tooth-id='3' shape='rectangle'/>
                            <tooth ref="tooth-42" tooth-pos='4' tooth-id='2' shape='rectangle'/>
                            <tooth ref="tooth-41" tooth-pos='4' tooth-id='1' shape='rectangle'/>
                            <tooth ref="tooth-31" tooth-pos='3' tooth-id='1' shape='rectangle'/>
                            <tooth ref="tooth-32" tooth-pos='3' tooth-id='2' shape='rectangle'/>
                            <tooth ref="tooth-33" tooth-pos='3' tooth-id='3' shape='rectangle'/>
                            <tooth ref="tooth-34" tooth-pos='3' tooth-id='4' shape='square'/>
                            <tooth ref="tooth-35" tooth-pos='3' tooth-id='5' shape='square'/>
                            <tooth ref="tooth-36" tooth-pos='3' tooth-id='6' shape='square'/>
                            <tooth ref="tooth-37" tooth-pos='3' tooth-id='7' shape='square'/>
                            <tooth ref="tooth-38" tooth-pos='3' tooth-id='8' shape='square'/>
                        </div>

                    </div>
                    <div id="printLegend">
                        <desease-legend/>
                    </div>
                    <div v-if='name != null' class='mt-2 mr-3 text-right'>
                        <b-button @click="printPdf('primary')">Pobierz plik PDF</b-button>
                    </div>

                </b-card-body>
            </b-collapse>
        <!-- </b-card> -->

        <!-- <b-card class="mb-1"> -->
            <b-card-header header-tag="header" class="p-1" role="tab">
                <b-button block v-b-toggle.accordion-2 variant="info">Zęby mleczne</b-button>
            </b-card-header>
            <b-collapse id="accordion-2" visible accordion="my-accordion" role="tabpanel">
                <b-card-body>
                    <div class='diagram' id="printBabyDiagram">

                        <div class="row mt-3 text-center tooth-row">
                            <tooth ref="tooth-55" tooth-pos='5' tooth-id='5' shape='square'/>
                            <tooth ref="tooth-54" tooth-pos='5' tooth-id='4' shape='square'/>
                            <tooth ref="tooth-53" tooth-pos='5' tooth-id='3' shape='rectangle'/>
                            <tooth ref="tooth-52" tooth-pos='5' tooth-id='2' shape='rectangle'/>
                            <tooth ref="tooth-51" tooth-pos='5' tooth-id='1' shape='rectangle'/>
                            <tooth ref="tooth-61" tooth-pos='6' tooth-id='1' shape='rectangle'/>
                            <tooth ref="tooth-62" tooth-pos='6' tooth-id='2' shape='rectangle'/>
                            <tooth ref="tooth-63" tooth-pos='6' tooth-id='3' shape='rectangle'/>
                            <tooth ref="tooth-64" tooth-pos='6' tooth-id='4' shape='square'/>
                            <tooth ref="tooth-65" tooth-pos='6' tooth-id='5' shape='square'/>
                        </div>

                        <div class="row mt-3 text-center tooth-row">
                            <tooth ref="tooth-85" tooth-pos='8' tooth-id='5' shape='square'/>
                            <tooth ref="tooth-84" tooth-pos='8' tooth-id='4' shape='square'/>
                            <tooth ref="tooth-83" tooth-pos='8' tooth-id='3' shape='rectangle'/>
                            <tooth ref="tooth-82" tooth-pos='8' tooth-id='2' shape='rectangle'/>
                            <tooth ref="tooth-81" tooth-pos='8' tooth-id='1' shape='rectangle'/>
                            <tooth ref="tooth-71" tooth-pos='7' tooth-id='1' shape='rectangle'/>
                            <tooth ref="tooth-72" tooth-pos='7' tooth-id='2' shape='rectangle'/>
                            <tooth ref="tooth-73" tooth-pos='7' tooth-id='3' shape='rectangle'/>
                            <tooth ref="tooth-74" tooth-pos='7' tooth-id='4' shape='square'/>
                            <tooth ref="tooth-75" tooth-pos='7' tooth-id='5' shape='square'/>
                        </div>

                    </div>                    
                    <desease-legend/>
                    <div v-if='name != null' class='mt-2 mr-3 text-right'>
                        <b-button @click="printPdf('baby')">Pobierz plik PDF</b-button>
                    </div>

                </b-card-body>
            </b-collapse>
        </b-card>
    </div>
    <div class='row mt-5 ml-4'>
        <!-- <div v-if="!micOn"> -->
        <div>
            <b-button @click="mic()">Powiedz komendę</b-button>
        </div>
        <!-- <div v-else>
            <b-button @click="endMic">Zakończ komunikację głosową</b-button>
        </div> -->
    </div>

</div>
</template>

<script>
import Tooth from './tooth';
import DeseaseLegend from './deseaseLegend'
import moment from 'moment'
export default {
    name: 'dentalDiagram',
    data() {
        return {
            name: null,
            command: '',
            versionDate: null,
            oldestVersion: false,
            newestVersion: true,
            micOn: false,
            endMic: false,
            newCommand: 0,
            savedPerson: null,
        }
    },
    watch: {
        newCommand: async function(val) {
            if (this.micOn) {
                await new Promise(resolve => setTimeout(resolve, 100));
                this.mic();
            }
        }
    },
    computed:{

    },
    methods: {
        showTeethData(person) {
            this.savedPerson = person;
            if (person == null) {
                this.resetData();
            }
            else {
                if (person.personalDetails.secondName == '' || person.personalDetails.secondName == null)
                    this.name = person.personalDetails.firstName + ' ' + person.personalDetails.surname
                else this.name = person.personalDetails.firstName + ' ' + person.personalDetails.secondName + ' ' + person.personalDetails.surname
                this.versionDate = moment(String(person.versionDate)).format('DD-MM-YYYY HH:mm');    
                // zęby stałe
                var teeth = person.permanentTeeth;
                for (var i = 1; i < 5; i++) {
                    for (var j = 1; j < 9; j++) {
                        var id = i.toString() + j.toString();
                        var ref = "tooth-" + id;
                        this.$refs[ref].setToothPartDesease(id, teeth[id]['A'], 'A');
                        this.$refs[ref].setToothPartDesease(id, teeth[id]['B'], 'B');
                        this.$refs[ref].setToothPartDesease(id, teeth[id]['C'], 'C');
                        this.$refs[ref].setToothPartDesease(id, teeth[id]['D'], 'D');
                        this.$refs[ref].setToothPartDesease(id, teeth[id]['E'], 'E');
                    }
                }

                // zęby mleczne
                var teeth = person.primaryTeeth;
                for (var i = 5; i < 9; i++) {
                    for (var j = 1; j < 6; j++) {
                        var id = i.toString() + j.toString();
                        var ref = "tooth-" + id;
                        this.$refs[ref].setToothPartDesease(id, teeth[id]['A'], 'A');
                        this.$refs[ref].setToothPartDesease(id, teeth[id]['B'], 'B');
                        this.$refs[ref].setToothPartDesease(id, teeth[id]['C'], 'C');
                        this.$refs[ref].setToothPartDesease(id, teeth[id]['D'], 'D');
                        this.$refs[ref].setToothPartDesease(id, teeth[id]['E'], 'E');
                    }
                }
            }
        },
        getMicCommand() {
            var request = new XMLHttpRequest();
            request.open('GET', 'http://127.0.0.1:5000/mic', false);
            request.send();
            return JSON.parse(request.response);
        },
        useCommand(obj) {
            let info = 'Numer zęba: ' + obj.toothId + '\nCzęść zęba: ' + obj.toothPart + '\nChoroba: ' + obj.toothDesease;
            this.makeToast('default', 'Wczytano następujące zmiany', info);
            var ref = "tooth-" + obj.toothId;
            this.$refs[ref].setToothPartDesease(obj.toothId, obj.toothDesease, obj.toothPart);
        },
        async mic() {
            this.micOn = true;
            this.command = '';
            var obj = this.getMicCommand();
            this.command = obj.command;
            console.log(obj.command);
            if (obj.next == 0 || this.endMic) {
                this.command = '';
                this.endMic = false;
                this.micOn = false;
                return;
            }
            else if (obj.next == 1) {
                console.log("id: " + obj.toothId+"  part: " + obj.toothPart + "  desease: " + obj.toothDesease);
                await this.useCommand(obj);
                this.newCommand++;
                return;
            }
            else if (obj.next == 2) {
                console.log("Please, repeat command:")
            }
            while (obj.next == 1 || obj.next == 2) {
                obj = this.getMicCommand();
                this.command = obj.command;
                console.log(obj.command);
                if(obj.next == 0 || this.endMic){
                    this.command = '';
                    this.endMic = false;
                    this.micOn = false;
                    return;
                }
                else if (obj.next == 1) {
                    console.log("id: " + obj.toothId + "  part: " + obj.toothPart + "  desease: " + obj.toothDesease);
                    await this.useCommand(obj);
                    this.newCommand++;
                    return;
                }
                else if (obj.next == 2) {
                    console.log("Please, repeat command:");
                }
            }
        },
        saveTeeth() {
            var permanentTeeth = {}
            for (var i = 1; i < 5; i++) {
                for (var j = 1; j < 9; j++) {
                    var id = i.toString() + j.toString();
                    var ref = "tooth-" + id;
                    permanentTeeth[id] = this.$refs[ref].saveTooth();
                }
            }
            var babyTeeth = {}
            for (var i = 5; i < 9; i++) {
                for (var j = 1; j < 6; j++) {
                    var id = i.toString() + j.toString();
                    var ref = "tooth-" + id;
                    babyTeeth[id] = this.$refs[ref].saveTooth();
                }
            }
            return { permanentTeeth: permanentTeeth, babyTeeth: babyTeeth };
        },
        showVersion(time){
            if(this.versionDate != null){
                this.$emit('showVersion', time);
            }
        },
        showNoVersion(time){
            if(time == "-1"){
                this.oldestVersion = true;
                this.newestVersion = false;
            }else if(time == "1"){
                this.newestVersion = true;
                this.oldestVersion = false;
            }else{
                this.oldestVersion = false;
                this.newestVersion = false;
            }
        },
        resetData() {
            this.name = null;
            this.versionDate = null;

            for (var i = 1; i < 5; i++) {
                for (var j = 1; j < 9; j++) {
                    var id = i.toString() + j.toString();
                    var ref = "tooth-" + id;
                    this.$refs[ref].setToothPartDesease(id, null, 'A');
                    this.$refs[ref].setToothPartDesease(id, null, 'B');
                    this.$refs[ref].setToothPartDesease(id, null, 'C');
                    this.$refs[ref].setToothPartDesease(id, null, 'D');
                    this.$refs[ref].setToothPartDesease(id, null, 'E');
                }
            }
            for (var i = 5; i < 9; i++) {
                for (var j = 1; j < 6; j++) {
                    var id = i.toString() + j.toString();
                    var ref = "tooth-" + id;
                    this.$refs[ref].setToothPartDesease(id, null, 'A');
                    this.$refs[ref].setToothPartDesease(id, null, 'B');
                    this.$refs[ref].setToothPartDesease(id, null, 'C');
                    this.$refs[ref].setToothPartDesease(id, null, 'D');
                    this.$refs[ref].setToothPartDesease(id, null, 'E');
                }
            }
        },
        makeToast(variant, title, comment) {
            this.$bvToast.toast(comment, {
                title: title,
                variant: variant,
                solid: true,
            })
        },
        printPdf(teeth) {
            if (this.savedPerson == null) {
                this.makeToast('danger', 'Błąd', 'Przed wydrukiem dodaj osobę w formularzu');
                return;
            }
            let prtHtmlDiagram = null;
            if (teeth == 'primary') prtHtmlDiagram = document.getElementById('printPrimaryDiagram').innerHTML;
            else prtHtmlDiagram = document.getElementById('printBabyDiagram').innerHTML;

            const prtHtmlLegend = document.getElementById('printLegend').innerHTML;
            
            let stylesHtml = '';
            for (const node of [...document.querySelectorAll('link[rel="stylesheet"], style')]) {
                stylesHtml += node.outerHTML;
            }

            const WinPrint = window.open('', '', 'left=0,top=0,width=800,height=900,toolbar=0,scrollbars=0,status=0');

            let time = moment(String(new Date().toISOString())).format('DD-MM-YYYY HH:mm'); 

            WinPrint.document.write(`<!DOCTYPE html>
            <html>
            <head>
                ${stylesHtml}
            </head>
            <body>
                <div class='mt-5 ml-5'>
                <h3>${this.name}</h3>
                <h5>Pesel: ${this.savedPerson.personalDetails.pesel}</h5>
                <label>Wygenerowano: ${time}</label>
                </div>
                <div class='mt-5'/>
                ${prtHtmlDiagram}
                <div class='mt-5'/>
                ${prtHtmlLegend}
            </body>
            </html>`);

            WinPrint.document.close();
            WinPrint.focus();
            WinPrint.print();
            // WinPrint.close();
        }
    },
    components: {
        Tooth,
        DeseaseLegend
    }
}
</script>