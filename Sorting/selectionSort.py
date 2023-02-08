def swap(arr,i,mini):
	temp = arr[i]
	arr[i] = arr[mini]
	arr[mini] = temp

def selectionSort(arr,n):
	for i in range(n-1):
		mini = i
		for j in range(i+1,n):
			if arr[mini] > arr[j] :
				mini = j
		swap(arr,i,mini)


arr = [2,3,1,5,10,3]
n = len(arr)
print("Unsorted Array:")
print(arr)
selectionSort(arr,n)
print("Sorted Array:")
print(arr)
