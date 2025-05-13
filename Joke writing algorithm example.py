import random

# Joke Templates
joke_templates = [
    "Why did the {animal} cross the road? To get to the {place}!",
    "I told my {relation} To stop acting like a {noun} but they said it was their{adjective} nature.",
    "Why don't {plural_noun} ever win at poker? Because they always {verb}!",
    "I asked my {profession} if I could get a discount. They said, 'Only if you {verb}!'",
    "What's the difference between a {animal} and a {profession}? One has fur, The other just makes you pay through the nose!"]

# Word lists
animals = ["Chicken", "penguin", "elephant", "monkey", "dog", "cat"],
places = ["library", "moon", "gym", "speakeasy", "kitchen"],
relations = ["dad", "aunt", "cousin", "brother", "grandpa"],
nouns = ["blender", "tulip", "scooter", "banana", "evil robots"],
adjectives = ["weird", "chaotic", "magnetic", "fancy", "invisible"],
plural_nouns = ["ghosts", "lawyers", "dinosaurs", "pigeons", "clowns"],
verbs = ["fold", "bluff", "run", "sneeze", "code"],
professions = ["carpenter", "dentist", "programmer", "lawyer", "barista"]

def generate_joke():
    template= random.choice(joke_templates)
    joke = template.format(
        animal=random.choice(animals),
        place=random.choice(places),
        relation=random.choice(relations),
        noun=random.choice(nouns),
        adjective=random.choice(adjectives),
        plural_noun=random.choice(plural_nouns),
        verb=random.choice(verbs),
        profession=random.choice(professions))
    return joke

if __name__ == "__main__":
    for _ in range(5):
        print(generate_joke())