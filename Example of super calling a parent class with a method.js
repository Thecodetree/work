class Parent {
    greet() {
        return "Hello Cole";
    }
}

class Child extends Parent {
    greet() {
        return
        super.greet() + "and hello from John";
        // Calls the parent class method
    }
}

const childInstance = new Child();
console.log(childInstance.greet());
// Hello from Cole and hello from John