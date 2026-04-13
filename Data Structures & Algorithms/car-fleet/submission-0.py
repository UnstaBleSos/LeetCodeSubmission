class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # check whether the lenght of position and speed matches or not
        if len(position) != len(speed):
            return False
        # create a stack
        stack=[]
        # sort the position of the cars
        sortedposition = sorted(position)
        #sort the speed of the cars 
        sortedspeed = sorted(speed)

        # running the loop in reverse
        for x in range(len(sortedposition)-1,-1,-1):
            # add the largetst position car on the stack
            stack.append(sortedposition[x])

            if len(stack) == 2:
                second = stack[-1]
                first = stack[0]
                print(first,second)
                time2= (target-second)/sortedspeed[-1]
                time1=(target-first)/sortedspeed[0]
                
                if time2 <= time1:
                    stack.pop()
               
           

        return len(stack)

