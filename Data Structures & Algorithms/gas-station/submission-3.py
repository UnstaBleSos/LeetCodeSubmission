class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalGas = sum(gas)
        totalCost = sum(cost)

        if totalGas < totalCost:
            return -1 
        start = 0
        current_balance = 0 
        for i in range(len(gas)):
            net = gas[i] - cost[i]
            current_balance += net

            if current_balance < 0:
                start = i +1 
                current_balance = 0
                
        return start