from typing import Dict, List

import requests

exerciseResponse = requests.get('https://raw.githubusercontent.com/davejt/exercise/master/data/exercises')
if exerciseResponse.status_code == 200:
    print('this was successful')
else:
    print('this failed')

rawData = exerciseResponse.content.decode()
exerciseList = rawData.split('\n')
dictTamp: Dict[str, List[str]] = dict()
x = 'dictTamp'


def strip_all(x):
    if isinstance(x, str):  # if using python2 replace str with basestring to include unicode type
        x = x.strip()
    elif isinstance(x, list):
        x = [strip_all(v) for v in x]
    elif isinstance(x, dict):
        for k, v in x.items():
            x.pop(k)  # also strip keys
            x[strip_all(k)] = strip_all(v)
    return x


for exercise in exerciseList:
    exerciseComma = exercise.split(',')
    exerciseType = exerciseComma[1]
    exerciseWorkout = exerciseComma[0]
    if dictTamp.get(exerciseType):
        dictTamp[exerciseType].append(exerciseWorkout)

    else:
        tempList = [exerciseWorkout]
        dictTamp[exerciseType] = tempList
        print(dictTamp)

    # orig_text = ' dictTamp \n'
    # print(orig_text.strip([dictTamp]))
