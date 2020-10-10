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


def show_exercise_options(exercise_options):
    """
    :param exercise_options: generate choices with exercise option
    :return: displays input and allows input with generate choices and exercise options as the choices
    """

    return input(f"\n\n What is your Exercise choice, If multiple use a comma to separate values. "
                 f"  (EX: 1, 2  Displays: Lying Knee Curl, Goblet squat \n{generate_choices(exercise_options)}\n"
                 f" Select a exercise by Muscle Group:")

def show_existing_workout_options(workout_options):
    """
    :param exercise_options: generate choices with exercise option
    :return: displays input and allows input with generate choices and exercise options as the choices
    """

    return input(f"\n\n Please select existing workout options "
                 f"\n{generate_choices(workout_options)}\n"
                 f" Select a Workout:")


def new_work_out(userId):
    selected_workout = input(f"What is the name of your workout: ")
    data_base.Workout_Table_insert(selected_workout)
    workoutId = data_base.search_by_workout(selected_workout)
    data_base.Users_Workout_Table_insert(userId, int(workoutId))
    return workoutId


def existing_work_out(userId):
    userWorkouts = data_base.search_workout_by_userId(userId)
    display_workouts = [x['WorkoutName'] for x in userWorkouts]
    workout_choice = show_existing_workout_options(display_workouts)
    if display_workouts[int(workout_choice)] == userWorkouts[int(workout_choice)]['WorkoutName']:
        workoutId = userWorkouts[int(workout_choice)]['WorkoutID']
        results = data_base.search_by_workout_exercises(workoutId)
        print(generate_choices(results))


def show_workouts_options(userId):
    """
    Finds user a existing workout or creates new workout

    :return:
    """
    first_option = ['New Workout', 'Existing Workout']
    selectedMainMenu = input(
        f"Welcome\nPlease select an option \n{generate_choices(first_option)}\n\n What is your choice:")
    if int(selectedMainMenu) == 0:
        workoutId = new_work_out(userId)
        userExercisesIds = show_muscle_exercises_options()
        for exerciseid in userExercisesIds:
            data_base.Workout_Exercise_Table_insert(workoutId, exerciseid)
        

    elif int(selectedMainMenu) == 1:
        existing_work_out(userId)


def show_muscle_exercises_options():
    all_muscle_options = data_base.display_all_muscles()
    selectedMuscleGroup = input(
        f"Select a Workout by Muscle Group\n{generate_choices(all_muscle_options)}\n\n What is your Muscle choice, "
        f"If mulitiple use a comma to add Multiple Muscle Groups "
        f"  (EX: 1, 2  Displays: abdominals, adductors:")
    selected_muscle_options = selectedMuscleGroup.split(',')
    muscle_results_dict = {}
    for option in selected_muscle_options:
        muscle_results_dict[all_muscle_options[int(option)]] = data_base.search_by_muscle(
            all_muscle_options[int(option)])

    exercise_list = [
        {**{"Exercise_display": f"Exercise: {exercise_dict['ExerciseName']}\n   MuscleGroup:{key}\n"}, **exercise_dict}
        for key, list_exercise in muscle_results_dict.items()
        for exercise_dict in list_exercise]

    display_exercises = [x['Exercise_display'] for x in exercise_list]
    selectedExercises = show_exercise_options(display_exercises)

    multiple_exercise_options = selectedExercises.split(',')
    userExercisesIds = []
    for options in multiple_exercise_options:
        if display_exercises[int(options)] == exercise_list[int(options)]['Exercise_display']:
            userExercisesIds.append(exercise_list[int(options)]['ExerciseId'])

    return userExercisesIds


def orderOfStuff(userId):
    show_workouts_options(userId)
