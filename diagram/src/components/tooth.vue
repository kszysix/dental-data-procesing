<template>
    <div>
        <p v-if='toothPos < 3'>{{ toothPos + toothId }}</p>
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
            <p v-if='toothPos > 2'>{{ toothPos + toothId }}</p>
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
            // colors: ["gray","lightseagreen", "lightsalmon", "darkslategray", "peru", "peachpuff", "internationalorange"],
            // ailments: [null,"wypełnienie","próchnica","usunięty","proteza","przęsło","niewyrżnięty"],
            // color: { A: 'gray', B: 'gray', C: 'gray', D: 'gray', E: 'gray' },
            ailment: { A: null, B: null, C: null, D:null, E:null},
        }
    },
    created() {
        if (this.shape == 'square') this.toothShape = SQUARE_TOOTH_SHAPE;
        else this.toothShape = RECTANGLE_TOOTH_SHAPE;
    },
    mounted() {
        this.$root.$on('clickDeseaseButton', (toothNumber, deseaseId, toothPart) => {
            this.setToothPartDesease(toothNumber, deseaseId, toothPart);
        })
    },
    methods: {
        saveTooth() {
            // return this.ailment;
            return this.toothData.deseases;
        },
        setToothPartDesease(toothNumber, deseaseName, toothPart) {
            if(toothNumber == this.toothPos + this.toothId) {
                this.show[toothPart] = false;
                this.toothData.deseases[toothPart] = deseaseName;
                // if (deseaseId == 5 || deseaseId == 6 || deseaseId == 7) {
                //     for (let part in this.toothData.deseases) {
                //         this.toothData.deseases[part] = deseaseId;
                //     }
                // }
            }
        },
        checkPosition(toothPos, toothPart) {
            if (toothPos < 3) {
                if (toothPart == this.parts.A || toothPart == this.parts.E) return 'top'
                else if (toothPart == this.parts.B) return 'bottom'
                else if (toothPart == this.parts.C) return 'righttop'
                else if (toothPart == this.parts.D) return 'lefttop'
            }
            else if (toothPos > 2) {
                if (toothPart == this.parts.A) return 'top'
                else if (toothPart == this.parts.B || toothPart == this.parts.E) return 'bottom'
                else if (toothPart == this.parts.C) return 'rightbottom'
                else if (toothPart == this.parts.D) return 'leftbottom'
            }
        },
    },
    components: { DeseaseList }
}

</script>