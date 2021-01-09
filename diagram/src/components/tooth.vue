<template>
    <div>
        <p v-if='toothPos < 3 || (toothPos > 4 && toothPos < 7)'>{{ toothPos + toothId }}</p>
        <div class="text-center mt-2 ml-1 mr-1 mb-2">
            <svg
                id='test'
                class='tooth'
                :class="{ clicked: show.A || show.B || show.C || show.D || show.E }"
                viewBox="0 0 100 100"
                role="group"
                height="100"
                width="100">
                <g v-for="part in parts" :key="part">
                    <path
                        :id='toothPos + toothId + parts[part]'
                        class='clickable-tooth'
                        :d="toothShape[part]"
                        :fill="deseases.find(elem => elem.name == toothData.deseases[part]).color"/>
                </g>
            </svg>
        </div>
        <div class='mt-3'>
            <p v-if='(toothPos > 2 && toothPos < 5) || toothPos > 6'>{{ toothPos + toothId }}</p>
        </div>

        <div v-for="part in parts" :key="part">
            <b-popover
                :show.sync="show[part]"
                :target='toothPos + toothId + parts[part]'
                delay=0
                triggers="click blur"
                :placement='checkPosition(toothPos, parts[part])'>
                <desease-list
                    :tooth-number="toothPos + toothId"
                    :tooth-part='parts[part]'/>
            </b-popover>
        </div>
    </div>
</template>

<script>
import {
    SQUARE_TOOTH_SHAPE,
    RECTANGLE_TOOTH_SHAPE,
    DESEASES,
} from './../assets/dentalData'
import DeseaseList from './deseaseList.vue'

export default {
    name: 'tooth',
    props: ['shape', 'toothPos', 'toothId'],
    data: function(){
        return {
            deseases: DESEASES,
            toothShape: null,
            toothData: {
                id: this.toothPos + this.toothId,
                deseases: { A: null, B: null, C: null, D: null, E: null },
            },
            parts: { A: 'A', B: 'B', C: 'C', D: 'D', E: 'E' },
            show: { A: false, B: false, C: false, D: false, E: false },
        }
    },
    created() {
        if (this.shape == 'square') this.toothShape = SQUARE_TOOTH_SHAPE[(this.toothPos - 1) % 4];
        else this.toothShape = RECTANGLE_TOOTH_SHAPE[(this.toothPos - 1) % 4];
    },
    mounted() {
        this.$root.$on('clickDeseaseButton', (toothNumber, deseaseId, toothPart) => {
            this.setToothPartDesease(toothNumber, deseaseId, toothPart);
        })
    },
    methods: {
        saveTooth() {
            return this.toothData.deseases;
        },
        setToothPartDesease(toothNumber, deseaseName, toothPart) {
            if(toothNumber == this.toothPos + this.toothId) {
                if(toothPart == 'F'){
                    this.setToothFullDesease(deseaseName);
                }else{
                    this.show[toothPart] = false;
                    this.toothData.deseases[toothPart] = deseaseName;
                    // if (deseaseId == 5 || deseaseId == 6 || deseaseId == 7) {
                    //     for (let part in this.toothData.deseases) {
                    //         this.toothData.deseases[part] = deseaseId;
                    //     }
                    // }
            }
            }
        },
        checkPosition(toothPos, toothPart) {
            if (toothPos == 1 || toothPos == 5) {
                if (toothPart == this.parts.B || toothPart == this.parts.D) return 'top'
                else if (toothPart == this.parts.E) return 'bottom'
                else if (toothPart == this.parts.A) return 'righttop'
                else if (toothPart == this.parts.C) return 'lefttop'
            }
            else if (toothPos == 2 || toothPos == 6) {
                if (toothPart == this.parts.B || toothPart == this.parts.D) return 'top'
                else if (toothPart == this.parts.E) return 'bottom'
                else if (toothPart == this.parts.C) return 'righttop'
                else if (toothPart == this.parts.A) return 'lefttop'
            }
            else if (toothPos == 3 || toothPos == 7) {
                if (toothPart == this.parts.E) return 'top'
                else if (toothPart == this.parts.B || toothPart == this.parts.D) return 'bottom'
                else if (toothPart == this.parts.C) return 'rightbottom'
                else if (toothPart == this.parts.A) return 'leftbottom'
            }
            else if (toothPos == 4 || toothPos == 8) {
                if (toothPart == this.parts.E) return 'top'
                else if (toothPart == this.parts.B || toothPart == this.parts.D) return 'bottom'
                else if (toothPart == this.parts.A) return 'rightbottom'
                else if (toothPart == this.parts.C) return 'leftbottom'
            }
        },
        setToothFullDesease(deseaseName){
            this.show['A'] = false;
            this.toothData.deseases['A'] = deseaseName;
            this.show['B'] = false;
            this.toothData.deseases['B'] = deseaseName;
            this.show['C'] = false;
            this.toothData.deseases['C'] = deseaseName;
            this.show['D'] = false;
            this.toothData.deseases['D'] = deseaseName;
            this.show['E'] = false;
            this.toothData.deseases['E'] = deseaseName;
        }
    },
    components: { DeseaseList }
}

</script>