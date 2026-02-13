const words = ["MERN Stack Developer","Full Stack Web Developer","Information Science Engineer","Software Developer" ];
let i=0,j=0,current="",deleting=false;

function type(){
    current = words[i];
    document.getElementById("typing").textContent = current.substring(0,j);

    if(!deleting && j<current.length){ j++; setTimeout(type,100); }
    else if(deleting && j>0){ j--; setTimeout(type,50); }
    else{
        deleting=!deleting;
        if(!deleting) i=(i+1)%words.length;
        setTimeout(type,1000);
    }
}
type();

function reveal(){
    document.querySelectorAll(".reveal").forEach(el=>{
        if(el.getBoundingClientRect().top < window.innerHeight-100){
            el.classList.add("active");
        }
    });
}
window.addEventListener("scroll",reveal);
window.addEventListener("load",reveal);

window.addEventListener("scroll",()=>{
    const nav=document.getElementById("navbar");
    nav.classList.toggle("scrolled",window.scrollY>50);
});
