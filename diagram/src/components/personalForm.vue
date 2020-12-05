<template>
<div>
    <b-form class="ml-3 mr-3 personal-form round-corner">

        <label class='h4 mb-4'>DANE OSOBOWE</label>

        <div class="row">
            <div class="col sm">
                <label for="first-name">Pierwsze imię</label>
                <b-form-input id="first-name" type="text"></b-form-input>
            </div>
            <div class="col sm">
                <label for="second-name">Drugie imię</label>
                <b-form-input id="second-name" type="text"></b-form-input>
            </div>
            <div class="col sm">
                <label for="surname">Nazwisko</label>
                <b-form-input id="surname" type="text"></b-form-input>
            </div>
        </div>

        <div class="row mt-3 mb-2">
            <div class="col sm">
                <label for="birth-date">Data urodzenia</label>
                <b-form-input id="pesel" type="date"></b-form-input>
            </div>
            <div class="col sm">
                <label for="pesel">Pesel</label>
                <b-form-input id="pesel" type="number"></b-form-input>
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
                <b-form-input id="phone-number" type="text"></b-form-input>
            </div>
            <div class="col sm">
                <label for="e-mail">E-mail</label>
                <b-form-input id="e-mail" type="text"></b-form-input>
            </div>
        </div>

        <div class="row mt-3 mb-2">
            <div class="col sm">
                <label for="street">Ulica</label>
                <b-form-input id="street" type="text"></b-form-input>
            </div>
            <div class="col sm">
                <label for="address-1">Numer domu</label>
                <b-form-input id="address-1" type="number"></b-form-input>
            </div>
            <div class="col sm">
                <label for="address-2">Numer lokalu</label>
                <b-form-input id="address-2" type="number"></b-form-input>
            </div>
        </div>

        <div class="row mt-3 mb-2">
            <div class="col sm">
                <label for="zip-code">Kod pocztowy</label>
                <b-form-input id="zip-code" type="text"></b-form-input>
            </div>
            <div class="col sm">
                <label for="city">Miejscowość</label>
                <b-form-input id="city" type="text"></b-form-input>
            </div>
        </div>
          
    </b-form>
</div>
</template>

<script>
export default {
    
}
</script>