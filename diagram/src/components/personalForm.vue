<template>
<div>
    <div class="col sm">
        <label for="person-pesel">Podaj pesel:</label>
        <b-form-input
            id="person-pesel"
            ref="person-pesel"
            v-model="personPesel"
            type="text"
            :state="personPeselState">
        </b-form-input>
        <b-button class='mt-2 mb-4' v-on:click="showData()">Wybierz osobę</b-button>
    </div>
 
    <b-form class="ml-3 mr-3 personal-form round-corner">

        <label class='h4 mb-4'>DANE OSOBOWE</label>

        <div class="row">
            <div class="col sm">
                <label for="first-name">Pierwsze imię</label>
                <b-form-input id="first-name" type="text" v-model="firstName" :state="firstNameState"></b-form-input>
            </div>
            <div class="col sm">
                <label for="second-name">Drugie imię</label>
                <b-form-input id="second-name" type="text" v-model="secondName"></b-form-input>
            </div>
            <div class="col sm">
                <label for="surname">Nazwisko</label>
                <b-form-input id="surname" type="text" v-model="surname" :state="surnameState"></b-form-input>
            </div>
        </div>

        <div class="row mt-3 mb-2">
            <div class="col sm">
                <label for="birth-date">Data urodzenia</label>
                <b-form-input id="birth-date" type="date" v-model="birthDate"></b-form-input>
            </div>
            <div class="col sm">
                <label for="pesel">Pesel</label>
                <b-form-input id="pesel" type="text" v-model="pesel" :state="peselState"></b-form-input>
            </div>
            <div class="col sm">
                <label for="gender">Płeć</label>
                <div class="genders">
                    <b-form-radio v-model="gender" value="male" >Mężczyzna</b-form-radio>
                    <b-form-radio v-model="gender" value="female" >Kobieta</b-form-radio>
                </div>

            </div>
        </div>

    </b-form>

    <b-form class="ml-3 mr-3 personal-form round-corner">

        <label class='h4 mb-4'>DANE KONTAKTOWE</label>

        <div class="row">
            <div class="col sm">
                <label for="phone-number">Numer telefonu</label>
                <b-form-input id="phone-number" type="text" v-model="phoneNumber"></b-form-input>
            </div>
            <div class="col sm">
                <label for="e-mail">E-mail</label>
                <b-form-input id="email" type="text" v-model="email"></b-form-input>
            </div>
        </div>

        <div class="row mt-3 mb-2">
            <div class="col sm">
                <label for="street">Ulica</label>
                <b-form-input id="street" type="text" v-model="street"></b-form-input>
            </div>
            <div class="col sm">
                <label for="address-1">Numer domu</label>
                <b-form-input id="street-number" type="number" v-model="streetNumber"></b-form-input>
            </div>
            <div class="col sm">
                <label for="address-2">Numer lokalu</label>
                <b-form-input id="box-number" type="number" v-model="boxNumber"></b-form-input>
            </div>
        </div>

        <div class="row mt-3 mb-2">
            <div class="col sm">
                <label for="zip-code">Kod pocztowy</label>
                <b-form-input id="zip-code" type="text" v-model="zipCode"></b-form-input>
            </div>
            <div class="col sm">
                <label for="city">Miejscowość</label>
                <b-form-input id="city" type="text" v-model="city"></b-form-input>
            </div>
        </div>
          
    </b-form>

    <div class='ml-3 mt-2'>
        <b-button v-on:click="showSaveModal">Zapisz dane</b-button>
        <b-button class='ml-2' @click="showResetModal">Resetuj dane</b-button>
    </div>

    <b-modal
        v-model="ifShowSaveModal"
        class='confirmModal'
        @ok='savePersonData' 
        :hide-header='true'
        cancel-title='Anuluj'
        ok-title='Zapisz'
        centered>
        Czy skończyłeś wprowadzanie danych i chcesz zapisać nową wersję diagramu w systemie?
    </b-modal>

    <b-modal
        v-model="ifShowResetModal"
        class='confirmModal'
        @ok='resetPerson' 
        :hide-header='true'
        cancel-title='Anuluj'
        ok-title='Resetuj'
        centered>
        Czy na pewno chcesz resetować wprowadzone dane?
    </b-modal>
</div>
</template>

<script>
export default {
    data: function() {
        return {
            versionDate: null,
            person: {},
            firstName: null,
            secondName: null,
            surname: null,
            birthDate: null,
            pesel: null,
            gender: null,
            phoneNumber: null,
            email: null,
            street: null,
            streetNumber: null,
            boxNumber: null,
            zipCode: null,
            city: null,
            personPesel: null,
            notExists: false,
            cannotSaveState: false,
            confirmSaveState: false,
            ifShowSaveModal: false,
            ifShowResetModal: false
        }
    },
    watch: {
        pesel: function(val) {
            if (val.length > 5) {
                let year = val.substring(0,2);
                let month = val.substring(2,4);
                let day = val.substring(4,6);
                console.log(year, month, day)
                if (parseInt(month) < 13) {
                    this.birthDate = '19' + year + '-' + month + '-' + day;
                }
                else {
                    month = (parseInt(month) - 20).toString();
                    if (month.length == 1) month = '0' + month;
                    this.birthDate = '20' + year + '-' + month + '-' + day;
                }
            } 
        }
    },
    computed: {
        firstNameState() {
            if (this.firstName) {
                return this.firstName.length > 2 ? true : false;
            }
            else {
                return false;
            }
        },
        surnameState() {
            if (this.surname) {
                return this.surname.length > 2 ? true : false;
            }
            else {
                return false;
            }
        },
        peselState() {
            if (this.pesel) {
                return this.pesel.length == 11 ? true : false;
            }
            else {
                return false;
            }
        },
        personPeselState() {
            if (this.personPesel) {
                return this.personPesel.length == 11 ? true : false;
            }
            else {
                return null;
            }
        }
    },
    methods:{
        showData(){
            this.cannotSaveState = false;
            this.confirmSaveState = false;
            if (this.personPeselState) {
                var request = new XMLHttpRequest();
                request.open('POST', 'http://127.0.0.1:5000/getPersonData', false);
                request.send(this.personPesel);
                if (request.response == "0") {
                    console.log("Pesel: " + this.personPesel + " does not exist in mongoDatabase.");
                    this.notExists = true;
                    this.makeToast('danger', 'Błąd odczytu danych', 'Nie znaleziono osoby o wskazanym peselu');
                    this.resetPerson();
                    return;
                }
                else {
                    this.notExists = false;
                    this.makeToast('success', 'Operacja powiodła się', 'Poprawnie wczytano dane')
                }

                this.showPersonData(request.response);
            }
        },
        resetPerson() {
            this.showPersonData(null);
        },
        showDataVersion(time){
            this.cannotSaveState = false;
            this.confirmSaveState = false;
            if (this.personPeselState) {
                var request = new XMLHttpRequest();
                request.open('POST', 'http://127.0.0.1:5000/getPersonDataVersion', false);
                var requestMsg = {
                    "pesel":this.personPesel,
                    "versionDate":this.versionDate,
                    // jeżeli time == -1 to starsza wersja, jeżeli == 1 to nowsza
                    "time":time
                }
                request.send(JSON.stringify(requestMsg));
                if (request.response == "0") {
                    console.log("Pesel: " + this.personPesel + " does not exist in mongoDatabase.");
                    this.notExists = true;
                    return;
                }else if(request.response == "-1"){
                    // nie ma starszej wersji
                    //TODO
                    this.$emit('showNoVersion', "-1");
                    return;
                }else if(request.response == "1"){
                    // nie ma nowszej wersji
                    //TODO
                    this.$emit('showNoVersion', "1");
                    return;
                }
                else {
                    this.notExists = false;
                }
                this.$emit('showNoVersion', "0");
                this.showPersonData(request.response);
            }
        },
        showPersonData(person) {
            if (person != null) {
                person = JSON.parse(person);
                this.$emit('getTeeth', person)

                this.versionDate = person.versionDate;

                this.firstName = person.personalDetails.firstName;
                this.secondName = person.personalDetails.secondName;
                this.surname = person.personalDetails.surname;
                this.birthDate = person.personalDetails.birthDate;
                this.pesel = person.personalDetails.pesel;
                this.gender = person.personalDetails.gender;
                this.phoneNumber = person.contactDetails.phoneNumber;
                this.email = person.contactDetails.email;
                this.street = person.contactDetails.street;
                this.streetNumber = person.contactDetails.streetNumber;
                this.boxNumber = person.contactDetails.boxNumber;
                this.zipCode = person.contactDetails.zipCode;
                this.city = person.contactDetails.city;
            }
            else {
                this.$emit('getTeeth', null)
                this.versionDate = null;
                this.firstName = null;
                this.secondName = null;
                this.surname = null;
                this.birthDate = null;
                this.pesel = null;
                this.gender = null;
                this.phoneNumber = null;
                this.email = null;
                this.street = null;
                this.streetNumber = null;
                this.boxNumber = null;
                this.zipCode = null;
                this.city = null;
                this.personPesel = null;
            }
        },
        savePersonData() {
            var person = {};
            var personalDetails = this.savePersonalDetails();
            if (personalDetails == null) {
                this.cannotSaveState = true;
                this.confirmSaveState = false;
                this.makeToast('danger', 'Błąd zapisu danych', 'Dane nie są kompletne')
                return;
            }
            else {
                this.cannotSaveState = false;
                this.confirmSaveState = true;
                this.makeToast('success', 'Operacja powiodła się', 'Dane zostały poprawnie zapisane')
            }

            var contactDetails = this.saveContactDetails();
            person.personalDetails = personalDetails;
            person.contactDetails = contactDetails;

            this.person = person;
            this.$emit('setPerson');

            // var primaryTeeth = {};
            // person.primaryTeeth = primaryTeeth;
        },
        saveData(teeth) {
            this.person.permanentTeeth = teeth.permanentTeeth;
            this.person.primaryTeeth = teeth.babyTeeth;
            this.person.versionDate = new Date().toISOString();
            var request = new XMLHttpRequest();
            request.open('POST', 'http://127.0.0.1:5000/savePersonData', false);
            request.send(JSON.stringify(this.person));

            var confirmation = request.response;
            if (this.confirmSaveState == true) this.$emit('getTeeth', this.person)
        },
        savePersonalDetails() {
            if (this.firstNameState && this.surnameState && this.peselState) {
                var jsonPerson = {};
                jsonPerson.firstName = this.firstName;
                jsonPerson.secondName = this.secondName;
                jsonPerson.surname = this.surname;
                jsonPerson.birthDate = this.birthDate;
                jsonPerson.pesel = this.pesel;
                jsonPerson.gender = this.gender;
                return jsonPerson;
            }
            else {
                return null;
            }
        },
        saveContactDetails() {
            if (this.firstNameState && this.surnameState && this.peselState) {
                var jsonPerson = {};
                jsonPerson.phoneNumber = this.phoneNumber;
                jsonPerson.email = this.email;
                jsonPerson.street = this.street;
                jsonPerson.streetNumber = this.streetNumber;
                jsonPerson.boxNumber = this.boxNumber;
                jsonPerson.zipCode = this.zipCode;
                jsonPerson.city = this.city;
                return jsonPerson;
            }
            else {
                return null;
            }
        },
        showSaveModal() {
            if (this.firstNameState && this.surnameState && this.peselState)
                this.ifShowSaveModal = true;
            else
                this.makeToast('danger', 'Błąd zapisu danych', 'Dane nie są kompletne');
        },
        showResetModal() {
            this.ifShowResetModal = true;
        },
        makeToast(variant, title, comment) {
            this.$bvToast.toast(comment, {
                title: title,
                variant: variant,
                solid: true,
            })
        }
    }
}
</script>