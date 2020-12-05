<template>
    <div>
        <div class="text-center mt-2 ml-2 mr-2 mb-2">
            <svg
                class='tooth'
                viewBox="0 0 100 100"
                role="group"
                height="100" width="100"
                >
                <g>
                    <path
                        class='clickable-tooth'
                        @click="changecolor('A')"
                        :d="toothShape.A"
                        :fill="color.A"/>
                    <path
                        class='clickable-tooth'
                        @click="changecolor('B')"
                        :d="toothShape.B"
                        :fill="color.B"/>
                    <path
                        class='clickable-tooth'
                        @click="changecolor('C')"
                        :d="toothShape.C"
                        :fill="color.C"/>
                    <path
                        class='clickable-tooth'
                        @click="changecolor('D')"
                        :d="toothShape.D"
                        :fill="color.D"/>
                    
                    <path
                        class='clickable-tooth'
                        @click="changecolor('E')"
                        :d="toothShape.E"
                        :fill="color.E"/>
                </g>
            </svg>
        </div>
    </div>
</template>

<script>
import { SQUARE_TOOTH_SHAPE, RECTANGLE_TOOTH_SHAPE } from './../assets/dentalData'

export default {
    name: 'tooth',
    props: ['shape'],
    data() {
        return {
            colors: ["lightseagreen", "lightsalmon", "darkslategray", "peru", "peachpuff", "gray"],
            n1: 0,
            n2: 0,
            n3: 0,
            n4: 0,
            n5: 0,
            color: { A: 'gray', B: 'gray', C: 'gray', D: 'gray', E: 'gray' },
            toothShape: null
        }
    },
    created() {
        if (this.shape == 'square') this.toothShape = SQUARE_TOOTH_SHAPE
        else this.toothShape = RECTANGLE_TOOTH_SHAPE
    },
    methods: {
        changecolor(tooth) {
            if (tooth == 'A') {
                this.color.A = this.colors[this.n1]
                this.n1 = (this.n1 + 1) % 6
            }
            else if (tooth == 'B') {
                this.color.B = this.colors[this.n2]
                this.n2 = (this.n2 + 1) % 6
            }
            else if (tooth == 'C') {
                this.color.C = this.colors[this.n3]
                this.n3 = (this.n3 + 1) % 6
            }
            else if (tooth == 'D') {
                this.color.D = this.colors[this.n4]
                this.n4 = (this.n4 + 1) % 6
            }
            else if (tooth == 'E') {
                this.color.E = this.colors[this.n5]
                this.n5 = (this.n5 + 1) % 6
            }
        },
    },
}

</script>