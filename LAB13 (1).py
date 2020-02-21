#LAB 13
#Due Date: 11/18/2018, 11:59PM
########################################
#                                      
# Name: Jessica Walsh		
# Collaboration Statement: I completed this assignment alone           
#
########################################

def merge(list1, list2):
	#write your code here
		i=0
		j=0
		result=[]

		while (len(result)<(len(list1)+len(list2))):
			if list1[i]<list2[j]:
				result.append(list1[i])
				i=i+1
			else:
				result.append(list2[j])
				j=j+1
			if (i==len(list1) or j==len(list2)):
				result.extend(list1[i:] or list2[j:])
				break
		return result
	



def mergeSort(numList):
    if len(numList)<2:
            return numList
    mid=int(len(numList)/2)
    list1=mergeSort(numList[:mid])
    list2=mergeSort(numList[mid:])
    return merge(list1,list2)
