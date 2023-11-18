# dice.py
import random
import tomllib
import pathlib

DICE_ART_PATH = pathlib.Path(__file__).parent / "pyproject.toml"
DICE_ART = tomllib.loads(DICE_ART_PATH.read_text())["DICE_ART"]["faces"]
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "

def main():
    num_dice_input = input("How many dice do you want to roll? [1-6] ")
    dice_to_roll = parse_input(num_dice_input)
    # 2. Roll the dice
    roll_results = roll_dice(dice_to_roll)
    assemble_art = roll_art(roll_results)
    roll_art_display(assemble_art)


def parse_input(input_string):
    """Return `input_string` as an integer between 1 and 6.

    Check if `input_string` is an integer number between 1 and 6.
    If so, return an integer with the same value. Otherwise, tell
    the user to enter a valid number and quit the program.
    """
    if input_string.strip() in {"1", "2", "3", "4", "5", "6"}:
        return int(input_string)
    else:
        print("Please enter a number from 1 to 6.")
        raise SystemExit(1)


def roll_dice(num_dice):
    """
    Simulates the rolling of between one and six inclusive six-sided dice.

    Parameters:
    - num_dice (int): The number of dice to roll.

    Returns:
    - list: A list containing the results of rolling each die. Each result is an integer
            between 1 and 6 (inclusive), representing the face of the die.

    Example:
    >>> roll_dice(3)
    [4, 2, 6]
    """

    return [random.randint(0, 5) for _ in range(num_dice)]

def roll_art(roll_results):
    """
    Return the dice art corresponding to each index in roll_results:
    list of lists of strings
    """
    faces = [DICE_ART[face] for face in roll_results]

    # Generate a list containing the dice faces rows
    face_rows = []
    for row_idx in range(DIE_HEIGHT):
        row_components = [face[row_idx] for face in faces]
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        face_rows.append(row_string)

    return face_rows

def roll_art_display(face_rows):
    # Generate header with the word "RESULTS" centered
    width = len(face_rows[0])
    diagram_header = " RESULTS ".center(width, "~")

    dice_faces_diagram = "\n".join([diagram_header] + face_rows)
    print(dice_faces_diagram)

if __name__ == '__main__':
    main()
