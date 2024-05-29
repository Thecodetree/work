class Parent {
    constructor(name) {
        this.name = name;
    }
}

class Child extends parent {
    constructor(name, age, profession) {
        super(name);
        /*Calls the parent class 
        constructor*/

        this.age = age;

        this.profession = profession;
    }
}

const childInstance = new Child("Tom", 38, Teacher);
console.log(childInstance.name);
//Tom
console.log(childInstance.age);
//38
console.log(childInstance.profession);
//Teacher