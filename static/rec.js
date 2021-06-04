


for (let i = 0; i< 81; i+=9){
    let b = i
    let arr = []
    for (let j = 0; j < 9; j++){
        let t = b+j
        arr.push(t);
    }
    console.log(...arr)



    
}


function a1(v){
    
    function a2(){
        var temp = 0
        console.log(temp)
    }
   

    function a3(){
        console.log(temp)
    }
    return a3

}

let tv = a1(8)

console.log([...Array(9).keys()].map(x => ++x))  