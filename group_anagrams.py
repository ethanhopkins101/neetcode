'''
Given an array of strings strs, group all anagrams together into sublists.
You may return the output in any order.
An anagram is a string that contains the exact same characters as another string,
but the order of the characters can be different.

Example 1:
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
'''
from typing import List
class GroupAnagram:
    #Defining the group_anagram method
    def group_anagram(self,input:List[str])->List[List]:
        #defining two dictionaries to saperate anagrams and their indices
        temp1={}
        temp2={}
        result=[]
        #filling up the first dictionary
        for i in range(input):
            temp1[i]={} #dictionary of nested dictionaries (keys are indices of input)
            for j in input[i]:
                if j in temp1[i].keys():
                    temp1[i][j]+=1
                else:
                    temp1[i][j]=1
        result_index=1
        for k1,v1 in temp1.items():
            temp2[result_index]=[k1] # dictionary of nested lists (keys are indices of result , vals are lists of indices of input)
            for k2,v2 in temp1.items():
                if (k1!=k2) and (v1==v2):
                    temp2[result_index].append(k2)

            
