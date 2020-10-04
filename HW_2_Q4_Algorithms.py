#Question 4 Rachel Trickett
#I recommend using a small k value
#I recommend using a bigger t value and an n bigger than t
#k=3 t=8 and n=15 usually shows all possible cases

import random

#max heap sink function that swaps a mirroring array in the same fashion
def sink(k, array,end, mirror):
    root=k
    while (2*(root)+1<=end):
        child=2*(root)+1
        if ((child+1)<=end and (array[child]<array[child+1])):
            child=child+1
        if(array[root]>array[child]):
            break
        array[root], array[child]=array[child], array[root]
        mirror[root], mirror[child]=mirror[child], mirror[root]
        root=child
    return

def maxheapify(array,mirror):
    start=((len(array))//2)
    end=len(array)-1
    while start>=0:
        sink(start,array,end,mirror)
        start-=1
    return


#size of register
k=int(input("Please provide a value for k: "))

#optaining value of t as the possible memory locations
t=int(input("Please provide a value for t: "))

#number n for a1,a2, ...,an
n=int(input("Please provide a value for n: "))

#randomly optain a_i as a value from 1-t insert and in array a_n
a_n=[]
for i in range(0,n):
    a_n.append(random.randint(1,t))

#printing array a_n
print("a1,....,an: ")
for i in range(0,n):
    print(a_n[i])

#make null register of 0s
reg=[]
for i in range(0,k):
    reg.append(0)

#make array of size t of all memory locations currently in the register
in_register=[]
for i in range(0,t+1):
    in_register.append(0)
count_in_reg=0


#size array of next occurrances same size as register
next_occur=[]
for i in range(0,k):
    next_occur.append(0)


#scan through a_n putting into register based on three cases

num_evictions=0
num_fetches=0

for i in range(0,len(a_n)):
    #case 1: a_n in register
    if in_register[a_n[i]]==1:
        continue
    #case 2: a_n not in register but register is not full
    elif ((count_in_reg<k) and in_register[a_n[i]]==0):
        reg[count_in_reg]=a_n[i]
        in_register[a_n[i]]=1
        count_in_reg=count_in_reg+1
        num_fetches=num_fetches+1

        #printing current register
        print("current register. Zeros indicate free slot in register: ")
        for b in range (0,len(reg)):
            print(reg[b])
    else:
        #case 3: register is full and a_n not in register
        evict=-1
        #building next occurence array
        for r in range(0,len(reg)):
            for l in range(i,n):
                if a_n[l]==reg[r]:
                    next_occur[r]=l
                    break
                #doesnt occur again can immediate evict
                elif (l==(n-1) and a_n[l]!=reg[r]):
                    evict=r
        #this means we found an element without another occurence
        if evict>-1:
            print("current register: ")
            for q in range(0,len(reg)):
                print (reg[q])
                
            in_register[reg[evict]]=0

            print("evicting:",reg[evict], "because it does not occur again")
            print("replacing with: ", a_n[i])
            print("")
            reg[evict]=a_n[i]
            in_register[a_n[i]]=1
            num_evictions=num_evictions+1
            num_fetches=num_fetches+1
        else:
            print("current register: ")
            for q in range(0,len(reg)):
                print (reg[q])

            #build a max heap with register mirroring next_occurence 
            maxheapify(next_occur,reg)
            print("evicting: ",reg[0])
            print(reg[0], "had the farthest next occurence at index", next_occur[0])
            print("replacing with: ", a_n[i])
            print("")
            in_register[reg[0]]=0
            reg[0]=a_n[i]
            in_register[a_n[i]]=1
            num_evictions=num_evictions+1
            num_fetches=num_fetches+1
    
    

print("number of evictions ", num_evictions)
print("number of fetches ", num_fetches)
print("final register: ")
for b in range(0,len(reg)):
    print(reg[b])

