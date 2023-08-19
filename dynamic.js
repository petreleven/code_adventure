var obj = {
   a: "awesome",
   b: function cool() {
      console.log(this.a);
   },
};

var a = "not awesome";

setTimeout(obj.b,100)
