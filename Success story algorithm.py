import random

# Character and setting

male_names = ["Steven", "John", "James", "Stewart"]
female_names = ["Emma", "Ruth", "Bebe", "Jane", "Sue"]
locations = ["Small town America", "East Coast by the sea"]
Professions = ["Doctor", "Writer", "Carpenter", "Book shop owner"]
Conflicts = ["Steven & John Rivalry over Ruth", "Sue has a painful past",
            "James & Stewart once best friends but have a misunderstanding over Sue"]

Reunions = ["Steven & John develop a friendship at Ruth's Wedding",
            "James & Stewart reunite at Sue's funeral"]

Endings = ["Steven is John's best man at his wedding", 
        "James & Stewart open a chain of successful book stores"]

def generate_Success_story():
    male_name = random.choice(male_names)
    female_name = random.choice(female_names)
    setting = random.choice(locations)
    profession1 = random.choice(Professions)
    profession2 = random.choice([p for p in Professions if p != profession1])
    Conflict = random.choice(Conflicts)
    Reunion = random.choice(Reunions)
    Ending = random.choice(Endings)

story = f"""
Title: Success in the {setting.title()}

In a {setting}, {female_name}, a passionate {profession1},
crosses paths with {male_name}, a witty {profession2}.
sparks fly immediately but {conflict}. Friends reunite at {reunion}.
through witty banter a common bond {ending}.
"""

if __name__ == "__main__":
    print(generate_Success_story())