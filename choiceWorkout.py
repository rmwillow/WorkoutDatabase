# from random import choice
# from myQueries import Users_Table
from database import DataBase

from exercisesApi import *

# import password as password
# import username


data_base = DataBase()


def generate_choices(choices):
    """
    :param choices: list containing two strings new workout and existing workout
    :return: appends choices to a number and value and joins it to choice_result
    """
    choices_result = []
    for number, value in enumerate(choices):
        choices_result.append(f'\n{number}) {value}')
    return ''.join(choices_result)

def show_exercise_options(userId, exercise_options):
    """
    :param exercise_options: generate choices with exercise option
    :return: displays input and allows input with generate choices and exercise options as the choices
    """
    return input(f" What is your Muscle choice, If mulitiple use a comma to add Multiple Muscle Groups"
                 f"  (EX: 1, 2  Displays: abdominals, adductors \n{generate_choices(exercise_options)}\n\n"
                 f" Select a exercise by Muscle Group:")


def new_work_out(userId):
    selected_workout = input(f"What is the name of your workout: ")
    data_base.Workout_Table_insert(selected_workout)
    workoutId = data_base.search_by_workout(selected_workout)
    data_base.Users_Workout_Table_insert(userId, int(workoutId))

def existing_work_out(userId):
    pass


def show_workouts_options(userId):
    """
    Finds user a existing workout or creates new workout

    :return:
    """
    first_option = ['New Workout', 'Existing Workout']
    selectedMainMenu = input(
        f"Welcome\nPlease select an option \n{generate_choices(first_option)}\n\n What is your choice:")
    if int(selectedMainMenu) == 0:
        new_work_out(userId)
        show_muscle_options()
    if int(selectedMainMenu) == 1:
        existing_work_out(userId)






def show_muscle_options():
    muscle_options = data_base.display_all_muscles()
    selectedMuscleGroup = input(
        f"Select a Workout by Muscle Group\n{generate_choices(muscle_options)}\n\n What is your Muscle choice, "
        f"If mulitiple use a comma to add Multiple Muscle Groups "
        f"  (EX: 1, 2  Displays: abdominals, adductors:")
    if ',' in selectedMuscleGroup:
        exercise_options = []
    multiple_muscle_options = selectedMuscleGroup.split(',')
    for option in multiple_muscle_options:
        multiMuscleOptionList = []
    results = data_base.search_by_muscle(muscle_options[int(option)])
    for result in results:
        exercise_options.append(f'{result}- {muscle_options[int(option)]}')
    selectedExercises = show_exercise_options(exercise_options)
    if ',' in selectedExercises:
        exercise_options = []
    multiple_exercise_options = selectedExercises.split(',')
    for multiple in multiple_exercise_options:
        multiExerciseOptionList = []
    results = data_base.search_by_workout(exercise_options[int(multiple)])
    for result in results:
        multiExerciseOptionList.append(f'{result}- {exercise_options[int(multiple)]}')
    else:
        exercise_options = data_base.search_by_muscle(muscle_options[int(selectedMuscleGroup)])
        selectedExercises = show_exercise_options(exercise_options)
        exercise_id = data_base.search_by_exercise_id(exercise_options[int(selectedExercises)])
        data_base.Workout_Exercise_Table_insert(workoutId, exercise_id[0])



def orderOfStuff(userId):
    show_workouts_options(userId)




