def get_input():
    print("Welcome to Mad Libs!")
    adjective1 = input("Enter the adjective1: ")
    noun1 = input("Enter the noun1: ")
    name1 = input("Enter the name: ")
    verb1 = input("Enter the verb1: ")
    adjective2 = input("Enter the adjective2: ")
    noun2 = input("Enter the noun2: ")
    verb2 = input("Enter the verb2: ")

    return {
        "adjective1": adjective1,
        "noun1": noun1,
        "name1": name1,
        "verb1": verb1,
        "adjective2": adjective2,
        "noun2": noun2,
        "verb2": verb2
    }


def create(template, replacements):
    story = template
    for key, value in replacements.items():
        placeholder = f"[{key}]"
        story = story.replace(placeholder, value)
    return story


def main():
    story_template = """Once upon a time, in a [adjective1] land, there was a [noun1] named [name1].
    [name1] loved to [verb1] every day. One day, [name1] met a [adjective2] [noun2] who wanted to [verb2] with them.
    """

    user_inputs = get_input()
    final_story = create(story_template, user_inputs)

    print("\nHere's your Mad Libs story!")
    print(final_story)


if __name__ == "__main__":
    main()
