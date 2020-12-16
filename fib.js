// This will show the first 100 numbers of the sequence

let fir = 0
let sec = 1

console.log(fir)
console.log(sec)


for (let i = 0; i < 100; i++) {
    j = fir + sec
    console.log(j)

    fir = sec
    sec = j
}