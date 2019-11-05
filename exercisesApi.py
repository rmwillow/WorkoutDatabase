from typing import Dict, List

import requests

"""getting the raw data from the http content 
transferring the raw data into a object called exerciseResponse"""
exerciseResponse = requests.get('https://raw.githubusercontent.com/davejt/exercise/master/data/exercises')

"""if exercise response is successful it returns 
"this was successful, else this failed"""
if exerciseResponse.status_code == 200:
    print('this was successful')
else:
    print('this failed')

""" Taking the raw data from exerciseResponse (http content) we use content 
to get access to raw bytes of data and than use decoding which converts a bytes 
object encoded using a particular character set encoding to a string object. """
rawData = exerciseResponse.content.decode()

""" taking the raw data and splitting it up into a new line after each "\n" that is in the raw data/code """
exerciseList = rawData.split('\n')

""" telling the python interpreter what data types will
 be in this dictionary for ex: the key will be a  
 str and the value will be a list that has strings as elements """
dictTamp: Dict[str, List[str]] = dict()

"""creating a function called clean data giving it a argument/parameter of x"""


def clean_data(x):
    """

    :param x:
    :return: cleans list of string
    """
    """The isinstance() function returns True if the specified object
    is of the specified type, otherwise False in this line if it is a
    string it returns true and the value of x"""
    if isinstance(x, str):  # if using python2 replace str with basestring to include unicode type

        """function chaining, takes x performs strip against 
        it than takes that output and preforms lower case 
        against it once it is finished it stores it in the variable X"""
        x = x.strip().lower()
    elif isinstance(x, list):
        x = [clean_data(v) for v in x]
    # elif isinstance(x, dict):
    #    for k, v in x.items():
    #        x.pop(k)  # also strip keys
    #        x[strip_all(k)] = strip_all(v)
    """return returns the value of x"""
    return x


"""taking exerciseList from Exercise you create a variable called exerciseComma 
append.split to each exercise after each , in which it 
returns a new line after each , like we have done previously with "/n" """
for exercise in exerciseList:
    exerciseComma = exercise.split(',')

    """take the first and second element from the list exerciseComma.
    1 and 0 are the index numbers of exerciseComma list.
    next we send those list elements as parameters/arguments for the function clean data.
    once the function clean data completes/returns data it will store 
    it in the new variable called exerciseType and exerciseWorkout"""
    exerciseType = clean_data(exerciseComma[1])
    exerciseWorkout = clean_data(exerciseComma[0])

    '''if it is dictTamp  it retrieves exerciseType and appends it
    to exerciseWorkout (append method adds an item to the end of the list)'''
    if dictTamp.get(exerciseType):
        dictTamp[exerciseType].append(exerciseWorkout)
    else:
        """if it is not dictamp else will assign exercise workout list to the name of tempList.
            than it will add the list of exercise type from dictTamp and append it to templist.
            printing the result of dictTamp and getting a return of abdominals."""
        tempList = [exerciseWorkout]
        dictTamp[exerciseType] = tempList




"""the key is used to access the elements of the dictionary.
the value returns the list of values in the dictionary specified.
and in dictTamp is providing the dictionary name we want to retrieve our values from.
and we append the items method to our dictionary dictTamp so that
it will display our list from dictTamp now that we provided the KEY, VALUE and dictionary name.
"""
for key, value in dictTamp.items():
    dictTamp[key] = list(set(value))
