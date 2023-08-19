var ApiManager = (function manager() {
   var modules = {};

   function define(name, args, impl) {
      for (let i = 0; i < args.length; i++) {
         args[i] = modules[args[i]];
      }
      modules[name] = impl.apply(impl, args);
   }
   function get(name) {
      return modules[name];
   }

   return {
      define: define,
      get: get,
   };
})();

ApiManager.define("bar", [], function () {
   function sayhello(who) {
      return "HELLO ITS "+who;
   }

   return {
      sayhello: sayhello,
   };
});

ApiManager.define("foo", ["bar"], function (bar) {
   let survival = "7D2D";
   function survivalGame() {
      console.log(survival, bar.sayhello('peter'));
   }
   return {
      survivalGame: survivalGame,
   };
});


export ApiManager