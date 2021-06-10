##################################################################
#                 Import libraries / Define globals              #
##################################################################

import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import matplotlib as mpl
import os
os.environ['MPLCONFIGDIR'] = '/tmp/matplotlib'
mpl.use('macosx')


numFunctionCalls = 20         # Number of times we will call Fib, GCD, and Exponentiations
testData = []                 # Holds all test data
copyTestData = []
smallTestData = []            # Holds all small test data
numOperations = 0             # Counter for operations for the various algorithms
fibData = []                  # Holds the x axis data and y value data for the Fibonacci scatter plot
gcdData = []                  # Holds the x axis data and y value data for the GCD scatter plot
expoData = [[], [], []]       # Holds the x axis data and y value data for the Exponentiation scatter plot
insertionData = []            # Holds the x axis data and y value data for the Insertion Sort scatter plot
selectionData = []            # Holds the x axis data and y value data for the Selection Sort scatter plot



##################################################################
#                    Import data from test data                  #
##################################################################

testDataPrefixes = ['sorted/data', 'random/data', 'rsorted/data']
smallTestDataPrefixes = ['smallSorted/data', 'smallRandom/data', 'smallRsorted/data']
fileSuffixes = ['_sorted.txt', '.txt', '_rSorted.txt']

# Load the test data into the testData array for processing with scatter plots
for directory in range(len(testDataPrefixes)):
  testData.append([])
  fileNumber = 100
  for i in range(100):
    with open(testDataPrefixes[directory] + str(fileNumber) + fileSuffixes[directory], 'rb') as f:
      testData[directory].append([int(i) for i in f.read().splitlines()])
    fileNumber += 100

# Load the small test data into the smallTestData array for processing with scatter plots
for directory in range(len(smallTestDataPrefixes)):
  smallTestData.append([])
  fileNumber = 0
  for file in range(10):
    fileNumber += 10
    with open(smallTestDataPrefixes[directory] + str(fileNumber) + fileSuffixes[directory], 'rb') as f:
      smallTestData[directory].append([int(file) for file in f.read().splitlines()])


##################################################################
#                       Fibonacci Sequence                       #
##################################################################

def Fib(k):
  global numOperations
  if k <= 1:
    return k
  else:
    numOperations += 1
    return Fib(k - 1) + Fib(k - 2)


def getFibNumOps():
  global numOperations, fibData
  xData = []
  yData = []
  for i in range(numFunctionCalls):
    Fib(i)
    xData.append(i)
    yData.append(numOperations)
    numOperations = 0
  fibData.append([xData, yData])



##################################################################
#                               GCD                              #
##################################################################

def euclids(m, n):
  global numOperations
  while n != 0:
    numOperations += 1
    r = m % n
    m = n
    n = r
  return m


def getGcdNumOps():
  global numOperations, gcdData
  xData = []
  yData = []
  for i in range(numFunctionCalls):
    n = Fib(i)
    numOperations = 0
    m = Fib(i + 1)
    numOperations = 0
    euclids(m, n)
    xData.append(n)
    yData.append(numOperations)
    numOperations = 0
  gcdData.append([xData, yData])


##################################################################
#                         Exponentiation                         #
##################################################################

#######################  Exponentiation 1  #######################
#decrease by one
def expo1(a, n):
  global numOperations
  if n == 0:
    return 1
  else:
    numOperations += 1
    return a * expo1(a, n - 1)


def getExpo1NumOps():
  global numOperations, expoData
  xData = []
  yData = []
  for i in range(numFunctionCalls):
    expo1(2, i)
    xData.append(i)
    yData.append(numOperations)
    numOperations = 0
  expoData[0].append([xData, yData])


#######################  Exponentiation 2  #######################

#decrease by constant factor
def expo2(a, n):
  global numOperations
  if n == 0:
    return 1
  elif n % 2 == 1:
    numOperations += 1
    return pow(expo2(a, (n - 1) / 2), 2) * a
  else:
    numOperations += 1
    return pow(expo2(a, n / 2), 2)


def getExpo2NumOps():
  global numOperations, expoData
  xData = []
  yData = []
  for i in range(numFunctionCalls):
    expo2(2, i)
    xData.append(i)
    yData.append(numOperations)
    numOperations = 0
  expoData[1].append([xData, yData])


#######################  Exponentiation 3  #######################
#divide and conquer
def expo3(a, n):
  global numOperations
  if n == 0:
    return 1
  elif n % 2 == 1:
    numOperations += 2
    return a * expo3(a, (n - 1) / 2) * expo3(a, (n - 1) / 2)
  else:
    numOperations += 1
    return expo3(a, n / 2) * expo3(a, n / 2)


def getExpo3NumOps():
  global numOperations, expoData
  xData = []
  yData = []
  for i in range(numFunctionCalls):
    expo3(2, i)
    xData.append(i)
    yData.append(numOperations)
    numOperations = 0
  expoData[2].append([xData, yData])



##################################################################
#                          Insertion Sort                        #
##################################################################

def insertionSort(n, dataSet):
  global numOperations
  for i in range(1, n):
    v = dataSet[i]
    j = i - 1
    while j >= 0 and dataSet[j] > v:
      numOperations += 1
      dataSet[j + 1] = dataSet[j]
      j -= 1
    numOperations += 1
    dataSet[j + 1] = v
  return dataSet


def getInsertionSortNumOps(inDataSetLen, dataSet):
  global numOperations, insertionData
  xData = []
  yData = []
  a = 0
  while a < inDataSetLen:
    dataSetLen = len(dataSet[a])
    insertionSort(dataSetLen, dataSet[a])
    xData.append(dataSetLen)
    yData.append(numOperations)
    numOperations = 0
    a += 2
  insertionData.append([xData, yData])



##################################################################
#                          Selection Sort                        #
##################################################################

def selectionSort(n, dataSet):
  global numOperations
  for i in range(n - 1):
    minVal = i
    for j in range(i + 1, n):
      numOperations += 1
      if dataSet[j] < dataSet[minVal]:
        minVal = j
    temp = dataSet[i]
    dataSet[i] = dataSet[minVal]
    dataSet[minVal] = temp
  return dataSet


def getSelectionSortNumOps(inDataSetLen, dataSet):
  global numOperations, selectionData
  xData = []
  yData = []
  a = 1
  while a < inDataSetLen:
    dataSetLen = len(dataSet[a])
    selectionSort(dataSetLen, dataSet[a])
    xData.append(dataSetLen)
    yData.append(numOperations)
    numOperations = 0
    a += 2
  selectionData.append([xData, yData])



##################################################################
#                       Main Function Calls                      #
##################################################################

getFibNumOps()
getGcdNumOps()
getExpo1NumOps()
getExpo2NumOps()
getExpo3NumOps()
for case in range(len(testData)):
  copyTestData.append(testData[case])
  getInsertionSortNumOps(len(copyTestData[case])/2, copyTestData[case])
  getSelectionSortNumOps(len(testData[case])/2, testData[case])





##################################################################
#                      Scatter Plot Rendering                    #
##################################################################

x = plt.figure(figsize=(20, 10))
x.set_facecolor("whitesmoke")
x.suptitle('Asymptotic Analysis of Algorithms', x=0.15, y=0.97, size=20)
plt.rcParams['axes.facecolor'] = 'w'

# Fibonacci Scatter Plot
plt.subplot(2, 3, 1)
plt.scatter([fibData[0][0]], fibData[0][1], s=6)
plt.xlabel('Input Size (k)')
plt.ylabel('#Additions A(k)')
plt.grid(linewidth=0.3)
plt.title('Fibonacci Complexity', size=11)


# GCD Scatter Plot
plt.subplot(2, 3, 2)
plt.scatter(gcdData[0][0], gcdData[0][1], s=6)
plt.xlabel('Input Size (n)')
plt.ylabel('#Divisions D(n)')
plt.grid(linewidth=0.3)
plt.title('GCD Complexity', size=11)

print(gcdData[0][0])
print(gcdData[0][1])
# Exponentiations 1, 2, 3 Scatter Plot
plt.subplot(2, 3, 3)
plt.scatter(expoData[0][0][0], expoData[0][0][1], s=6, label="Decrease by One")
plt.scatter(expoData[1][0][0], expoData[1][0][1], s=6, label="Decrease by Constant Factor")
plt.scatter(expoData[2][0][0], expoData[2][0][1], s=6, label="Divide and Conquer")
plt.ylabel('#Multiplications M(n)')
plt.xlabel('Input Size (n)')
plt.title('Exponetiation Complexity', size=11)
plt.grid(linewidth=0.3)
plt.legend(loc="upper left", facecolor='whitesmoke', framealpha=1)


# Insertion/Selection Sort Best Case Scatter Plot
plt.subplot(2, 3, 4)
plt.scatter(insertionData[0][0], insertionData[0][1], s=6, label="Insertion")
plt.scatter(selectionData[0][0], selectionData[0][1], s=6, label="Selection")
plt.xlabel('Input Size (n)')
plt.ylabel('#Comparisons C(n)')
plt.grid(linewidth=0.3)
plt.title('Insertion/Selection Sort Complexity (Best)', size=11)
plt.legend(loc="upper left", facecolor='whitesmoke', framealpha=1)


# Insertion/Selection Sort Average Case Scatter Plot
plt.subplot(2, 3, 5)
plt.scatter(insertionData[1][0], insertionData[1][1], s=6, label="Insertion")
plt.scatter(selectionData[1][0], selectionData[1][1], s=6, label="Selection")
plt.xlabel('Input Size (n)')
plt.ylabel('#Comparisons C(n)')
plt.grid(linewidth=0.3)
plt.title('Insertion/Selection Sort Complexity (Ave)', size=11)
plt.legend(loc="upper left", facecolor='whitesmoke', framealpha=1)


# Insertion/Selection Sort Worst Case Scatter Plot
plt.subplot(2, 3, 6)
plt.scatter(insertionData[2][0], insertionData[2][1], s=6, label="Insertion")
plt.scatter(selectionData[2][0], selectionData[2][1], s=6, label="Selection")
plt.xlabel('Input Size (n)')
plt.ylabel('#Comparisons C(n)')
plt.grid(linewidth=0.3)
plt.title('Insertion/Selection Sort Complexity (Worst)', size=11)
plt.legend(loc="upper left", facecolor='whitesmoke', framealpha=1)



##########################################################################################
#                                     Button Creation                                    #
##########################################################################################

buttonFibGcdAx = plt.axes([0.34, 0.94, 0.18, 0.03])
buttonFibGcd = Button(buttonFibGcdAx, 'Fibonacci/GCD User Testing Mode')
buttonExpoAx = plt.axes([0.53, 0.94, 0.18, 0.03])
buttonExpo = Button(buttonExpoAx, 'Exponentiation User Testing Mode')
buttonInsertionSelectionAx = plt.axes([0.72, 0.94, 0.18, 0.03])
buttonInsertionSelection = Button(buttonInsertionSelectionAx, 'Selection/Insertion User Testing Mode')


##########################################################################################
#                    Button Class Event Handlers and User Testing Mode I/O               #
##########################################################################################

class UserTestingButton(object):

  # Fib/GCD User Testing Mode Button Pressed
  def userTestingFibGcd(self, event):
    print("\n********* Fibonacci Sequence and GCD User Testing Mode *********")
    repeat = True
    while repeat:
      k = int(input("\nEnter new value for k to compute Fib(k) and Euclid\'s GCD(Fib(k+1),Fib(k)): "))
      while k < 0:
        print("Error: Invalid input. Input value must be non-negative.")
        k = int(input("Enter new value for k to compute Fib(k) and Euclid\'s GCD(Fib(k+1),Fib(k)): "))
      n = Fib(k)
      m = Fib(k+1)
      print("\nFib(k): " + str(n))
      print("GCD(Fib(k+1),Fib(k)): " + str(euclids(m,n)))
      result = input("\nCompute for another k value? (y or n): ")
      while result != "y" and result != "Y" and result != "n" and result != "N":
        print("\nError: Invalid input. Input value must be \"y\" or \"n\".")
        result = input("\nCompute for another k value? (y or n): ")
      if result == "n" or result == "N":
        repeat = False


  # Exponentiation User Testing Mode Button Pressed
  def userTestingExponentiation(self, event):
    print("\n************** Exponentiation User Testing Mode **************")
    repeat = True
    while repeat:
      print("\nEnter new values for a and n to compute E(a^n) using three methods.\n")
      a = int(input("Value for a: "))
      n = int(input("Value for n: "))
      while n < 0:
        print("\nError: Invalid input. Input value n must be non-negative.")
        n = int(input("\nEnter new value for n to compute E(a^n): "))
      print("\nExponentiation Method 1/Decrease by One gives result: " + str(expo1(a,n)))
      print("Exponentiation Method 2/Decrease by Constant Factor gives result: " + str(expo2(a,n)))
      print("Exponentiation Method 3/Divide and Conquer gives result: " + str(expo3(a,n)))
      result = input("\nCompute for another pair of a and n values? (y or n): ")
      while result != "y" and result != "Y" and result != "n" and result != "N":
        print("\nError: Invalid input. Input value must be \"y\" or \"n\".")
        result = input("\nCompute for another k value? (y or n): ")
      if result == "n" or result == "N":
        repeat = False


  # Inserttion/Selection Sort User Testing Mode Button Pressed
  def userTestingInsertionSelectionSort(self, event):
    print("\n******** Selection and Insertion Sort User Testing Mode ********")
    repeat = True
    while repeat:
      print("\nEnter new value for n to compute SelectionSort(n) and InsertionSort(n)")
      print("Value must be either 10, 20, 30, ..., or 100")
      n = int(input("\nEnter n value: "))
      while n < 0 or n > 100 or n % 10 != 0:
        print("\nError: Invalid input. Input value n must be non-negative AND meet range/increment standards.")
        print("\nEnter new value for n to compute SelectionSort(n) and InsertionSort(n)")
        print("Value must be either 10, 20, 30, ..., or 100")
        n = int(input("\nEnter n value: "))


      newSelection1 = selectionSort(n, smallTestData[0][int(n/10 - 1)])
      newInsertion1 = insertionSort(n, smallTestData[0][int(n/10 - 1)])
      print("\nBest Case for Selection Sort: " + str(newSelection1))
      print("Best Case for Insertion Sort: " + str(newInsertion1))


      newSelection2 = selectionSort(n, smallTestData[1][int(n / 10 - 1)])
      newInsertion2 = insertionSort(n, smallTestData[1][int(n / 10 - 1)])
      print("\nAverage Case for Selection Sort: " + str(newSelection2))
      print("Average Case for Insertion Sort: " + str(newInsertion2))


      newSelection3 = selectionSort(n, smallTestData[2][int(n / 10 - 1)])
      newInsertion3 = insertionSort(n, smallTestData[2][int(n / 10 - 1)])
      print("\nWorst Case for Selection Sort: " + str(newSelection3))
      print("Worst Case for Insertion Sort: " + str(newInsertion3))


      result = input("\nCompute for another n value? (y or n): ")
      while result != "y" and result != "Y" and result != "n" and result != "N":
        print("\nError: Invalid input. Input value must be \"y\" or \"n\".")
        result = input("\nCompute for another n value? (y or n): ")
      if result == "n" or result == "N":
        repeat = False



##################################################################
#                   Button Click Event Calls                     #
##################################################################

callback = UserTestingButton()
buttonFibGcd.on_clicked(callback.userTestingFibGcd)
buttonExpo.on_clicked(callback.userTestingExponentiation)
buttonInsertionSelection.on_clicked(callback.userTestingInsertionSelectionSort)



##################################################################
#                          Final Display                        #
##################################################################

plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.2, hspace=0.3)
plt.tight_layout
plt.show()