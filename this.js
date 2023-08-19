"use strict";
function uchiha() {
    console.log(this.susano);
}

var sasuke = {
    susano: "blue",
    uchiha: uchiha,
};
var itachi = {
    susano: "pink",
    uchiha: uchiha,
};
var shisui = {
    susano: "purple",
};

sasuke.uchiha();
itachi.uchiha();
uchiha.call(shisui);
