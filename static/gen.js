

var row = [...Array(81).keys()]

function shuffle(lin_sudoku){
    for (let i=0; i<lin_sudoku.length;i++){

        psuedoIndex = Math.floor(Math.random()*9);
        if (psuedoIndex === i){
            continue;
        }
        lin_sudoku[i] = lin_sudoku[i] + lin_sudoku[psuedoIndex];
        lin_sudoku[psuedoIndex] = lin_sudoku[i] - lin_sudoku[psuedoIndex];
        lin_sudoku[i] = lin_sudoku[i] - lin_sudoku[psuedoIndex];
      
        } 

    return lin_sudoku;


}


function print(s){
    for (let i = 0; i< 9;i++){

        console.log(...s[i]);
    }


}

let sudoku = new Array(9)
sudoku.fill(0)

sudoku.forEach((val,index) => {
    //console.log(index)
    sudoku[index] = new Array(9).fill(0)
})



function isSafeRow(sudoku,element,i){
    //console.log(sudoku,i)

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
        for (let y=j;y<j+3;y++){
            //console.log(i,j,element)
            if (sudoku[x][y] === element){
                
                return false
            }
        }
    }
    return true
}

function safe(sudoku,i,j,element){
    //console.log(isSafeRow(sudoku,element,i),isSafeCol(sudoku,element,j),isSafeBlock(sudoku,element,i,j))
    return isSafeRow(sudoku,element,i) && isSafeCol(sudoku,element,j) && isSafeBlock(sudoku,element,i,j)


}


function isFilled(sudoku){

    for (let i = 0; i < 9; i++){
        for (let j = 0; j < 9; j++){
            if (sudoku[i][j] === 0){
                return false
            }
        }

    }
    return true

}


function sfill(sudoku){

    
    if (isFilled(sudoku)){
        return true
    }
    

    for (const ri of row){
        let x = Math.floor(ri/9)
        let y = ri%9


        if (sudoku[x][y] === 0){

        //console.log(ri) 
        let otn = [...Array(9).keys()].map(x => x+1)
        otn = shuffle(otn)
        console.log(otn)

        for (const i of otn){
             
            
           
            //console.log(x,y,row[ri])
            

            if (safe(sudoku,x,y,i)){
                sudoku[x][y] = i
                        
            //console.log(i,ri,x,y)
            console.log(ri)
            //print(sudoku)

                 
            if (sfill(sudoku)){
                return true
            }
            //console.log("ok")

            sudoku[x][y] = 0
        }


        }

        break;
    }
}

return false

}

sfill(sudoku,row)
console.log("done")
print(sudoku)
