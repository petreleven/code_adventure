var obj = {
   a: "awesome",
   cool: function cool() {
      console.log(this.a);
   },
};

var a = "not awesome";
obj.cool()
setTimeout(obj.cool, 100);
