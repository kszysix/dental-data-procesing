<template>
    <div class='text-center legend mt-4 mb-3'>
        <label class='mb-3'>Lista oznaczeń</label>
        <b-list-group horizontal='md'>
            <div
                class="desease-legend mr-1 text-center"
                v-for="(desease, index) in deseases"
                :index='index'
                :key="desease.id">
                <b-list-group-item
                    :style='"background-color: " + desease.color'>
                    {{ desease.name }}
                </b-list-group-item>
            </div>
        </b-list-group>
    </div>
</template>

<script>
import { DESEASES } from './../assets/dentalData'
export default {
    data() {
        return {
            deseases: DESEASES
        }
    },
}
</script>