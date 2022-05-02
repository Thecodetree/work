const ComputerChoiceDisplay = document.getElementById("Computer Choice")
const UserChoiceDisplay = document.getElementById("User Choice")
const ResultDisplay = document.getElementById("Result")
const possibleChoices = document.querySelectorAll('button')
let UserChoice
let ComputerChoice
let Result

possibleChoices.forEach(possibleChoice => possibleChoice.addEventListener('click', (e) => {
UserChoice = e.target.id
UserChoiceDisplay.innerHTML = UserChoice
generateComputerChoice()
getResult()
}))

function generateComputerChoice() {
    const randomNumber = Math.floor(Math.random() * 3) + 1 //or you can use possible choices.length
   
    if (randomNumber === 1) {
        ComputerChoice = "rock"
    }
    if (randomNumber === 2) {
        ComputerChoice = "paper"
    }
    if (randomNumber === 3) {
        ComputerChoice = "scissors"
    }
    ComputerChoiceDisplay.innerHTML = ComputerChoice
}

function getResult( ) {
    if (ComputerChoice === UserChoice) {
        Result = 'Its a draw!'
    }
    if (ComputerChoice === 'rock' && UserChoice === "paper") {
        Result = 'You win!'
}
    if (ComputerChoice === 'rock' && UserChoice === "scissors") {
        Result = 'You lose!'
}
    if (ComputerChoice === 'paper' && UserChoice === "scissors") {
        Result = 'You win!'
}
    if (ComputerChoice === 'paper' && UserChoice === "rock") {
        Result = 'You lose!'
}
    if (ComputerChoice === 'scissors' && UserChoice === "rock") {
        Result = 'You win!'
}
        if (ComputerChoice === 'scissors' && UserChoice === "paper") {
            Result = 'You lose!'
    }
    ResultDisplay.innerHTML = Result
}