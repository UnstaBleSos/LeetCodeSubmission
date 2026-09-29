class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        freq= {}
        for i in range(len(hand)):
            if hand[i] not in freq:
                freq[hand[i]] = 0
            freq[hand[i]] += 1

        groups = len(hand) // groupSize
        while groups > 0:
            smallest = float("inf")
            for card in freq:
                if card < smallest and freq[card] > 0:
                    smallest = card

            for i in range(groupSize):
                card = smallest + i

                if card not in freq or freq[card] == 0 :
                    return False

                freq[card] -= 1
            
            groups -= 1 

        return True


        