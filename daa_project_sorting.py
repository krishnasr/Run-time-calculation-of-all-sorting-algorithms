# -*- coding: utf-8 -*-
"""DAA_project_sorting

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GlSr8A2cwozGNu4zc467qskRmEbwzgSz
"""

#First we import the required Libraries
import numpy as np #for arrays
import matplotlib.pyplot as plt #for Charts

array_a= np.random.randint(1,100,10)
print(array_a)

def Selectionsort(array): #Function Selectionsort
  for i in range(0,len(array)):
    min = i                          # min holds the index of the minimum value in the array
    for j in range(i+1,len(array)):
      if (array[j]<array[min]): 
        min=j                       #after looping we swap the min index value 
    temp = array[i]
    array[i]=array[min]
    array[min]=temp
  return array

print(Selectionsort(array_a))

import time  #importing time library to calculate the run time of the algorithm
size=[5,10,20,50,75,100,150,250,500,750,1000,2500,5000,7500,10000]
timetak=[None]*len(size)  #We initialize an array that will store the run time  of the algorithm for each array size
i=0
for item in size:
  array_r=np.random.randint(1,100,item) #for each array size we initialize random number between 1 to 100
  start=time.time()
  x=Selectionsort(array_r) 
  end=time.time()
  timetak[i]=end-start
  i=i+1
print(timetak)

plt.plot(size,timetak)       #using matplotlib library we plot the time vs input chart for the given algorithm
plt.xlabel('Size of the array') #we name  the x label of the chart 
plt.ylabel('Time taken') #we name the y label of the chart
plt.title('Time vs Inputsize chart for Selection Sort') #we name the title of the chart
plt.show()

def Bubblesort(array): #Function BubbleSort
  for i in range(0,len(array)):
    for j in range(0, len(array)-1):
      if (array[j]>array[j+1]): #we compare the current index value to the next index value and swap 
        temp= array[j]
        array[j]=array[j+1]
        array[j+1]=temp
  return array

print(Bubblesort(array_a))

import time #importing time library to calculate the run time of the algorithm
size1=[5,10,20,50,75,100,150,250,500,750,1000,2500,5000,7500,10000]
timetak1=[None]*len(size1) #We initialize an array that will store the run time of the algorithm for each array size
i=0
for item in size1:
  array_r=np.random.randint(1,100,item)  #for each array size we initialize random number between 1 to 100
  start=time.time()
  x=Bubblesort(array_r)
  end=time.time()
  timetak1[i]=end-start
  i=i+1
print(timetak1)

plt.plot(size1,timetak1)  #using matplotlib library we plot the time vs input chart for the given algorithm
plt.xlabel('Size of the array') #we name  the x label of the chart
plt.ylabel('Time taken')   #we name the y label of the chart
plt.title('Time vs Inputsize chart for Bubble Sort') #we name the title of the chart
plt.show()

def Insertionsort(array): #Function InsertionSort
  for i in range(1,len(array)):
    value = array[i]         #we assign the variable value as the element which we need to compare
    j=i-1
    while (j>=0)and(array[j]>value):  #we compare the current value with the previous or predecessor value
      array[j+1]=array[j] #we move the larger value one position up to make space for swapping
      j=j-1
    array[j+1]=value
  return array

print(Insertionsort(array_a))

import time #importing time library to calculate the run time of the algorithm
size2=[5,10,20,50,75,100,150,250,500,750,1000,2500,5000,7500,10000]
timetak2=[None]*len(size2)  #We initialize an array that will store the run time of the algorithm for each array size
i=0
for item in size2:
  array_r=np.random.randint(1,100,item)  #for each array size we initialize random number between 1 to 100
  start=time.time()
  x=Insertionsort(array_r)
  end=time.time()
  timetak2[i]=end-start
  i=i+1
print(timetak2)

plt.plot(size2,timetak2) #using matplotlib library we plot the time vs input chart for the given algorithm
plt.xlabel('Size of the array') #we name  the x label of the chart 
plt.ylabel('Time taken') #we name the y label of the chart
plt.title('Time vs Inputsize chart for InsertionSort Sort')  #we name the title of the chart
plt.show()

def Mergesort(array):
  if (len(array)==1):   # if length of the array is 1 we return the array cuz there is no need to sort the array
    return array
  mid=int((len(array)/2))  #finding the middle index of the array
  Left=array[0:mid]       #storing the first and second half of the array in variable left and right 
  Right=array[mid:len(array)]
  Left=Mergesort(Left)        #calling mergesort on the first half
  Right=Mergesort(Right)      #calling mergesort on the second half
  return Merge(Left,Right)

def Merge(L,R):
  x=0
  y=0
  z=0
  k=len(L)+len(R)
  array_t=[None]*k
  while(x<len(L))and(y<len(R)):
    if (L[x]<R[y]):    #find the smaller value in L and R store that in the temperory array
      array_t[z]=L[x]
      x=x+1
    else:
      array_t[z]=R[y]
      y=y+1
    z=z+1
  while(x<len(L)):  #when the R array is empty we store the remaining value of L array to the temperory array
    array_t[z]=L[x]
    z=z+1
    x=x+1
  while(y<len(R)): #when the L array is empty we store the remaining value of R array to the temperory array
    array_t[z]=R[y]
    z=z+1
    y=y+1
  return array_t

print(Mergesort(array_a))

import time  #importing time library to calculate the run time of the algorithm
size3=[5,10,20,50,75,100,150,250,500,750,1000,2500,5000,7500,10000]
timetak3=[None]*len(size3)  #We initialize an array that will store the run time of the algorithm for each array size
i=0
for item in size3:
  array_r=np.random.randint(1,100,item)  #for each array size we initialize random number between 1 to 100
  start=time.time()
  x=Mergesort(array_r)
  end=time.time()
  timetak3[i]=end-start
  i=i+1
print(timetak3)

plt.plot(size3,timetak3)  #using matplotlib library we plot the time vs input chart for the given algorithm
plt.xlabel('Size of the array')  #we name  the x label of the chart
plt.ylabel('Time taken')  #we name the y label of the chart
plt.title('Time vs Inputsize chart for MergeSort Sort')  #we name the title of the chart
plt.show()

def Quicksort(array,low,high): #Function Quicksort
  if(low<high):
    piv=Partition(array,low,high) #calling partition function to partition the array
    Quicksort(array,low,(piv-1)) #calling Quicksort for the left half of pivot
    Quicksort(array,(piv+1),high) #calling Quicksort for the Right half of pivot
  return array

def Partition(array,low,high):
  pivot=array[high]    #Picking the last element as pivot
  i=low-1
  for j in range(low,high+1):
    if(array[j]<pivot): # if current value is smaller than the pivot we increment the index of the samller value
      i=i+1
      temp=array[j]
      array[j]=array[i]
      array[i]=temp
  temp1=array[i+1]     #finally we swap the last value with i+1 index value
  array[i+1]=array[high]
  array[high]=temp1
  return (i+1)

print(Quicksort(array_a,0,len(array_a)-1))

import time  #importing time library to calculate the run time of the algorithm
size4=[5,10,20,50,75,100,150,250,500,750,1000,2500,5000,7500,10000]
timetak4=[None]*len(size4)  #We initialize an array that will store the run time of the algorithm for each array size
i=0
for item in size4:
  array_r=np.random.randint(1,100,item)  #for each array size we initialize random number between 1 to 100
  start=time.time()
  x=Quicksort(array_r,0,len(array_r)-1) 
  end=time.time()
  timetak4[i]=end-start
  i=i+1
print(timetak4)

plt.plot(size4,timetak4) #using matplotlib library we plot the time vs input chart for the given algorithm
plt.xlabel('Size of the array')  #we name  the x label of the chart
plt.ylabel('Time taken')  #we name the y label of the chart
plt.title('Time vs Inputsize chart for QuickSort Sort')  #we name the title of the chart
plt.show()

def quicksort3median(array,low,high):  #Function Quicksort using 3 medians
  if(low<high):
    piv=parti(array,low,high)   #calling partition function to partition the array
    if(piv!=0):
      quicksort3median(array,low,(piv-1))  #calling Quicksort3median for the left half of pivot
      quicksort3median(array,(piv+1),high)  #calling Quicksort3median for the other half of pivot
  return array

def parti(array,low,high):
  if((high-low)<2):     #when the size of the array if less than 2 we simply insertion sort the array
    Insertionsort1(array,low,high)
    return 0
  else:
    first=low
    mid=int((low+high)/2)     #finding the middle index
    last=high
    if(array[mid]<array[first]):    #after finding the first, middle, last elements we sort them simply using if else
      temp=array[mid]
      array[mid]=array[first]
      array[first]=temp
    if(array[last]<array[mid]):
      temp=array[last]
      array[last]=array[mid]
      array[mid]=temp
      if(array[mid]<array[first]):
        temp=array[mid]
        array[mid]=array[first]
        array[first]=temp
    temp=array[mid]
    array[mid]=array[high-1]
    array[high-1]=temp
    pivot=array[high-1]   #we pick the middle element of the sorted 3 values as the pivot
    i=low
    for j in range(low+1,high): # we do the same partition as the quick sort
      if(array[j]<pivot):
        i=i+1
        temp=array[j]
        array[j]=array[i]
        array[i]=temp
    temp1=array[i+1]
    array[i+1]=array[high-1]
    array[high-1]=temp1
    return (i+1)

def Insertionsort1(array,low,high): #Function Insertionsort1  we call this function when the array size is less than 2
  for i in range(low+1,high+1):
    value = array[i]
    j=i-1
    while (j>=0)and(array[j]>value):
      array[j+1]=array[j]
      j=j-1
    array[j+1]=value
  return array

quicksort3median(array_a,0,(len(array_a)-1))

import time #importing time library to calculate the run time of the algorithm
size5=[5,10,20,50,75,100,150,250,500,750,1000,2500,5000,7500,10000]
timetak5=[None]*len(size5)  #We initialize an array that will store the run time of the algorithm for each array size
i=0
for item in size5:
  array_r=np.random.randint(1,100,item)  #for each array size we initialize random number between 1 to 100
  start=time.time()
  x=quicksort3median(array_r,0,len(array_r)-1)
  end=time.time()
  timetak5[i]=end-start
  i=i+1
print(timetak5)

plt.plot(size5,timetak5)  #using matplotlib library we plot the time vs input chart for the given algorithm
plt.xlabel('Size of the array')  #we name  the x label of the chart
plt.ylabel('Time taken')  #we name the y label of the chart
plt.title('Time vs Inputsize chart for QuickSort using 3 medians Sort')  #we name the title of the chart
plt.show()

def Heapsort(array): #Function Heapsort
  array1=[0]*(len(array)+1) #we move the array elements by one index so that it will be easy to sort
  for i in range(0,len(array)):
    array1[i+1]=array[i]
  for j in range((int(len(array)/2)),0,-1):  #the parents of the of the heapsort tree will be the first half of the array so we run the loop upto half of the array
    Heapifyarray(array1,j,len(array1)-1)   # First we heapify the given array into max heap by calling the heapifyarray function 
  for k in range(len(array),1,-1): # we swap the first and last element of the array and do max heapify until all the elements in the array are sorted
    temp=array1[k]
    array1[k]=array1[1]
    array1[1]=temp
    Heapifyarray(array1,1,k)
  for p in range(0,len(array)): #Finally we move the all the elements one index value back to original position and return the array
    array[p]=array1[p+1]
  return array

def Heapifyarray(array,parent,size):
  max=parent                        #for the heap sort array the left child of parent is parent*2 and the right child of the parent is parent*2+1 so we stire the index of those value in vairable leftchild and rightchild
  leftchild=parent*2
  rightchild=(parent*2)+1
  if(leftchild<size)and(array[parent]<array[leftchild]): #now we compare the leftchild value and the parent value and the larger ones index will be stored in the max variable
    max=leftchild
  if(rightchild<size)and(array[max]<array[rightchild]):   #now we compare the rightchild value and the parent value and the larger ones index will be stored in the max variable
    max=rightchild
  if max!=parent:             #if the max index is not the parent's index then we the swap the max index value with the parent index value
    temp=array[max]
    array[max]=array[parent]
    array[parent]=temp
    Heapifyarray(array,max,size)  #Finally we call Heapifyarray recursively until all the elements are in the max heaptree form

print(Heapsort(array_a))

import time  #importing time library to calculate the run time of the algorithm
size6=[5,10,20,50,75,100,150,250,500,750,1000,2500,5000,7500,10000]
timetak6=[None]*len(size6)  #We initialize an array that will store the run time of the algorithm for each array size
i=0
for item in size6:
  array_r=np.random.randint(1,100,item)  #for each array size we initialize random number between 1 to 100
  start=time.time()
  x=Heapsort(array_r)
  end=time.time()
  timetak6[i]=end-start
  i=i+1
print(timetak6)

plt.plot(size6,timetak6)  #using matplotlib library we plot the time vs input chart for the given algorithm
plt.xlabel('Size of the array')  #we name  the x label of the chart
plt.ylabel('Time taken')  #we name the y label of the chart
plt.title('Time vs Inputsize chart for HeapSort') #we name the title of the chart
plt.show()

alltimetaken=[timetak,timetak1,timetak2,timetak3,timetak4,timetak5,timetak6] #we store  the time taken in each and every algorithm in a single array alltimetaken
for i in range (0,len(size)):        #now using Bar char we represent all the comparison of the algorithms for different inputsize
  tik=[0]*7          #in tik array we store all the run time of algorithms for each input size
  k=0
  for time in alltimetaken:
    tik[k]=time[i]
    k=k+1
  print(tik)
  plt.figure(figsize=(10,5)) #size of the figure
  plt.bar(["selectionsort","Bubblesort","InsertionSort","Mergesort","Quicksort","3medianQuicksort","Heapsort"],tik,width=0.4) #calling barplot
  plt.xlabel('All sorting Algorithms')  #we name  the x label of the chart
  plt.ylabel('Time taken')  #we name the y label of the chart
  plt.title('Time vs Inputsize chart for all the Sorting Algorithm, Size = '+str(size[i])) #we name the title of the chart
  plt.show()

plt.figure(figsize=(5,10))
plt.plot(size,timetak,label="SelectionSort")  #using matplotlib library we plot the time vs input chart for all the given algorithm
plt.plot(size,timetak1,label="BubbleSort") 
plt.plot(size,timetak2,label="InsertionSort") 
plt.plot(size,timetak3,label="MergeSort") 
plt.plot(size,timetak4,label="QuickSort") 
plt.plot(size,timetak5,label="3 median QuickSort")
plt.plot(size,timetak6,label="HeapSort") 
plt.xlabel('Size of the array')  #we name  the x label of the chart
plt.ylabel('Time taken')  #we name the y label of the chart
plt.title('Time vs Inputsize chart for all the Sorting Algorithm') #we name the title of the chart
plt.yticks([0.01,0.02,0.03,0.05,0.08,0.09,0.1,0.2,0.3,0.5,0.10,0.11,0.12,0.13,1,2,3,4,5,7,8,9,10,12,13,14,15,25,30,40,45])
plt.legend()
plt.show()

