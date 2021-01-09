<template>
    <div class='row'>
        <div class='col'>
            <b-list-group flush>
                <div
                    class="desease-button"
                    v-for="(desease, index) in deseases"
                    :index='index'
                    :key="desease.id">
                    <b-list-group-item
                        :style='"background-color: " + desease.color'
                        @click="clickDeseaseButton(desease.name, toothPart)"
                        button>
                        {{ desease.name }}
                    </b-list-group-item>
                </div>
            </b-list-group>
        </div>
    </div>
</template>

<script>
import { DESEASES } from './../assets/dentalData'
export default {
    name: 'deseasePopover',
    props: ['toothNumber', 'toothPart'],
    data() {
        return {
            deseases: DESEASES,
        }
    },
    methods: {
        clickDeseaseButton(deseaseName, toothPart) {
            this.$root.$emit('clickDeseaseButton', this.toothNumber, deseaseName, toothPart);
        }
    },
}
</script>