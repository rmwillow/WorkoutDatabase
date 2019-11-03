# from .exercisesApi import exerciseList
import sqlite3

from exercisesApi import dictTamp
from myQueries import *

connection = sqlite3.connect("tutorial.db")

cursor = connection.cursor()

cursor.execute(exercises_table)
cursor.execute(muscles_table)
try:
    cursor.execute(muscles_table_id_index)
except Exception as exception:
    print(exception)
    print('this index already exists')

for muscle, exercises in dictTamp.items():
    cursor.execute(muscles_table_insert, [muscle])
    cursor.execute('select MuscleID from Muscles where MuscleName = ?', [muscle])
    muscleId = cursor.fetchone()[0]
    for exercise in exercises:
        cursor.execute(exercises_table_insert, [exercise, muscleId])

cursor.execute(muscles_table_insert, ['abdominals'])

connection.commit()
connection.close()
