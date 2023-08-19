"use strict";
function varScope() {
   var x = 1;
   if (true) {
      var x = 2;
      console.log(x);
   }
   console.log(x);
}

function letScope() {
   let x = 1;
   if (true) {
      let x = 2;
      console.log(x);
   }
   console.log(x);
}
var x = 0;
let y = 1;
console.log(x);
console.log(y);
