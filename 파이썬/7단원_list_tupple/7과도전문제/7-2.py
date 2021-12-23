list1 = [3,5,7]
list2 = [2,3,4,5,6]
for i in range(len(list1)): #range함수를 이용한다.
    for k in range(len(list2)):
        print(list1[i],'*',list2[k],'=',list1[i] * list2[k])
   
 