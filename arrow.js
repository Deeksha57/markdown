function add() {
    a=10;
    b=19;
    return a+b;
}
x= add();
console.log(x);

add = ()=>{
    var a=10;
    var b=20;
    return a-b;
}
console.log(typeof(add()));

display= (
function(){
    var a=10;
    var b=20;
    return a-b;
}
)();
console.log(display);

function* generator(i){
    for(i=0;i<10;i++)
    yield i;
   
}
var gen = generator(10);
console.log(gen.next().value);
