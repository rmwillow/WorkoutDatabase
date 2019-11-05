create table Muscles
(
    MuscleID   integer
        constraint Muscles_pk
            primary key autoincrement,
    MuscleName text not null
);

create unique index Muscles_MuscleID_uindex
    on Muscles (MuscleID);

create table Exercises
(
    ExerciseName text,
    MuscleId     integer
        references Muscles,
    ExerciseId   integer not null
        constraint Exercises_pk
            primary key autoincrement
);

create table Users_table
(
    UsersId        int
        constraint Users_table_pk
            primary key,
    UsersFirstName int not null,
    UsersLastName  int not null
);


create table Users_Exercise_Table
(
    UsersId    int
        references Users_table,
    ExerciseId int
        references Exercises
);


SELECT ExerciseName
from Exercises as E
         JOIN Muscles M on E.MuscleId = M.MuscleID
WHERE M.MuscleName = ' adductors'


