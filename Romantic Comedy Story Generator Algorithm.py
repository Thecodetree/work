import random

first_names = ["Stacy", "Paul", "George", "Beatrix", "stanley"]
last_names = ["Benz", "Reagan", "Stein", "Sax", "Sweeney"]

def generate_character():
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    trait = random.choice(["clumsy", "Goofy", "Witty", "Charming", "Introverted", "Extroverted"])
    job = random.choice(["baker", "Scientist", "Architect", "Bookstore owner", "influencer", "Actor"])
    return {"name": name, "trait": trait, "job": job}

# Plot
meet_cutes = [
    "Accidentally swapped phones at a coffee shop",
    "ran into each other during a failed blind date",
    "fought over the last avocado at the grocery store",
    "were handcuffed together in an escape room",
    "mistakenly booked the same airbnb during a snowstorm"]

conflicts = [
    "One has to move across the country for a job",
    "A jealous ex shows up unexpectedly",
    "They discover they're rival small business owners",
    "A lie told spirals out of control",
    "One is not who they said they were",]

climaxes = [
    "a big romantic gesture at the airport",
    "a public confession at a karaoke bar",
    "A unexpected reunion during a thunderstorm",
    "a flash mob proposal during a festival",
    "a heartfelt letter delivered by a favorite dog"]

resolutions = [
    "They open a bistro together",
    "They move in and adopt a weiner dog",
    "They publish a romantic comedy based on their love story",
    "They get married at a lakeside chateau",
    "They start a youtube channel together"]

def generate_romantic_comedy_story():
    protagonist = generate_character
    love_interest = generate_character
    
    while love_interest["name"] == protagonist["name"]:
        love_interest = generate_character
        
    if __name__ =="--main__":
        print(generate_romantic_comedy_story)