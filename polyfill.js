var foo = (function CoolModule(id) {
   function identify1() {
      console.log(id);
   }
   function identify2() {
      console.log(id.toUpperCase());
   }
   function change() {
      publicApi.identity = identify2;
   }

   var publicApi = {
      identity: identify1,
      change: change,
   };
   return publicApi
})("foo module");

foo.identity()
foo.change()
foo.identity()
