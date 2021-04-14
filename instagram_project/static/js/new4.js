let tu=document.querySelector('.tu')
let head=document.querySelector(".head")

let a=document.querySelector(".content")
let b=document.querySelector('.sd')
console.log(a,b)
console.log(a.offsetHeight,b.offsetHeight)
head.style.height ="48px";

a.style.height =(100/100)*(b.offsetHeight-170).toString()+"px";
// tu.style.height =(10/100)*(b.offsetHeight-34).toString()+"px";

console.log(a.offsetHeight)



let button=document.querySelector(".ffff")
let container = document.querySelector('.dd');