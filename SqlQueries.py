exercises_table = """create table  IF NOT EXISTS Exercises
(ExerciseId   integer not null
        constraint Exercises_pk
            primary key autoincrement,
    ExerciseName text,
    MuscleId     integer
        references Muscles
    
);"""

muscles_table = """create table  IF NOT EXISTS Muscles
(
    MuscleID   integer
        constraint Muscles_pk
            primary key autoincrement,
    MuscleName text not null
);
"""

Users_Table = """create table IF NOT EXISTS Users
(
	UsersId integer
		constraint Users_table_pk
			primary key autoincrement,
	UsersFirstName text not null,
	UsersLastName text not null
);
"""

Workout_Table = """create table Workout
(
    WorkoutID         integer
        constraint Workout_pk
            primary key autoincrement,
    WorkoutName       text
);"""





Workout_Exercise_Table = """create table Workout_exercise
(
    WorkoutID  integer 
        references Workout,
    ExerciseId integer 
        references Exercises
);"""

Users_Workout_Table = """create table Users_Workout
(
    WorkoutID integer 
        references Workout,
    UserId    integer 
        references Users
);
"""

search_by_muscle = """SELECT ExerciseName FROM Muscles
    JOIN Exercises E on Muscles.MuscleID = E.MuscleId

WHERE MuscleName = ?"""


search_by_workout = """SELECT WorkoutName FROM Workout
    JOIN WorkoutName on Workout.WorkoutID = WorkoutID

WHERE WorkoutName = ?"""


search_by_exercise_id = """SELECT ExerciseId FROM Exercises
WHERE ExerciseName = ?"""

search_by_user_exercises = """
SElECT Exercises.ExerciseName from Exercises
JOIN Users_Exercises UE on Exercises.ExerciseId = UE.ExerciseId
JOIN Users U on UE.UsersId = U.UsersId
WHERE U.UsersFirstName = ?
"""

search_by_multiple_selection = """
SELECT Exercises.ExerciseName from Exercises
JOIN Workout UE ON MultipleSelection.existingWorkout = UE.existingWorkout
WHERE  U.previousWorkouts = ?
"""


Users_Workout_Table_index = """ create unique index sqlite_autoindex_User_Workout_1
    on User_Workout (WorkoutID);"""

muscles_table_id_index = """create unique index Muscles_MuscleID_uindex
    on Muscles (MuscleID);"""

muscles_table_insert = """INSERT INTO Muscles VALUES (NULL,?)"""
exercises_table_insert = """INSERT INTO Exercises VALUES (NULL,?,?)"""
Users_Table_insert = """INSERT INTO Users VALUES (NULL, ?, ?)"""
Workout_Exercise_Table_insert = """INSERT INTO Workout_exercise VALUES ( ?, ?)"""
Users_Workout_Table_insert = """INSERT INTO Users_Workout VALUES (?, ?)"""
Workout_Table_insert = """INSERT INTO Workout VALUES ( NULL, ?)"""
Previous_Table_Workouts_insert = """INSERT INTO Previous_Workout VALUES (NULL, ?, ?)"""
workout_table_insert = """INSERT INTO MultipleSelection VALUES (NULL, ?, ?, ?)"""

exercises_table_update_muscleid = """UPDATE Exercises
SET MuscleId = 1
WHERE
    MuscleId = 19 
;"""

