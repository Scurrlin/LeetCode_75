class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        k = new = set(rooms[0])
        while len(k) < len(rooms) - 1:
            new = reduce(
                lambda a, b: a.union(b), (set(rooms[n]) for n in new), set()
            ) - k.union({0})
            if not new:
                return False
            k.update(new)
        return True