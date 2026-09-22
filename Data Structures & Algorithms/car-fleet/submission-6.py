class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # create a pair for each car that gives position and speed
        pairs = sorted(zip(position,speed), reverse=True)
        # stack for tracking fleets
        fleets = []
        
        for pos,spd in pairs:
            time = (target - pos) / spd
            if not fleets or (time > fleets[-1]):
                fleets.append(time)
        
        return len(fleets)