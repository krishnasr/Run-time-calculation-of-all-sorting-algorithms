
from tkinter import *
import numpy as np
import time 
root=Tk()  #assign the tkinter call to root variable for easy calling 
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
def Selectionsort1():
    n=int(enter.get())  #get the input from the entry
    array_r=np.random.randint(1,100,n)  #assign random elements to array_a
    start=time.time()
    x=Selectionsort(array_r)  #calculate the run time of the algorithm
    end=time.time()
    timetaken=end-start
    outputlabel=Label(root,text="The run time of Selectionsort is   "+str(timetaken),fg="red") #print the runtime output
    outputlabel.grid(row=10,column=0)  
def Bubblesort(array): #Function BubbleSort
    for i in range(0,len(array)):
        for j in range(0, len(array)-1):
            if (array[j]>array[j+1]): #we compare the current index value to the next index value and swap 
                temp= array[j]
                array[j]=array[j+1]
                array[j+1]=temp
    return array
def Bubblesort1():
    n=int(enter.get()) #get the input from the entry
    array_r=np.random.randint(1,100,n) #assign random elements to array_a
    start=time.time()
    x=Bubblesort(array_r) #calculate the run time of the algorithm
    end=time.time()
    timetaken=end-start
    outputlabel1=Label(root,text="The run time of Bubblesort is  "+str(timetaken),fg="red")  #print the runtime output
    outputlabel1.grid(row=10,column=0)  
def Insertionsort(array): #Function InsertionSort
    for i in range(1,len(array)):
        value = array[i]         #we assign the variable value as the element which we need to compare
        j=i-1
        while (j>=0)and(array[j]>value):  #we compare the current value with the previous or predecessor value
            array[j+1]=array[j] #we move the larger value one position up to make space for swapping
            j=j-1
        array[j+1]=value
    return array
def Insertionsort1():
    n=int(enter.get()) #get the input from the entry
    array_r=np.random.randint(1,100,n) #assign random elements to array_a
    start=time.time()
    x=Insertionsort(array_r) #calculate the run time of the algorithm
    end=time.time()
    timetaken=end-start
    outputlabel2=Label(root,text="The run time of Insertionsort is  "+str(timetaken),fg="red")  #print the runtime output
    outputlabel2.grid(row=10,column=0)

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

def Mergesort1():
    n=int(enter.get()) #get the input from the entry
    array_r=np.random.randint(1,100,n) #assign random elements to array_a
    start=time.time()
    x=Mergesort(array_r) #calculate the run time of the algorithm
    end=time.time()
    timetaken=end-start
    outputlabel3=Label(root,text="The run time of Mergesort is  "+str(timetaken),fg="red")  #print the runtime output
    outputlabel3.grid(row=10,column=0)

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
def Quicksort1():
    n=int(enter.get()) #get the input from the entry
    array_r=np.random.randint(1,100,n) #assign random elements to array_a
    start=time.time()
    x=Quicksort(array_r,0,len(array_r)-1) #calculate the run time of the algorithm
    end=time.time()
    timetaken=end-start
    outputlabel4=Label(root,text="The run time of Quicksort is  "+str(timetaken),fg="red")  #print the runtime output
    outputlabel4.grid(row=10,column=0)

def quicksort3median(array,low,high):  #Function Quicksort using 3 medians
    if(low<high):
        piv=parti(array,low,high)   #calling partition function to partition the array
        if(piv!=0):
            quicksort3median(array,low,(piv-1))  #calling Quicksort3median for the left half of pivot
            quicksort3median(array,(piv+1),high)  #calling Quicksort3median for the other half of pivot
    return array
def parti(array,low,high):
    if((high-low)<2):     #when the size of the array if less than 2 we simply insertion sort the array
        Insertionsort2(array,low,high)
        return 0
    else:
        first=low
        mid=int((low+high)/2)     #finding the middle index
        last=high
        if(array[mid]<array[first]):    #after findinf the first, middle, last elements we sort them simply using if else
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
def Insertionsort2(array,low,high): #Function Insertionsort1  we call this function when the array size is less than 2
    for i in range(low+1,high+1):
        value = array[i]
        j=i-1
        while (j>=0)and(array[j]>value):
            array[j+1]=array[j]
            j=j-1
        array[j+1]=value
    return array
def quicksort3median1():
    n=int(enter.get()) #get the input from the entry
    array_r=np.random.randint(1,100,n) #assign random elements to array_a
    start=time.time()
    x=quicksort3median(array_r,0,len(array_r)-1) #calculate the run time of the algorithm
    end=time.time()
    timetaken=end-start
    outputlabel5=Label(root,text="The run time of 3medianQuicksort is  "+str(timetaken),fg="red")  #print the runtime output
    outputlabel5.grid(row=10,column=0)

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
def Heapsort1():
    n=int(enter.get()) #get the input from the entry
    array_r=np.random.randint(1,100,n) #assign random elements to array_a
    start=time.time()
    x=Heapsort(array_r) #calculate the run time of the algorithm
    end=time.time()
    timetaken=end-start
    outputlabel6=Label(root,text="The run time of Heapsort is  "+str(timetaken),fg="red")  #print the runtime output
    outputlabel6.grid(row=10,column=0)


   

inputlabel=Label(root,text="Enter the Size of the array :",fg="red") #making label for getting the size of the input
inputlabel.grid(row=1,column=0)        #here grid is used to position all the labels, entry, button in specific place of the GUI
enter=Entry(root,width=20)  #making an entry space to enter the size of the array
enter.grid(row=1,column=5)
inputlabel=Label(root,text="Select an Algorithm:",fg="red") #making label to select an algorithm
inputlabel.grid(row=3,column=0)       #making buttons for each type of sorting algorithm
button1=Button(root,text="Merge Sort",command=Mergesort1,fg="Blue")
button1.grid(row=5,column=0)
button2=Button(root,text="Heap Sort",command=Heapsort1,fg="Blue")
button2.grid(row=5,column=5)
button3=Button(root,text="Quick Sort",command=Quicksort1,fg="Blue")
button3.grid(row=5,column=10)
button4=Button(root,text="3 median Quick Sort",command=quicksort3median1,fg="Blue")
button4.grid(row=5,column=15)
button5=Button(root,text="Insertion Sort",command=Insertionsort1,fg="Blue")
button5.grid(row=7,column=0)
button6=Button(root,text="Selection Sort",command=Selectionsort1,fg="Blue")
button6.grid(row=7,column=5)
button7=Button(root,text="Bubble Sort",command=Bubblesort1,fg="Blue")
button7.grid(row=7,column=10)
root.mainloop()    #finally calling the  mainloop() to run the GUI
