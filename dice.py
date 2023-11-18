"""
dice.py - A simple command-line dice rolling app with ASCII art representation.

This module provides functionality for simulating the rolling of six-sided
dice and displaying
corresponding ASCII art for each die face.

Module Dependencies:
- random: Provides random number generation for dice rolling.
- tomllib: Custom library for loading and parsing data from TOML files.
- pathlib: Provides an object-oriented interface for file system paths.

Module Constants:
- DICE_ART_PATH (pathlib.Path): The path to the TOML file containing ASCII
art for dice faces.
- DICE_ART (list): List of lists representing ASCII art for each die face.
- DIE_HEIGHT (int): The height of each die face in rows.
- DIE_WIDTH (int): The width of each die face in columns.
- DIE_FACE_SEPARATOR (str): Separator used when combining rows of
multiple dice faces.

Module Functions:
- main(): The main entry point for the dice rolling application.
- parse_input(input_string: str) -> int: Parses user input into an integer
between 1 and 6.
- roll_dice(num_dice: int) -> list: Simulates rolling between one and six
inclusive six-sided dice.
- roll_art(roll_results: list) -> list: Returns the dice art corresponding to
each index in roll_results.
- roll_art_display(face_rows: list): Displays the ASCII art representation of
the rolled dice faces.
"""

import random
import tomllib
import pathlib

DICE_ART_PATH = pathlib.Path(__file__).parent / "pyproject.toml"
DICE_ART = tomllib.loads(DICE_ART_PATH.read_text())["DICE_ART"]["faces"]
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "


def main():
    """
    The main entry point for the dice rolling application.

    Prompts the user for the number of dice to roll, rolls the dice,
    and displays the corresponding ASCII art for the rolled dice faces.
    """
    num_dice_input = input("How many dice do you want to roll? [1-6] ")
    dice_to_roll = parse_input(num_dice_input)
    roll_results = roll_dice(dice_to_roll)
    assemble_art = roll_art(roll_results)
    roll_art_display(assemble_art)


def parse_input(input_string):
    """
    Return `input_string` as an integer between 1 and 6.

    Check if `input_string` is an integer number between 1 and 6.
    If so, return an integer with the same value. Otherwise, tell
    the user to enter a valid number and quit the program.

    Parameters:
    - input_string (str): User input as a string.

    Returns:
    - int: The parsed integer value.

    Raises:
    - SystemExit: If the input is not a valid number between 1 and 6.
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
    - list: A list containing the results of rolling each die. Each result is
    an integer between 1 and 6 (inclusive), representing the face of the die.

    Example:
    >>> roll_dice(3)
    [4, 2, 6]
    """
    return [random.randint(0, 5) for _ in range(num_dice)]


def roll_art(roll_results):
    """
    Return the dice art corresponding to each index in roll_results:
    list of lists of strings.

    Parameters:
    - roll_results (list): List of integers representing the results
    of rolling dice.

    Returns:
    - list: List of strings representing the ASCII art for the rolled
    dice faces.
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
    """
    Displays the ASCII art representation of the rolled dice faces.

    Parameters:
    - face_rows (list): List of strings representing the ASCII art for
    the rolled dice faces.
    """
    width = len(face_rows[0])
    diagram_header = " RESULTS ".center(width, "~")

    dice_faces_diagram = "\n".join([diagram_header] + face_rows)
    print(dice_faces_diagram)


if __name__ == "__main__":
    main()
