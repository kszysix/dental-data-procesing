<template>
<div>
 
    <b-form class="ml-3 mr-3 personal-form round-corner">

        <label class='h4 mb-4'>DANE OSOBOWE</label>

        <div class="row">
            <div class="col sm">
                <label for="first-name">Pierwsze imię</label>
                <b-form-input id="first-name" ref="first-name" type="text"></b-form-input>
            </div>
            <div class="col sm">
                <label for="second-name">Drugie imię</label>
                <b-form-input id="second-name" ref="second-name" type="text"></b-form-input>
            </div>
            <div class="col sm">
                <label for="surname">Nazwisko</label>
                <b-form-input id="surname" ref="surname" type="text"></b-form-input>
            </div>
        </div>

        <div class="row mt-3 mb-2">
            <div class="col sm">
                <label for="birth-date">Data urodzenia</label>
                <b-form-input id="birth-date" ref="birth-date" type="date"></b-form-input>
            </div>
            <div class="col sm">
                <label for="pesel">Pesel</label>
                <b-form-input id="pesel" ref="pesel" type="number"></b-form-input>
            </div>
            <div class="col sm">
                <label for="gender">Płeć</label>
                <b-form-radio-group id="gender">
                <b-form-radio value="male">Mężczyzna</b-form-radio>
                <b-form-radio value="female">Kobieta</b-form-radio>
                </b-form-radio-group>
            </div>
        </div>

    </b-form>

    <b-form class="ml-3 mr-3 personal-form round-corner">

        <label class='h4 mb-4'>DANE KONTAKTOWE</label>

        <div class="row">
            <div class="col sm">
                <label for="phone-number">Numer telefonu</label>
                <b-form-input id="phone-number" ref="phone-number" type="text"></b-form-input>
            </div>
            <div class="col sm">
                <label for="e-mail">E-mail</label>
                <b-form-input id="e-mail" ref="e-mail" type="text"></b-form-input>
            </div>
        </div>

        <div class="row mt-3 mb-2">
            <div class="col sm">
                <label for="street">Ulica</label>
                <b-form-input id="street" ref="street" type="text"></b-form-input>
            </div>
            <div class="col sm">
                <label for="address-1">Numer domu</label>
                <b-form-input id="address-1" ref="address-1" type="number"></b-form-input>
            </div>
            <div class="col sm">
                <label for="address-2">Numer lokalu</label>
                <b-form-input id="address-2" ref="address-2" type="number"></b-form-input>
            </div>
        </div>

        <div class="row mt-3 mb-2">
            <div class="col sm">
                <label for="zip-code">Kod pocztowy</label>
                <b-form-input id="zip-code" ref="zip-code" type="text"></b-form-input>
            </div>
            <div class="col sm">
                <label for="city">Miejscowość</label>
                <b-form-input id="city" ref="city" type="text"></b-form-input>
            </div>
        </div>
          
    </b-form>
</div>
</template>

<script>
export default {
    methods:{
        getPersonData(person){
            person = JSON.parse(person);
            this.$refs["first-name"].value = person.personalDetails.firstName;
            this.$refs["second-name"].value = person.personalDetails.secondName;
            this.$refs["surname"].value = person.personalDetails.lastName;
            // this.$refs["birth-date"].value = person.personalDetails.firstName;
            this.$refs["pesel"].value = person.personalDetails.pesel;
            // this.$refs["gender"].value = person.personalDetails.firstName;

            this.$refs["phone-number"].value = person.contactDetails.phoneNumber;
            this.$refs["e-mail"].value = person.contactDetails.email;

            this.$refs["street"].value = person.contactDetails.street;
            this.$refs["address-1"].value = person.contactDetails.streetNumber;
            this.$refs["address-2"].value = person.contactDetails.boxNumber;
            this.$refs["zip-code"].value = person.contactDetails.zipCode;
            this.$refs["city"].value = person.contactDetails.city;
        }
    }
}
</script>