# from .exercisesApi import exerciseList
import sqlite3

from exercisesApi import exerciseApiResults
import SqlQueries
import os

"""
Class — A blueprint created by a programmer for an object. 
This defines a set of attributes that will characterize any object that is instantiated from this class.

An object is created using the constructor of the class. This object will then be called the instance of the class. 
In Python we create instances in the following manner Instance = class(arguments)

Object — An Instance of a class. 
This is the realized version of the class, where the class is manifested in the program.

self represents the instance of the class.

"__init__"This method called when an object is created from the 
class and it allow the class to initialize the attributes of a class
"""


class DataBase(object):

    def __init__(self, restart=False):
        """
    
        :param restart: init calls on the data and restarts/refreshes it when it is set to True
        """

        if not os.path.isfile("tutorial.db"):
            restart = True

        self.connection = sqlite3.connect("tutorial.db")

        self.cursor = self.connection.cursor()

        """ if set to true and the data base restarts it will drop all of the following tables"""
        if restart:
            self.cursor.execute('DROP TABLE IF EXISTS Exercises')
            self.cursor.execute('DROP TABLE IF EXISTS Muscles')
            self.cursor.execute('DROP TABLE IF EXISTS Users')
            self.cursor.execute('DROP TABLE IF EXISTS Workout')
            self.cursor.execute('DROP TABLE IF EXISTS Users_Workout')
            self.cursor.execute('DROP TABLE IF EXISTS Workout_Exercise')
            self.cursor.execute('DROP TABLE IF EXISTS Previous_Workouts')

            self.cursor.execute(SqlQueries.exercises_table)
            self.cursor.execute(SqlQueries.muscles_table)
            self.cursor.execute(SqlQueries.Users_Table)
            self.cursor.execute(SqlQueries.Workout_Table)
            self.cursor.execute(SqlQueries.Users_Workout_Table)
            self.cursor.execute(SqlQueries.Workout_Exercise_Table)
            """after it has dropped the tables it is set to create the new tables above"""
            """it than trys and executes muscle table id index which we created in my 
            quieries.py using an input function of python called index. Index which 
            searches for a given element from the entire list and returns the lowest 
            index where the element appears, except/unless it already exists"""
            # try:
            #    self.cursor.execute(muscles_table_id_index)
            # except Exception as exception:
            #    print(exception)
            #    print('this index already exists')
            """ for muscle and exercises table in exerciseApiResults
             dictionary  it executes muscle_table_insert and inserts the value of muscle
             than it selects muscleId column from muscles table where muscle name equals to null.
             it than takes muscle id and uses fetchone which Fetches the next row in the list"""
            for muscle, exercises in exerciseApiResults.items():
                self.cursor.execute(SqlQueries.muscles_table_insert, [muscle])
                self.cursor.execute('select MuscleID from Muscles where MuscleName = ?', [muscle])
                muscleId = self.cursor.fetchone()[0]
                for exercise in exercises:
                    self.cursor.execute(SqlQueries.exercises_table_insert, [exercise, muscleId])

            self.cursor.execute(SqlQueries.exercises_table_update_muscleid)

            self.cursor.execute('DELETE FROM Muscles WHERE MuscleID = 19;')

            self.connection.commit()

    def __del__(self):
        self.connection.close()

    def close(self):
        self.connection.close()

    def search_by_muscle(self, muscle):
        """

        :param muscle:
        :return: the next row in the list of muscles
        """
        results = []
        self.cursor.execute(SqlQueries.search_by_muscle, [muscle])
        sql_results = self.cursor.fetchall()
        for row in sql_results:
            results.append(row[0])
        return results

    def search_by_exercise_id(self, exercise):
        """
        :param exercise: list of exercises
        :return: the next row in the list of exercises
        """
        results = []
        self.cursor.execute(SqlQueries.search_by_exercise_id, [exercise])
        sql_results = self.cursor.fetchall()
        for row in sql_results:
            results.append(row[0])
        return results

    def search_by_firstname(self, firstname):
        """

        :param firstname:
        :return: first name entered through user input
        """
        try:
            self.cursor.execute('select UsersId from Users where UsersFirstName = ?', [firstname])
            return self.cursor.fetchone()[0]
        except:
            return False

    def search_by_workout(self, workout):
        """

        :param workout:
        :return: workout entered though user data base newly or
        previously, than fetching it from the next row in the list
        """
        try:
            self.cursor.execute('select WorkoutID from Workout where WorkoutName = ?', [workout])
            return self.cursor.fetchone()[0]
        except:
            return False

    def add_user(self, firstname, lastname):
        """

        :param firstname:
        :param lastname:
        :return: firstName and Lastname from user input and
        inserts it into the database with user_table
        """
        self.cursor.execute(SqlQueries.Users_Table_insert, [firstname, lastname])
        self.connection.commit()

    def Workout_Table_insert(self, workoutName):
        """

        :param workoutName:
        :return: workoutname that was inputed by the user and inserts it into workout_table
        """
        self.cursor.execute(SqlQueries.Workout_Table_insert, [workoutName])
        self.connection.commit()

    def Previous_Table_Workouts_insert(self, existingWorkout, workoutId, MultipleSelection):
        """

        :param existingWorkout:
        :param workoutId:
        :param MultipleSelection:
        :return:
        """

        self.cursor.execute(SqlQueries.Previous_Table_Workouts_insert, [existingWorkout, workoutId, MultipleSelection])
        self.connection.commit()

    def Users_Workout_Table_insert(self, userId, workoutId):
        """

        :param userId:
        :param workoutId:
        :return:it inerts userId and workoutId into user_workout_table
        assigning it a number in order of input being entered
        """
        self.cursor.execute(SqlQueries.Users_Workout_Table_insert, [userId, workoutId])
        self.connection.commit()

    def Workout_Exercise_Table_insert(self, workoutId, exerciseId):
        """

        :param workoutId:
        :param exerciseId:
        :return: assigning workoutId and exerciseId into workout_exercise_table
        """
        self.cursor.execute(SqlQueries.Workout_Exercise_Table_insert, [workoutId, exerciseId])
        self.connection.commit()

    def search_by_Users_Exercises(self, firstname):
        """

        :param firstname:
        :return: Fetches the next row in the table of exercises,
        which is first name and appends the results to an empty list
        """
        results = []
        self.cursor.execute(SqlQueries.search_by_user_exercises, [firstname])
        sql_results = self.cursor.fetchall()
        for row in sql_results:
            results.append(row[0])
        return results

    def search_by_WorkoutID(self, workoutName):
        results = []
        self.cursor.execute(self.search_by_WorkoutID, [workoutName])
        sql_results = self.cursor.fetchall()
        for row in sql_results:
            results.append(row[0])
        return results

    def display_all_muscles(self):
        """

        :return: returns the list of results and displays all muscles in that list
        """
        results = []
        self.cursor.execute('select MuscleName from Muscles')
        sql_results = self.cursor.fetchall()
        for row in sql_results:
            results.append(row[0])
        return results

    def existingWorkout(self, Users_Workout, results=None):
        self.cursor.execute(self.search_by_previous_workouts, [Users_Workout])
        sql_results = self.cursor.fetchall()
        for row in sql_results:
            results.append(row[0])
            return results
        self.connection.commit()

    def search_by_previous_workouts(self, WorkoutName):
        results = []
        self.cursor.execute(SqlQueries.Previous_Table_Workouts, [WorkoutName])
        sql_results = self.cursor.fetchall()
        for row in sql_results:
            results.append(row[0])
        return results

