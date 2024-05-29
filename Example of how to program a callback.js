//function that accepts a call back
function greet(name, callback) {
    console.log("Hello" + name);
    callback();
}

//Callback function
function sayGoodbye() {
    console.log('goodbye!');
}

//Using the callback
greet('Thomas', sayGoodbye);