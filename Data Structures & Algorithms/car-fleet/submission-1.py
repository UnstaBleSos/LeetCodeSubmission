class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # check whether the lenght of position and speed matches or not
        if len(position) != len(speed):
            return False
        # create a stack
        stack=[]
        cars = list(zip(position,speed))

        sortedCars = sorted(cars,reverse=True)

        for x in sortedCars:
            time1 = (target - x[0])/x[1]
            print(time1)

            if len(stack) == 0:
                stack.append(time1)
            else:
               if time1 > stack[-1]:
                stack.append(time1)
        
        return len(stack)


