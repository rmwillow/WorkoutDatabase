
from choiceWorkout import orderOfStuff, data_base



if __name__ == "__main__":
    firstname = input("First Name: ")
    userId = data_base.search_by_firstname(firstname)
    if userId:
        orderOfStuff(userId)
    else:
        lastname = input("Last Name: ")
        data_base.add_user(firstname, lastname)
        userId = data_base.search_by_firstname(firstname)
        orderOfStuff(userId)