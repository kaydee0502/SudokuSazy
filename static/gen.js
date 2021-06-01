

var row = [...Array(81).keys()].map(x => ++x)

function shuffle(lin_sudoku){
    for (let i=0; i<lin_sudoku.length;i++){

        psuedoIndex = Math.floor(Math.random()*81);
        if (psuedoIndex === i){
            continue;
        }
        lin_sudoku[i] = lin_sudoku[i] + lin_sudoku[psuedoIndex];
        lin_sudoku[psuedoIndex] = lin_sudoku[i] - lin_sudoku[psuedoIndex];
        lin_sudoku[i] = lin_sudoku[i] - lin_sudoku[psuedoIndex];
      
        } 

    return lin_sudoku;


}

row = shuffle(row)




var sudoku = new Array(9)
sudoku.fill(0)

sudoku.forEach((val,index) => {
    //console.log(index)
    sudoku[index] = new Array(9).fill(0)
})



function isSafeRow(sudoku,element,i){

    for (let j = 0; j<sudoku.length;j++){
        if (sudoku[i][j] === element){
            return false
        }
    }
    return true;


}

function isSafeCol(sudoku,element,j){

    for (let i=0; i<sudoku.length; i++){
        if (sudoku[i][j] === element){
            return false;
        } 
 
    }
    return true;
}

function isSafeBlock(sudoku,element,i,j){

    i = Math.floor(i/3)*3
    j = Math.floor(j/3)*3

    for (let x=i;x<i+3;x++){
        for (let y=j;y<y+3;y++){
            if (sudoku[x][y] == element){
                return false
            }
        }
    }
    return true
}

function safe(sudoku,i,j,element){

    return isSafeRow(sudoku,element,i) && isSafeCol(sudoku,element,j) && isSafeBlock(sudoku,element,i,j)


}


function isFilled(sudoku){

    for (let i = 0; i < 9; i++){
        for (let j = 0; j < 9; j++){
            if (sudoku[i][j] == 0){
                return false
            }
        }

    }
    return true

}


function sfill(sudoku,row){


    if (isFilled(sudoku)){
        return true
    }
    

    for (let ri = 0; ri < row.length; ri++){

        console.log(ri)  
        for (let i = 1; i <= 9; i++){
             
            
            x = Math.floor(ri/3)
            y = ri%3

            if (safe(sudoku,x,y,i)){
                sudoku[x][y] = i
                        

                 
            if (sfill(sudoku)){
                return true
            }

            sudoku[x][y] = 0
        }


        }
        break;
    }

}

sfill(sudoku,row)

