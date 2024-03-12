class colleague {
    constructor(name, title) {
        this.name = name;
        this.title = title;
    }

    speak() {console.log(`${this.name} speaks`);
    }

    introduce() {console.log(`Hi my name is ${this.name} 
    and I am a ${this.title} at Illinois Industries `);
    }
}