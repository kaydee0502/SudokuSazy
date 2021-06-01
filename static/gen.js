

var row = [...Array(81).keys()].map(x => ++x)

for (i=0; i<row.length;i++){

    psuedoIndex = Math.floor(Math.random()*81);
    if (psuedoIndex === i){
        continue;
    }
    row[i] = row[i] + row[psuedoIndex];
    row[psuedoIndex] = row[i] - row[psuedoIndex];
    row[i] = row[i] - row[psuedoIndex];
  
    } 


console.log(row)


let sudoku = new Array(9)
sudoku.fill(0)

sudoku.forEach((val,index) => {
    console.log(index)
    sudoku[index] = new Array(9).fill(0)
})

sudoku[0][1] = 1;
console.log(sudoku)