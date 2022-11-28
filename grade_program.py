#!/usr/bin/env python3
# Created by: Lia Duggan
# Created on: Nov.28th, 2022
# This program takes a grade level and returns the middle percentage mark


def calc_mark(user_level):

    # Selecting the grade percentage based on the user's grade level.
    if user_level == "1-":
        grade_percentage = "51%"
    elif user_level == "1":
        grade_percentage = "54.5%"
    elif user_level == "1+":
        grade_percentage = "58%"
    elif user_level == "2-":
        grade_percentage = "61%"
    elif user_level == "2":
        grade_percentage = "64.5%"
    elif user_level == "2+":
        grade_percentage = "68%"
    elif user_level == "3-":
        grade_percentage = "71%"
    elif user_level == "3":
        grade_percentage = "74.5%"
    elif user_level == "3+":
        grade_percentage = "78%"
    elif user_level == "4-":
        grade_percentage = "83%"
    elif user_level == "4":
        grade_percentage = "90.5%"
    elif user_level == " 4+":
        grade_percentage = "97.5%"
    else:
        return -1

    return grade_percentage


def main():

    # Getting the user's grade level
    user_level = input("Input your grade: ")

    # Call the function to convert the user level to a percentage
    user_mark = calc_mark(user_level)

    # Checking for invalid input
    if user_mark == -1:
        print("Please input a valid grade level")

    # Displaying the middle mark to the user
    else:
        print("{} has a middle percentage of {}".format(user_level, user_mark))


if __name__ == "__main__":
    main()
