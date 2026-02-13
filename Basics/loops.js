// while loop
let i = 0;
while(i<10){
    console.log(i);
    i++;
}

//for loop
for(i=0;i<10;i++){
    console.log("Iteration :"+i)
}

//do while loop
let j = 0;
do{
    console.log("Value of j: "+j);
    j++; 
}while(j<10)

//switch case
let day = 7;
switch(day){
    case 1:
        console.log("Monday");
        break;
    case 2:
        console.log("Tuesday");
        break;
    case 3:
        console.log("Wednesday");
        break;
    case 4:
        console.log("Thursday");
        break;
    case 5:
        console.log("Friday");
        break;
    case 6:
        console.log("Saturday");
        break;
    case 7:
        console.log("Sunday");
        break;
    default:
        console.log("Invalid day");
}

//if else
let age= 18;
if(age>=18){
    console.log("You are an adult.");
}else{
    console.log("You are a minor.");
}

//nested if else
let score = 85;
if(score >= 90){
    console.log("Grade: A");
}else if(score >= 80){
    console.log("Grade: B");
}else if(score >= 70){
    console.log("Grade: C");
}else if(score >= 60){
    console.log("Grade: D");
}else{
    console.log("Grade: F");
}

//functions
function greet(name){
    console.log("Hello, "+name);
}
greet("Gowtham");

