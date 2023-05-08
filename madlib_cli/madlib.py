import re

def read_template(file_path):
    """
    Reads the contents of a file located at the given file path.
    Returns the contents of the file as a stripped string.
    """
    print('''
             Welcome to the MadLibs game! In this game, you'll have the opportunity to create hilarious and wacky stories 
             by filling in the blanks with various parts of speech.
             To get started, we'll provide you with a story template that has several blanks.
             You'll need to come up with words that match the parts of speech requested in the blanks.
             Once you've filled in all the blanks, we'll merge your words with the template to create a completely
             original story then compare it with original story text!
             Are you ready to get started? Let's play MadLibs!


             Here is the template:-

             Make Me A Video Game!
             I the "1" and "2" "3" have "4" "5" "6" sister and plan to steal her "7" "8"!
             What are a "9" and backpacking "10" to do? Before you can help "11", you'll have 
             to collect the "12" "13" and "14" "15" that open up the "16" worlds connected to A "17"'s Lair.
             There are "18" "19" and "20" "21" in the game, along with hundreds of other goodies for you to find.


             Notice that you need to enter 21 inputs to complete the game !!!




          ''')
    try:
        with open(file_path) as file:
            return file.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"No such file or directory: {file_path}")


def parse_template(text):
    """
    Takes a template string as input and returns a tuple containing two elements:
    1. A string with the language parts removed.
    2. A tuple of the language parts.
    """
    variables = re.findall(r"{([^}]+)}", text)
    template_without_variables = re.sub(r"{[^}]+}", "{}", text)

    return template_without_variables, tuple(variables)


def merge(text, parts):
    """
    Takes a "bare" template string and a list of user entered language parts,
    and returns a string with the language parts inserted into the template.
    """
    return text.format(*parts)


def get_user_inputs(language_parts):
    """
    Takes a tuple of language parts as input and prompts the user to enter values for each part.
    Returns a list of user entered values in the same order as the original tuple.
    """
    user_inputs = []
    for part in language_parts:
        user_input = input(f"Enter a {part}: ")
        user_inputs.append(user_input)
    return user_inputs


def write_madlib(madlib, file_path):
    """
    Takes a completed madlib and writes it to a file located at the given file path.
    """
    try:
        with open(file_path, "w") as file:
            file.write(madlib)
    except:
        raise Exception("Could not write to file")
    

def compare_files(generated_filename, original_filename):
    with open(generated_filename, "r") as generated_file:
        generated_text = generated_file.read()
    with open(original_filename, "r") as original_file:
        original_text = original_file.read()

    if generated_text.strip() == original_text.strip():
        print()
        print("Congratulations! The generated MadLibs game matches the original.")
        return True
    else:
        print()
        print("Sorry, the generated MadLibs game does not match the original. Try again")
        return False


if __name__ == "__main__":
    template_path = "../assets/madlib.txt"
    original_filename = "../assets/completed_text.txt"

    # Read the template file
    template = read_template(template_path)

    # Parse the template
    template_without_language_parts, language_parts = parse_template(template)

    # Get user inputs for the language parts
    user_inputs = get_user_inputs(language_parts)

    # Merge the template and user inputs
    completed_madlib = merge(template_without_language_parts, user_inputs)
    print(completed_madlib)

    # Write the completed madlib to a file
    write_madlib(completed_madlib, "completed_text.txt")

    # Compare the generated madlib to the original
    compare_files("completed_text.txt", original_filename)

