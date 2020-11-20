# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import matplotlib.pyplot as plt
import random
plt.style.use('fivethirtyeight')


# %%
#Create a test, with No. questions and the correct answers 
def create_test(n_questions):
    # 1 or 0 are the answers of the questions
    test = []
    for i in range(n_questions):
        answer = random.randint(0, 1)
        test.append(answer)
    return test


# %%
test = create_test(10)
print(test)


# %%
#This function returns the grade of each student
def check_grade(student_answers, test_answers):
    grade = 0
    for i in range(len(test_answers)):
        if student_answers[i] == test_answers[i]:
            grade += 1
    return grade


# %%
#This generates random answers from each student
def create_student_random_answers(n_questions):
    student_answers = []
    for i in range(1, n_questions + 1):
        x = random.randint(0, 1)
        student_answers.append(x)
    return student_answers


# %%
#Creating the structure where i am gonna store all the data
def create_storage(n_students):    
    students_historical_data = {}# student history should be a dictonary (where the id of the student
    # is the # of the student, and each student have a list with the history of grades)
    for i in range(1, n_students + 1):
        students_historical_data[i] = []
    return students_historical_data


# %%
#with this function we are creating data for
#the grades of the students 
def create_data_graph(n_questions, n_students, test_answers, number_simulations):
    students_historical_data = create_storage(n_students)
    for j in range(number_simulations):
        for i in range(1, n_students+1):
            student_answers = create_student_random_answers(n_questions)
            grade = check_grade(student_answers, test_answers)
            students_historical_data[i].append(grade)
    return students_historical_data


# %%
results = create_data_graph(10, 1000, test, 20)


# %%
#With this function we can storage in an list multiple simulations
#of a test 
def storage_y_data(n_questions, results, number_simulations):
    sets_of_y_data = []
    for i in range(number_simulations):
        y_data = [0]*n_questions
        for j in range(1, len(results) + 1):
            y_data[results[j][i]-1] += 1
        sets_of_y_data.append(y_data)
    return sets_of_y_data


# %%
#Create y label data
sets_y_data = storage_y_data(10, results, 20)
num = 0
for i in sets_y_data:
    num += 1
    print(i)
print


# %%
#Create x label data (Grades)
x_data = []
for i in range(1, 11):
    x_data.append(i)


# %%
#Visualize the graph using matplotlib 
plt.figure(figsize=(12.2, 4.5))
plt.plot([results[200][0]+1], [sets_y_data[0][results[200][0]]], 'ro')
plt.plot(x_data, sets_y_data[0], zorder = 1)
plt.xlabel('Grades')
plt.ylabel('Students')
plt.show()


