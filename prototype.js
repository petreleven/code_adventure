var baseUchiha = {
    susano: "susanoo",
    sharingan: "sharingan",
};

var baseShinobi = {
    ninjutsu: "ninjutsu",
    natureelement: "",
};


var sasuke = Object.create(baseShinobi)
sasuke.natureelement = "lightning"
console.log(sasuke.natureelement)
console.log(sasuke.ninjutsu)
