import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        distance = [a - b for a, b in zip([target]*len(position), position)]
        time = [a/b for a, b in zip(distance, speed)]
        tot = [[a, b] for a, b in zip(position, time)]
        tot.sort(reverse=True)
        print(tot)
        print(position)
        print(distance)
        print(time)

        fleets = 0
        curr_position = float('inf')
        max_time = 0
        for i in tot:
            if i[0] < curr_position and i[1] > max_time:
                fleets += 1
                curr_position = i[0]
                max_time = i[1]

        
        return fleets