function createMatchUp(challenger) {
   var hokage = ["uzumaki", "kakashi", "tsunade", "minato"];
   function getOpponents() {
      let chosenAiCharacter = chooseAichallenger();
      return chosenAiCharacter + " Vs " + challenger;
   }

   function chooseAichallenger() {
      let index = Math.floor(Math.random() * (hokage.length));
      return hokage[index];
   }
   return getOpponents()
}

module.exports = {createMatchUp}