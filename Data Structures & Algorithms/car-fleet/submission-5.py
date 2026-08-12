class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p, s] for p, s in zip(position, speed)]
        cars.sort(reverse=True)
        fleets = []

        # traversing backwards
        for p, s in cars:
            # adding car's arrival time to the stack
            fleets.append((target - p) / s)

            # if the arrival time is before an existing arrival time, they must have collided and become a fleet
            if len(fleets) > 1 and fleets[-1] <= fleets[-2]:
                fleets.pop()
            
        return len(fleets)