class Parent {
    static sayHello() {
        return "Hello from Isabella";
    }
}

class Child extends parent {
    static sayHello() {
        return
        super.sayHello() + "and hello from Bob";
        // Calls the parent class static method
    }
}

console.log(Child.sayHello());
// Hello from Isabella and hello from Bob