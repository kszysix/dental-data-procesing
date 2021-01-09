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
        <p id="notExists" v-if="notExists">Nie ma takiego PESELu w bazie.</p>
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

    <div>
        <div class='row mt-2 ml-3 mb-4'>
            <b-button v-on:click="savePersonData()">Zapisz dane</b-button>
            <p class='ml-2' id="saveState" v-if="cannotSaveState">Nie zapisano danych - dane niekompletne.</p>
            <p class='ml-2' id="saveState" v-if="confirmSaveState">Zapisano dane do bazy.</p>
        </div>
    </div>
</div>
</template>

<script>
export default {
    data: function() {
        return {
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
            cannotSaveState: false,
            confirmSaveState: false
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
                    return;
                }
                else {
                    this.notExists = false;
                }
                //var person = JSON.parse(request.response);

                this.showPersonData(request.response);
            }
        },
        showPersonData(person) {
            person = JSON.parse(person);
            this.$emit('getTeeth', person)

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
        },
        savePersonData() {
            var person = {};
            var personalDetails = this.savePersonalDetails();
            if (personalDetails == null) {
                this.cannotSaveState = true;
                this.confirmSaveState = false;
                return;
            }
            else {
                this.cannotSaveState = false;
                this.confirmSaveState = true;
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
    }
}
</script>