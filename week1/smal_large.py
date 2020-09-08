largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        if smallest is None:
            smallest = int(num)
        if largest is None:    
            largest = int(num)
    except:
        print('Invalid input')
        continue
    if (int(smallest) > int(num)):
    	smallest = num
    if (int(largest) < int(num)):
    	largest = num
    # print(smallest)
print("Maximum is ", largest)
print("Minimum is ", smallest)