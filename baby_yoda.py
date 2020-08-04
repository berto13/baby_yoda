def solution(x, y, d):

    #initialize number of steps
    num_steps = 0
    #calculate initial distance between x and y
    initial_distance = y - x
    #loop to add steps of distance d to x, while x is less than y
    while x < y:
        #if d is 0 return
        if d == 0:
            return "Baby Yoda is not moving, he is dead. We have lost the Galactic Civil War! \n"
        #add d to x to move
        x = x + d
        num_steps += 1
        #calculate current distance to see if baby Yoda is moving closer to the destination
        current_distance = y - x
        #Verify and return if there is no movement progress
        if current_distance > initial_distance:
            return "Yoda is moving away from y, call Luke Skywalker!"
        
    return "baby Yoda would have to take a minimal of " + str(num_steps) + " steps."
	
	
#Error handlers for incorrect inputs
try:
    #get user inputs for x, y and d
    x = int(input("Enter value of x: "))
    y = int(input("Enter value of y: "))
    d = int(input("Enter value of d: "))

    answer = solution(x, y, d)
    print(answer)
except:
    print("Make sure your inputs are numbers, check yourself!")
