  function checkSet(arrToBeSet, checkValue){
     let result = [];
     // Only change code below this line
     if(new Set(arrToBeSet).has(checkValue)){
        result.push(true);
     }
     else{
        result.push(false);
     }
     result.push(new Set(arrToBeSet).size);

     return result;

     // Only change code above this line

  }

