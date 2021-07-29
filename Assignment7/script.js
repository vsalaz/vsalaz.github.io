// PART A

let c=0;
let f=68;
let fahrenheittoC = (5/9) * (f - 32);
let celsiustoF = (c * 9/5) + 32;
console.log(`${c}°C is ${celsiustoF}°F `);
console.log(`${f}°F is ${fahrenheittoC}°C `);


// PART B
const massLucas=78;
const heightLucas=1.69;

const massJohn=95;
const heightJohn=1.88;

const BMILucas= massLucas/heightLucas**2;
const BMIJohn= massJohn/(heightJohn*heightJohn);
const lucasHigherBMI = BMILucas > BMIJohn;

if(BMILucas>BMIJohn){
    console.log(`Lucas's BMI ${BMILucas} is higher than John's!${BMIJohn}`);
}
else{
    console.log(`John's BMI ${BMIJohn} is higher than Lucas's!${BMILucas}`);
}

// PART C
// Test data:
// Data 1: Nets score 96, 108 and 89. Knicks score 88, 91 and 110
// Data Bonus 1: Nets score 97, 112 and 101. Knicks score 109, 95 and 123
// Data Bonus 2: Nets score 97, 112 and 101. Knicks score 109, 95 and 106

let netsScore = 96 + 108 + 89;
let netsAverage = netsScore / 3;
let knicksScore = 88 + 91 + 110;
let knicksAverage = knicksScore/3;

// console.log(netsAverage==knicksAverage);

if(knicksAverage>netsAverage){
    console.log(`The Knicks average score ${knicksAverage}, is higher than The Nets ${netsAverage} average score! The Knicks Win!`); 
}
else{
    console.log(`The Nets average score ${netsAverage} is higher than The Knicks ${knicksAverage} average score! The Nets Win!`); 
}

let netsScore2 = 97 + 112 + 101;
let netsAverage2 = netsScore2 / 3;
let knicksScore2 = 109 + 95 + 123;
let knicksAverage2 = knicksScore2 / 3;

// console.log(netsAverage2);
// console.log(knicksAverage2);


if(netsAverage2>=100 && netsAverage2>knicksAverage2){
    console.log(`The Net combined score of ${netsAverage2} is higher than 100! The Nets win!`);
}

else if(knicksAverage2>=100 && knicksAverage2>netsAverage2){
    console.log(`The Knicks combined score of ${knicksAverage2} is higher than 100! The Knicks win!`); 
}
else{
    console.log(`No Team wins!`)
}

let netsScore3 = 97 + 112 + 101;
let netsAverage3 = netsScore3 / 3;
let knicksScore3 = 109 + 95 + 106;
let knicksAverage3 = knicksScore3 / 3;

if(netsAverage3>=100 && netsAverage3>knicksAverage3){
    console.log(`The Net combined score of ${netsAverage3} is higher than 100! The Nets win!`)
}
else if(knicksAverage3>=100 && knicksAverage3>netsAverage3){
    console.log(`The Knicks combined score of ${knicksAverage3} is higher than 100! The Knicks win!`);
}
else if (netsAverage3==knicksAverage3){
    console.log(`The Knicks combined score of ${knicksAverage3} and The Nets combined score ${netsAverage3} are equal!. Its a draw!`);
}
else{
    console.log(`No team Wins!`)
}