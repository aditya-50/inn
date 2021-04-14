let tu=document.querySelector('.tu')
let head=document.querySelector(".head")

let a=document.querySelector(".content")
let b=document.querySelector('.sd')
console.log(a,b)
console.log(a.offsetHeight,b.offsetHeight)
a.style.height =(85/100)*(b.offsetHeight).toString()+"px";
tu.style.height =(15/100)*(b.offsetHeight).toString()+"px";

console.log(a.offsetHeight)



let button=document.querySelector(".ffff")
let container = document.querySelector('.dd');
