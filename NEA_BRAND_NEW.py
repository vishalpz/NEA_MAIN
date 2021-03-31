import sqlite3
import os
import math
import matplotlib.pyplot as plt
from scipy import stats
import time
import random
from datetime import date
import math

def Opening():

  print("Fitness App")
  print("-----")
  print("1. Login")
  print("2. Register")
  print()
  value_integer_check = intValid("Please select the integer value of what you want to access from the menu: ")
  value_userInput = rangeValid(value_integer_check, 1, 2)
  OpeningChoice(c, value_integer_check)

def OpeningChoice(c, value):
    if value == 1:
        Login(c)
    elif value == 2:
        Register(c)

def hashing(value):
  passw = []
  for x in range (len(value)):
    passw = ord(value[x])

  total = 12 + (5.6 * math.cos((360*passw) / 365)) + (1.4 * math.sin((360 * passw) /365 ))

  return int(total)


class UserValid:
  def __init__(self, username):
    self._username = username

  def len_valid(self):
    check = False
    while check == False:
        if len(self._username) <= 5 or len(self._username) >= 61:
            print("Your username must be between 6 to 60 characters long")
            print()
            self._username = input("Username: ")
        else:
            return self._username
          
  def dig_valid(self):
    check = False
    while check == False:
        if not any(char.isdigit() for char in self._username):
            print("Your username must contain a number")
            print()
            self._username = input("Username:")
        else:
            return self._username
          
  def upper_valid(self):
    check = False
    while check == False:
        if not any(char.isupper() for char in self._username):
            print("Your username must contain an uppercase letter")
            print()
            self._username = input("Username:")
        else:
            return self._username

  def lower_valid(self):
    check = False
    while check == False:
        if not any(char.islower() for char in self._username):
            print("Your username must contain a lowercase letter")
            print()
            self._username = input("Username:")
        else:
            return self._username

    
    

class PassValid:
  def __init__(self, password):
    self._password = password

  def len_valid(self):
    check = True
    while check == True:
        if len(self._password) <= 5 or len(self._password) >= 61:
            print("Your password must be between 6 to 60 characters long")
            print()
            self._password = input("Password: ")
        else:
            return self._password
          
  def dig_valid(self):
    check = False
    while check == False:
        if not any(char.isdigit() for char in self._password):
            print("Your password must contain a number")
            print()
            self._password = input("Password:")
        else:
            return self._password


  def upper_valid(self):
    check = False
    while check == False:
        if not any(char.isupper() for char in self._password):
            print("Your password must contain an uppercase letter")
            print()
            self._password = input("Password:")
        else:
            return self._password


  def lower_valid(self):
    check = False
    while check == False:
        if not any(char.islower() for char in self._password):
            print("Your password must contain a lowercase letter")
            print()
            self._password = input("Password:")
        else:
            return self._password
  

      


class RegisterValid:
  
  def __init__(self, username, password):
    self._password = password
    self._username = username


  def user_len_valid(self):
    check = True
    while check == True:
        if len(self._username) <= 5 or len(self._username) >= 61:
            tkinter.messagebox.showinfo("ERROR","Your username must be between 6 to 60 characters long")
            #self._username = input("Username:")
            Register()
        else:
            return self._username
       
  def user_dig_valid(self):
    check = False
    while check == False:
        if not any(char.isdigit() for char in self._username):
            tkinter.messagebox.showinfo("ERROR","Your username must contain a number")
            #self._username = input("Username:")
            Register()
        else:
            return self._username
          
  def user_upper_valid(self):
    check = False
    while check == False:
        if not any(char.isupper() for char in self._username):
            tkinter.messagebox.showinfo("ERROR","Your username must contain an uppercase letter")
            #self._username = input("Username:")
            Register()
        else:
            return self._username

  def user_lower_valid(self):
    check = False
    while check == False:
        if not any(char.islower() for char in self._username):
            tkinter.messagebox.showinfo("Your username must contain a lowercase letter")
            #self._username = input("Username:")
            Register()
        else:
            return self._username

  def pass_len_valid(self):
    check = True
    while check == True:
        if len(self._password) <= 5 or len(self._password) >= 61:
            tkinter.messagebox.showinfo("Your password must be between 6 to 60 characters long")
            #self._username = input("Username:")
            Register()
        else:
            return self._password
          
  def pass_dig_valid(self):
    check = False
    while check == False:
        if not any(char.isdigit() for char in self._password):
            tkinter.messagebox.showinfo("Your password must contain a number")
            #self._username = input("Username:")
            Register()
        else:
            return self._password
          
  def pass_upper_valid(self):
    check = False
    while check == False:
        if not any(char.isupper() for char in self._password):
            tkinter.messagebox.showinfo("Your password must contain an uppercase letter")
            #self._username = input("Username:")
            Register()
        else:
            return self._password

  def pass_lower_valid(self):
    check = False
    while check == False:
        if not any(char.islower() for char in self._password):
            tkinter.messagebox.showinfo("Your password must contain a lowercase letter")
            #self._username = input("Username:")
            Register()
        else:
            return self._password

def Login(c):
    print()
    print("Login")
    print("-----")
    username = input("Username: ")
    password = input("Password: ")
                     
    ID = hashing(password)
    val = selectUsernameFromUserID(c, ID)
    w = selectCustID(c, ID)
    y = selectNameFromUserID(c, w)
    if val == username:
      print()
      print("Welcome",y,"!")
      time.sleep(1)
      Menu(w)
    else:
      print()
      print("incorrect login, try again!")
      Login(c)

      
def Register(c):
    print("Register")
    print("--------")
    print("1. Your username and password must be between 6 to 60 characters and contain both letters and numbers and atleast 1 uppercase letter")
    print()
    
    user = input("Username: ")
    passw = input("Password: ")

    userVal = UserValid(user)
    passVal = PassValid(passw)
                        
    for choice in (userVal, userVal):
         user = choice.len_valid()
         user = choice.dig_valid()
         user = choice.upper_valid()
         user = choice.lower_valid()
      
    for choice in (passVal, passVal):
         passw = choice.len_valid()
         passw = choice.dig_valid()
         passw = choice.upper_valid()
         passw = choice.lower_valid()

    ID = hashing(passw)

    insertLogin(c, ID, user, passw)
    user_info(c, ID)

## divide the arrays into halves and sort them recursively until we get arrays with 1 element
def mergeSort(array, first_index, second_index):
    if first_index >= second_index:
        return

    middle = (first_index + second_index)//2
    mergeSort(array, first_index, middle)
    mergeSort(array, middle + 1, second_index)
    mergeArray(array, first_index, second_index, middle)
    
## mergining the sub arrays into a ordered array
def mergeArray(data, first_index, second_index, middle):

    first_ver = data[first_index:middle + 1]
    second_ver = data[middle+1:second_index+1]

    first_ver_index = 0
    second_ver_index = 0
    sorted_index = first_index


    while first_ver_index < len(first_ver) and second_ver_index < len(second_ver):


        if first_ver[first_ver_index] <= second_ver[second_ver_index]:
            data[sorted_index] = first_ver[first_ver_index]
            first_ver_index = first_ver_index + 1
            
        else:
            data[sorted_index] = second_ver[second_ver_index]
            second_ver_index = second_ver_index + 1

        sorted_index = sorted_index + 1
        

    while first_ver_index < len(first_ver):
        data[sorted_index] = first_ver[first_ver_index]
        first_ver_index = first_ver_index + 1
        sorted_index = sorted_index + 1

    while second_ver_index < len(second_ver):
        data[sorted_index] = second_ver[second_ver_index]
        second_ver_index = second_ver_index + 1
        sorted_index = sorted_index + 1
        
    return data
        

  
#2D array for exercise routines with calories for 1 rep
Abs = [["Crunches", "Mountain Climbers", "Sit Ups","Russian Twists", "Leg Raise"],[0.159, 0.327, 0.327, 0.234, 0.342]]
Chest = [["CPush Ups", "Knee Push Ups", "Wide Arm Push Ups", "Incline Push Ups","Leg Raise"],[0.423, 0.342, 0.450, 0.123, 0.234]]
Arms = [["CPush Ups", "Tricep Dips", "Bicep Curls", "Front Arm Raises", "Side Arm Raises"],[0.423, 0.334, 0.234, 0.145, 0.145]]
Leg = [["Squat", "Lunge", "Wall Calf Raises", "Side Lying Leg Lift Left", "Side Lying Leg Lift Right"],[0.324, 0.214, 0.134, 0.234, 0.234]]
Shoulder_Back = [["Front Arm Raises", "Side Arm Raises", "Push Ups", "Pull Ups", "Knee Push Ups"],[0.145, 0.145, 0.423, 0.450, 0.342]]

#data list of calories
data = [453, 954, 564, 783, 234, 522, 342]
dateNo = [1, 2, 3, 4, 5, 6, 7]
length = len(data)

#difficulty menu
def difficultyList(CustID):
    print()
    print("Loading new workout page...")
    time.sleep(2)
    print()
    print("Difficulty")
    print("----------")
    print("1. Beginner")
    print("2. Intermediate")
    print("3. Expert")
    print("---------")
    print("4. Go Back")
    print()
    #difficulty user inputs
    diff_integer_check = intValid("Please select the integer value of the difficulty: ")
    diff_userInput = rangeValid(diff_integer_check, 1, 4)
    return(diffDestination(diff_userInput, CustID))
    


def menuDestination(userInput, CustID):
 if userInput == 1:
   difficultyList(CustID)
 elif userInput == 2:
   progress(CustID)
 elif userInput == 3:
   load_workout()
 elif userInput == 4:
   user_info()

def diffDestination(userInput, CustID):
 if userInput == 1:
   workoutList(10, 600, CustID)
 elif userInput == 2:
   workoutList(15, 900, CustID)
 elif userInput == 3:
   workoutList(20, 1200, CustID)
 elif userInput == 4:
   Menu()
  


#workout menu list
def workoutList(reps, duration, CustID):
  Abs = [["Crunches", "Mountain Climbers", "Sit Ups","Russian Twists", "Leg Raise"],[0.159, 0.327, 0.327, 0.234, 0.342]]
  Chest = [["Push Ups", "Knee Push Ups", "Wide Arm Push Ups", "Incline Push Ups","Leg Raise"],[0.423, 0.342, 0.450, 0.123, 0.234]]
  Arms = [["Push Ups", "Tricep Dips", "Bicep Curls", "Front Arm Raises", "Side Arm Raises"],[0.423, 0.334, 0.234, 0.145, 0.145]]
  Leg = [["Squat", "Lunge", "Wall Calf Raises", "Side Lying Leg Lift Left", "Side Lying Leg Lift Right"],[0.324, 0.214, 0.134, 0.234, 0.234]]
  Shoulder_Back = [["Front Arm Raises", "Side Arm Raises", "Push Ups", "Pull Ups", "Knee Push Ups"],[0.145, 0.145, 0.423, 0.450, 0.342]]
  
  print()
  print("Workouts")
  print("--------")
  print("1. Abs")
  print("2. Chest")
  print("3. Arms")
  print("4. Leg")
  print("5. Shoulder & Back")
  print("------------")
  print("7. Go Back")
  print()
  workout_integer_check = intValid("Please select the integer value of what workout you want to access: ",)
  workout_userInput = rangeValid(workout_integer_check, 1 , 6)
  typeList = ['0','Abs','Chest','Arms','Leg','Shoulder & Back']
  Type = typeList[workout_userInput]

  if workout_userInput == 1:
      new_workout(reps, duration, Abs, Type, CustID)
  if workout_userInput == 2:
      new_workout(reps, duration, Chest, Type, CustID)
  if workout_userInput == 3:
      new_workout(reps, duration, Arms, Type, CustID) 
  if workout_userInput == 4:
      new_workout(reps, duration, Leg, Type, CustID)
  if workout_userInput == 5:
      new_workout(reps, duration, Shoulder_Back, Type, CustID)
  if workout_userInput == 6:
      new_workout(reps, duration, Abs, Type, CustID)
  if workout_userInput == 7:
    difficultyList()
      
class Workouts:
  
  def __init__(self, duration, reps, exercise, workout, Type, calories):
    self.__duration = duration
    self.__reps = reps
    self.__exercise = exercise
    self.__Type = Type
    self.__calories = calories
    self.__workout = workout

  def calc_calories(self):
   return self.__reps * (self.__exercise[self.__Type][self.__calories])

  def get_workout(self):
    return self.__exercise[self.__workout][self.__calories]

  def start(self):
    print()
    print((self.__calories + 1),". ", self.get_workout(), "x",self.__reps,"reps of", round(self.calc_calories(), 2) ,"calories.")

def binary_search(data, val, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if val == data[mid]:
        return mid

    if val < data[mid]:
        return binary_search(data, val, start, mid-1)
    else:
        return binary_search(data, val, mid+1, end)
      
    
def new_workout(reps, duration, exercise, Type, CustID):
  print()
  print("Loading new",Type,"workout...")
  time.sleep(2)
  print()
  print("---------------")
  print(Type,"Workout")
  print("---------------")
  
  dataSet = []
  array =[]
  
  for i in range (0, 5):
    x = Workouts(duration, reps, exercise, 0, 1, i)
    x.start()
    y = reps * (exercise[1][i])
    array.append(round(y, 2))
    
  for i in range (0, 5):
    y = reps * (exercise[1][i])
    dataSet.append(round(y, 2))
  
  mergeSort(array, 0, len(dataSet)-1)
  highest_val = array[len(array)-1]
  
  largest = binary_search(dataSet, highest_val, 0, len(dataSet)-1)
  
  print()
  print("The workout that burns the most calories is",exercise[0][largest],"with",array[len(array)-1],"calories")
    
  print()
  print("Duration(seconds):",duration)
  print()
  userInput = intValid("Press 1 to begin, Press 2 to go back to menu: ")
  rangeV = rangeValid(userInput, 1, 2)
  if rangeV == 1:
    startWorkout(reps, duration, exercise, Type, CustID, array)
  elif rangeV == 2:
    Menu()
  

class workoutQueue:

    def __init__(self, max_size, size=0, front=0, rear=0):
        self.queue = [[] for i in range(5)] 
        self.max_size = max_size
        self.size = size
        self.front = front
        self.rear = rear
    

    def enqueue(self, data):
        if not self.isFull():
            self.queue[self.rear] = data
            self.rear = int((self.rear + 1) % self.max_size)
            self.size += 1
        else:
            print('Queue is full')

    def dequeue(self):
        if not self.isEmpty():
            x = self.queue[self.front]
            self.front = int((self.front + 1) % self.max_size)
            self.size -= 1
        else:
            print('Queue is empty')
        return x

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.max_size

    def show(self):
        return self.queue


def totalCal(exercise):
    theSum = 0
    for i in exercise:
        theSum = theSum + i
    return theSum
 

def startWorkout(reps, duration, exercise, Type, CustID, array):
  q = workoutQueue(5)
  for i in range (0, 5):
    q.enqueue(exercise[0][i])

  queue = q.show()

  print(Type,"Workout")
  print("---------------")
  for i in range (0, 5):
    print("Start doing",q.dequeue(),"for",reps,"reps")
    time_per_exercise = duration / 5
    time.sleep(time_per_exercise)
    
  today = date.today()

  d1 = today.strftime("%d/%m/%Y")
  
  calories = totalCal(array)
  
  WorkoutID = random.randint(1, 100000)
  ID = random.randint(1, 100000)
  
  insertWorkouts(c, WorkoutID, Type, calories, duration)
  insertUserWorkouts(c, ID, CustID, WorkoutID, d1)
  print()
  print("Workout Complete! Well done!")
  input("Going back to Menu now....")
  Menu(CustID)
  

#creating database and tables

def createDatabase():
 if not os.path.isfile("fitness_db.db"):
   fitness_db = sqlite3.connect("fitness_db.db")
   c=fitness_db.cursor()

   c.execute('''CREATE TABLE Customer
   (CustomerID integer PRIMARY KEY,
   customer_firstname text,
   customer_surname text,
   customer_weight_kg integer,
   customer_height_cm integer,
   customer_dob date)
   ''')
   fitness_db.commit()

   c.execute('''CREATE TABLE Workouts
   (WorkoutID integer PRIMARY KEY,
   workout_routine text,
   calories integer,
   duration_secs integer)
   ''')
   fitness_db.commit()

   c.execute('''CREATE TABLE Login
   (LoginID integer PRIMARY KEY,
   username text,
   password text)
   ''')
   fitness_db.commit()

   c.execute('''CREATE TABLE UserWorkouts
   (UserWorkoutID integer PRIMARY KEY,
   CustomerID integer,
   WorkoutID integer,
   workout_date date)
   ''')
   fitness_db.commit()

   c.execute('''CREATE TABLE UserID
   (UserID integer PRIMARY KEY,
   CustomerID integer,
   LoginID integer,
   FOREIGN KEY(CustomerID) REFERENCES Customer(CustomerID),
   FOREIGN KEY(LoginID) REFERENCES Customer(CustomerID))
   ''')
   fitness_db.commit()
   fitness_db.close()

#inserting data into the database table for customer
def insertCustomer(c, ID, firstname, surname, weight, height, dob):
 c.execute('''INSERT OR REPLACE INTO Customer 
 VALUES (?, ?, ?, ?, ?, ?)''', (ID, firstname, surname, weight, height, dob))
 fitness_db.commit()

#inserting data into the database table for workouts list
def insertWorkouts(c, ID, routine, calories, duration):
 c.execute('''INSERT OR REPLACE INTO Workouts 
 VALUES (?, ?, ?, ?)''', (ID, routine, calories, duration))
 fitness_db.commit()

#inserting data into the database table for logins
def insertLogin(c, ID, username, password):
 c.execute('''INSERT OR REPLACE INTO Login 
 VALUES (?, ?, ?)''', (ID, username, password))
 fitness_db.commit()

#inserting data into the database table for customer workouts done
def insertUserWorkouts(c, ID, UserID, WorkoutID, workout_date):
 c.execute('''INSERT OR REPLACE INTO UserWorkouts
 VALUES (?, ?, ?, ?)''', (ID, UserID, WorkoutID, workout_date))
 fitness_db.commit()

def insertUser(c, ID, CustomerID, LoginID):
 c.execute('''INSERT OR REPLACE INTO UserID
 VALUES (?, ?, ?)''', (ID, CustomerID, LoginID))
 fitness_db.commit()

def selectLogin(c, LoginID):
 c.execute('''SELECT username FROM UserID.Login
 WHERE LoginID = ? ''', (LoginID,))
 val = c.fetchone()
 val = val[0]
 fitness_db.commit()
 return val

#def selectCalFromWorkouts(c, WorkoutID):

def selectCustID(c, LoginID):
 c.execute('''SELECT CustomerID FROM UserID
 WHERE LoginID = ? ''', (LoginID,))
 val = c.fetchone()
 val = val[0]
 fitness_db.commit()
 return val

def selectNameFromUserID(c, CustID):
 c.execute('''SELECT Customer.customer_firstname FROM UserID INNER JOIN Customer ON UserID.CustomerID = Customer.CustomerID WHERE Customer.CustomerID = ? ''', (CustID,))
 fitness_db.commit()
 val = c.fetchone()
 val = val[0]
 return val

def selectUsernameFromUserID(c, LoginID):
 c.execute('''SELECT Login.username FROM UserID
 INNER JOIN Login ON UserID.LoginID = Login.LoginID WHERE Login.LoginID = ? ''', (LoginID,))
 fitness_db.commit()
 val = c.fetchone()
 val = val[0]
 return val

def selectWorkoutDate(c, CustID):
 c.execute('''SELECT WorkoutID FROM UserWorkouts
 WHERE CustomerID = ? ''', (CustID,))
 val = c.fetchall()
 val = val[0]
 fitness_db.commit()
 return val


# recursively checking to see if user choice is an integer and if it isn't, asks again
def intValid(response):
  '''
  check = True
  while check == True:
  '''
  try:
       integer_check = int(input(response))       
  except ValueError:
       print("Please select an integer value option, try agian")
       intValid(response)
  else:
      return integer_check

#recursively checking to see if user choice is within the options and if it not, it asks again
def rangeValid(choice, lowest, highest):
  '''
    range_check = True
    while range_check == True:
    '''
  if choice < lowest or choice > highest:
            print("please select an option that is available")
            choice = int(input("Please select the integer value of what you want to access: "))
            rangeValid(choice, lowest, highest)
  else:
            return choice
 
#calculating the sum of all values in the list using recursion
def totalX(data):
    x = len(data)
    if x == 1:
        return data[0]
    else:
        return data[0] + totalX(data[1:])

#calculating the mean of x
def calcMean(total_x, length, data ):
  mean = total_x / length
  return mean
 
#calculating the sum of the squares of all list values
def totalXsqrd(length, data, y):
   Z= 0
   for i in range (0, length):
     x = Z + (data[i] * data[i]) 
     Z = x
   return Z

#calculating the standard deviation
def standardDev(Xsqrd, meanX, length):
   y = Xsqrd / length
   m = meanX * meanX
   variance = y - m
   standard_dev = math.sqrt(variance)
   return standard_dev

slope, intercept, r, p, std_err = stats.linregress(dateNo, data)

#draw linear graph
def linearGraph(x):
  y = slope * x + intercept
  return y
'''
  data = [453, 954, 564, 783, 234, 522, 342]
  dateNo = [1, 2, 3, 4, 5, 6, 7] 
  length = len(data)
  '''
def progress(CustID):
  x = selectWorkoutDate(c, CustID)
  print(x)
  data = []
  date = []
  date.append(x)
  print(date)
  
  print()
  print("Loading progress page...")
  time.sleep(2)
  mymodel = list(map(linearGraph, dateNo))
  plt.plot(dateNo, data) 
  plt.xlabel('date') 
  plt.xlabel('calories') 
  plt.title('Week 1')
  plt.scatter(dateNo, data)
  plt.plot(dateNo, mymodel)
  print()
  print("The mean calories burnt is:", mean)
  print("The standard deviation is:", sd)
  print()
  back = int(input("Press 1 to go back to menu: "))
  if back == 1:
      Menu(CustID)
  else:
      print()

  plt.show()
  
  
def load_workout():
  print()
  print("Loading saved workout...")
  time.sleep(2) 


def user_info(c, LoginID):
  CustID = random.randint(1, 100000)
  UserID = random.randint(1, 100000)
  print()
  print("Loading user info page...")
  time.sleep(2)
  print("USER INFO SETUP")
  print("---------------")
  print()
  Fname = input("Firstname: ")
  Sname = input("Surname: ")
  weight = input("Weight(kg): ")
  height = input("Height(cm): ")
  dob = input("Date of birth(DD/MM/YYYY): ")
  insertCustomer(c, CustID, Fname, Sname, weight, height, dob)
  insertUser(c, UserID, CustID, LoginID)
  y = selectNameFromUserID(c, CustID)
  print()
  print("Welcome",y,"!")
  time.sleep(1)
  Menu(CustID) 


createDatabase()

fitness_db = sqlite3.connect("fitness_db.db")
c=fitness_db.cursor()


temp = []

#outputting results of calculations
total_x = totalX(data)
meanX = round(calcMean(total_x, length, data),2)
total_x_sqrd = totalXsqrd(length, data, temp)
sdResult = round(standardDev(total_x_sqrd, meanX, length),2)

#Menu screen
def Menu(CustID):
 print()
 print("Menu")
 print("----")
 print("1. New Workout") 
 print("2. Review ")
 print("3. Change user info")
 print()
 #menu user inputs
 menu_integer_check = intValid("Please select the integer value of what you want to access from the menu: ")
 menu_userInput = rangeValid(menu_integer_check, 1, 3)
 menuDestination(menu_userInput, CustID)



Opening()

