import random

# definition of key components in suspense story
themes = ["betrayal", "revenge", "hidden identity", "cover-up", "cold case", "obsession"]
settings = ["abandoned mansion", "foggy town", "remote island", "urban alleyway", "crumbling asylum"]
protagonists = ["disgraced detective", "reluctant journalist", "troubled teenager", "former spy"]
antagonists = ["serial killer", "corrupt official", "unknown stalker", "vengeful ghost", "double agent"]
twists = [
    "The protagonist is actually the villain.",
    "The murder is staged",
    "A key ally was lying the whole time.",
    "The antagonist is a family member.",
    "There is no crime at all."]

# Function to create rising tension
def generate_chapter_tension(chapter_num, total_chapters):
    base_tension = chapter_num / total_chapters
    variability = random.uniform(-0.1, 0.2)
    return round (min(0.1, base_tension + variability), 2)

# Function to create plot line
def generate_plot_outline(num_chapters=10):
    plot = []
    
# The setup
    theme = random.choice(themes)
    setting = random.choice(settings)
    protagonist = random.choice(protagonists)
    antagonist = random.choice(antagonists)
    
    plot.append(f"Title: 'Shadows in the {setting.title()}'")
    plot.append(f"Theme: {theme}")
    plot.append(f"Setting: {setting}")
    plot.append(f"Protagonist: A {protagonist}")
    plot.append(f"Antagonist: A mysterious {antagonist}\n")
    plot.append(f"Chapter outline:\n")

    # chapter events

    for Chapter in range(1, num_chapters + 1):
        tension = generate_chapter_tension(Chapter, num_chapters)
        if Chapter == 1:
            event = f"Ch. {Chapter}: The {protagonist} discovers something odd in the {setting}."
        elif Chapter == num_chapters:
            twist = random.choice(twists)
            event = f"Ch. {Chapter}: The final confrontation occurs. {twist} Resolution follows."
        else: event_type = random.choice([
            "A clue is found",
            "someone vanishes",
            "a chase occurs",
            "a betrayal happens",
            "the protagonist questions their sanity",
            "a shocking secret is revealed"])
        
        event = f"Ch. {Chapter}: Tension level {tension}. an event {event_type}."
        plot.append(event)
        return "\n".join(plot)
    
    if __name__ == "__main__":
        suspense_novel = generate_plot_outline(12)
        print(suspense_novel)