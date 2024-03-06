"""
@RELATION monk1
@ATTRIBUTE attribute#1  {1,2,3}
@ATTRIBUTE attribute#2  {1,2,3}
@ATTRIBUTE attribute#3  {1,2}
@ATTRIBUTE attribute#4  {1,2,3}
@ATTRIBUTE attribute#5  {1,2,3,4}
@ATTRIBUTE attribute#6  {1,2}
@ATTRIBUTE class {0, 1}
@DATA
"""
import os
def main():
    
    #Access the data
    
    data = []
    file = "shakespeare.txt"
    with open("monk1.txt", "r", encoding="utf-8") as f:
        for i in range(124):
            try:
                data.append(list(f.readline().replace("\n","").split(',')))
            except:
                print("Reached EOF")
    
    #Process the data based on specified rules
    #Rules found : 
   
   """
    1. attribute#5=1 29 ==> class=1 29    conf:(1)
    2. attribute#2=2 attribute#3=1 23 ==> cluster=cluster1 23    conf:(1)
    3. attribute#2=2 attribute#6=2 23 ==> cluster=cluster1 23    conf:(1)
    4. attribute#1=3 attribute#2=3 17 ==> class=1 17    conf:(1)
    5. attribute#3=1 attribute#5=1 17 ==> class=1 17    conf:(1)
    6. attribute#3=1 attribute#5=4 17 ==> cluster=cluster1 17    conf:(1)
    7. attribute#5=1 cluster=cluster1 17 ==> class=1 17    conf:(1)
    8. attribute#5=1 attribute#6=1 16 ==> class=1 16    conf:(1)
    9. attribute#1=2 attribute#2=2 15 ==> class=1 15    conf:(1)
    10. attribute#2=2 attribute#3=1 attribute#6=2 14 ==> cluster=cluster1 14    conf:(1)
    11. attribute#1=3 attribute#5=1 13 ==> class=1 13    conf:(1)
    12. attribute#5=1 attribute#6=2 13 ==> class=1 13    conf:(1)
    13. attribute#1=2 attribute#2=2 cluster=cluster1 13 ==> class=1 13    conf:(1)
    14. attribute#2=2 attribute#3=1 class=1 13 ==> cluster=cluster1 13    conf:(1)
    15. attribute#3=1 attribute#5=1 cluster=cluster1 13 ==> class=1 13    conf:(1)
    16. attribute#3=1 attribute#5=4 class=0 13 ==> cluster=cluster1 13    conf:(1)
    17. attribute#5=4 attribute#6=2 class=0 13 ==> cluster=cluster1 13    conf:(1)
    18. attribute#2=3 attribute#5=1 12 ==> class=1 12    conf:(1)
    19. attribute#3=2 attribute#5=1 12 ==> class=1 12    conf:(1)
   """ 

    class1 = []
    class0 = []
    for i in range(124):
        #rule 1
        if (int(data[i][4]) == 1                            #1. attribute#5=1 29 ==> class=1 29    conf:(1)
        | (int(data[i][1]) == 2 and int(data[i][2]) == 1)   #2. attribute#2=2 attribute#3=1 23 ==> cluster=cluster1 23    conf:(1)
        | (int(data[i][1]) == 2 and int(data[i][5]) == 2)   #3. attribute#2=2 attribute#6=2 23 ==> cluster=cluster1 23    conf:(1)
        | (int(data[i][2]) == 3 and int(data[i][1])== 3)):  #4. attribute#1=3 attribute#2=3 17 ==> class=1 17    conf:(1)
            class1.append(data[i])
        
    # Count how many classes were identified correclty or not
    print(f"Number of objects selected: {len(class1)}")
    print(f"Number of class 1 in that selection: {(sum(int(row[6]) for row in class1))}")
    
    return 0

main()
