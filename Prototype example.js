// constructor function

function
Person(firstName, lastName) {
    this.firstName = firstName;
     this.LastName = lastName;
}

Person.prototype.full-Name = function() {
    return this.firstName + " " + this.lastName;
};

let person1 = new Person("Alice", "Smith");

console.log(person1.fullName());