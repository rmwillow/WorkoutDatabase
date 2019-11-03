from random import choices

from exercisesApi import exerciseList, tempList



generateWorkout = exerciseList
customizeWorkout = tempList


def print_choice(generateWorkout, customizeWorkout):
    """ This function prints the choices """
    print(generateWorkout + "Generate workout " + customizeWorkout + " Custom workout")

choices['generateWorkout', 'customizeWorkout']
if generateWorkout():
    print(exerciseList)
else:
    print(tempList)

# calling the function
print_choice(customizeWorkout='2)', generateWorkout='1)')
