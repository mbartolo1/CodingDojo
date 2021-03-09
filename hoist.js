
// 1 given :
console.log(hello);
var hello = 'word';
// prediction - prints out world;
// console is undefined.


// 1 fixed:
// var hello = 'world';
// console.log(hello);

//2: given 
var needle = 'haystack';
Test();
function Test(){
    var needle = 'magnet';
    console.log(needle);
}
// prediction - undefined since needle is outside function 
// prints out "magnet"

//2: fixed
// function test(){
// let needle = 'haystack';
// var needle = 'magnet';
// }
// console.log(test(needle));

//3 given: 
var brendan = 'super cool';
function print(){
    brendan = 'only okay';
    console.log(brendan);
}
console.log(brendan);

// prediction: prints out "only okay" and "supercool";
// prints out 'supercool' only and undefined.
// let brendan = 'super cool';
// console.log(brendan);
// function print(){
//     var brendan = 'only okay'
//     console.log(brendan)

// }
// return print; 

//4 given:
var food = 'chicken';
console.log(food);
eat();
function eat(){
    food = 'half-chicken';
    console.log(food);
    var food = 'gone';
}

// prediction: prints chicken and half-chicken
// prints : chicken & half chicke, then undefined.

//fixed: 
// let food = 'chicken';
// console.log(food);
// const eat(){
//     var food = 'half chicken ';
//     console.log(food);
//     var food = 'gone';
//     console.log(food);
// }


//5 given:
mean ();
console.log(food);
var mean = function(){
    food = "chicken";
    console.log(food);
    var food = "fish";
    console.log(food);
}
console.log(food);
// prediction: prints undefined, chicken, and fish;
// returns : unexpected identifer

//5 fixed:
// function mean(){
//     let food = 'chicken';
//     console.log(food); 
//     var food = 'fish';
//     console.log(food);
// }
// return mean;

//6 given:
console.log(genre);
var genre = "disco";
rewind();
function rewind() {
    genre = "rock";
    console.log(genre);
    var genre = "r&b";
    console.log(genre);
}
console.log(genre);
// prediction: prints genre, disco, rock, and r&b;
//prints: undefinded, rock, r&b, disco, and undefined.

// 6 fixed:
// rewind();
// function rewind (){
//     let genre = 'disco';
//     console.log(genre);
//     let genre = 'rock';
//     console.log(genre);
//     let genre = 'r&b';
//     console.log(genre);
// }

//7 given: 
dojo = "san jose";
console.log(dojo);
learn();
function learn() {
    dojo = "seattle";
    console.log(dojo);
    var dojo = "burbank";
    console.log(dojo);
}
console.log(dojo);
//prediction: prints sanjose, seattle, burbank, and undefined.
//prints: -correct;
