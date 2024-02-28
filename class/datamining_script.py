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
    
    
    print(data) 
    
    #Process the data based on specified rules
    
      
        
    return 0

main()
