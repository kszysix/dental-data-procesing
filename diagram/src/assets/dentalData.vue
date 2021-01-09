<script>
    export default { }

    // A - powierzchnia bliższa
    // B - powierzchnia żująca
    // C - powierzchnia dalsza
    // D - powierzchnia policzkowa
    // E - powierzchnia językowa

    const As = 'M3 0 L30 27 L70 27 L97 0 Z'
    const Bs = 'M30 73 L3 100 L97 100 L70 73 Z'
    const Cs = 'M73 30 L73 70 L100 97 L100 3 Z'
    const Ds = 'M0 3 L0 97 L27 70 L27 30 Z'
    const Es = 'M31 31 L31 69 L69 69 L69 31 Z'

    const Ar = 'M3 0 L20 37 L80 37 L97 0 Z'
    const Br = 'M20 63 L3 100 L97 100 L80 63 Z'
    const Cr = 'M83 40 L83 60 L100 97 L100 3 Z'
    const Dr = 'M0 3 L0 97 L17 60 L17 40 Z'
    const Er = 'M21 41 L21 59 L79 59 L79 41 Z'

    export const SQUARE_TOOTH_SHAPE = [
        { A: Cs, B: Es, C: Ds, D: As, E: Bs },
        { A: Ds, B: Es, C: Cs, D: As, E: Bs },
        { A: Ds, B: Es, C: Cs, D: Bs, E: As },
        { A: Cs, B: Es, C: Ds, D: Bs, E: As },
    ]

    export const RECTANGLE_TOOTH_SHAPE = [
        { A: Cr, B: Er, C: Dr, D: Ar, E: Br },
        { A: Dr, B: Er, C: Cr, D: Ar, E: Br },
        { A: Dr, B: Er, C: Cr, D: Br, E: Ar },
        { A: Cr, B: Er, C: Dr, D: Br, E: Ar },
    ]
    
    // export const DESEASES = [
    //     { id: 0, name: 'Zdrowy', color: 'lavender'},
    //     { id: 1, name: 'Próchnica', color: 'lightcoral'},
    //     { id: 2, name: 'Ubytek niepróchnicowy', color: 'gold'},
    //     { id: 3, name: 'Wypełnienie stałe', color: 'skyblue'},
    //     { id: 4, name: 'Wypełnienie czasowe', color: 'pink'},
    //     { id: 5, name: 'Implant', color: 'darkseagreen'},
    //     { id: 6, name: 'Do usunięcia', color: 'silver'},
    //     { id: 7, name: 'Brak zęba', color: 'dimgray'},
    // ]

    export const DESEASES = [
        { name: null, color: 'lavender'},
        { name: 'wypełnienie', color: 'lightcoral'},
        { name: 'próchnica', color: 'gold'},
        { name: 'usunięty', color: 'skyblue'},
        { name: 'proteza', color: 'pink'},
        { name: 'przęsło', color: 'darkseagreen'},
        { name: 'niewyrżnięty', color: 'silver'},
    ]
</script>