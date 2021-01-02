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
    data: function(){
        return {
            colors: ["gray","lightseagreen", "lightsalmon", "darkslategray", "peru", "peachpuff", "internationalorange"],
            ailments: [null,"wypełnienie","próchnica","usunięty","proteza","przęsło","niewyrżnięty"],
            n1: 1,
            n2: 1,
            n3: 1,
            n4: 1,
            n5: 1,
            color: { A: 'gray', B: 'gray', C: 'gray', D: 'gray', E: 'gray' },
            ailment: { A: null, B: null, C: null, D:null, E:null},
            toothShape: null
        }
    },
    created() {
        if (this.shape == 'square') this.toothShape = SQUARE_TOOTH_SHAPE
        else this.toothShape = RECTANGLE_TOOTH_SHAPE
    },

    methods: {
        saveTooth(){
            return this.ailment;
        },

        changecolor(tooth) {
            if (tooth == 'A') {
                this.color.A = this.colors[this.n1]
                this.ailment.A = this.ailments[this.n1];
                this.n1 = (this.n1 + 1) % this.colors.length
            }
            else if (tooth == 'B') {
                this.color.B = this.colors[this.n2]
                this.ailment.B = this.ailments[this.n2];
                this.n2 = (this.n2 + 1) % this.colors.length
            }
            else if (tooth == 'C') {
                this.color.C = this.colors[this.n3]
                this.ailment.C = this.ailments[this.n3];
                this.n3 = (this.n3 + 1) % this.colors.length
            }
            else if (tooth == 'D') {
                this.color.D = this.colors[this.n4]
                this.ailment.D = this.ailments[this.n4];
                this.n4 = (this.n4 + 1) % this.colors.length
            }
            else if (tooth == 'E') {
                this.color.E = this.colors[this.n5]
                this.ailment.E = this.ailments[this.n5];
                this.n5 = (this.n5 + 1) % this.colors.length
            }
        },
		
		setColor(toothPart, toothAilment){
            var newColor = 0;

            switch(toothAilment){
                case this.ailments[1]:
                    newColor = 1;
                    break;
                case this.ailments[2]:
                    newColor = 2;
                    break;
                case this.ailments[3]:
                    newColor = 3;
                    break;
                case this.ailments[4]:
                    newColor = 4;
                    break;
                case this.ailments[5]:
                    newColor = 5;
                    break;
                case this.ailments[6]:
                    newColor = 6;
                    break;
                default:
                    newColor = 0;
            }

			switch(toothPart) {
                case 'A':
                    this.color.A = this.colors[newColor];
                    this.ailment.A = this.ailments[newColor];
                    break;
                case 'B':
                    this.color.B = this.colors[newColor];
                    this.ailment.B = this.ailments[newColor];
                    break;
                case 'C':
                    this.color.C = this.colors[newColor];
                    this.ailment.C = this.ailments[newColor];
                    break;
                case 'D':
                    this.color.D = this.colors[newColor];
                    this.ailment.D = this.ailments[newColor];
                    break;
                case 'E':
                    this.color.E = this.colors[newColor];
                    this.ailment.E = this.ailments[newColor];
                    break;
                case 'F':
                    this.color.A = this.colors[newColor];
                    this.color.B = this.colors[newColor];
                    this.color.C = this.colors[newColor];
                    this.color.D = this.colors[newColor];
                    this.color.E = this.colors[newColor];
                    this.ailment.A = this.ailments[newColor];
                    this.ailment.B = this.ailments[newColor];
                    this.ailment.C = this.ailments[newColor];
                    this.ailment.D = this.ailments[newColor];
                    this.ailment.E = this.ailments[newColor];
                    break;
                default:
                    
                }
		}
    },
}

</script>