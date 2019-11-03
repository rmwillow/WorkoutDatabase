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

muscles_table_id_index = """create unique index Muscles_MuscleID_uindex
    on Muscles (MuscleID);"""

#muscles_table_insert = """INSERT INTO Muscles(MuscleID, MuscleName) VALUES (NULL,{0})"""


muscles_table_insert = """INSERT INTO Muscles VALUES (NULL,?)"""
exercises_table_insert = """INSERT INTO Exercises VALUES (NULL,?,?)"""
