class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_senators = deque()
        d_senators = deque()

        for i, s in enumerate(senate):
            if s == 'R':
                r_senators.append(i)
            else:
                d_senators.append(i)

        while r_senators and d_senators:
            r_index = r_senators.popleft()
            d_index = d_senators.popleft()

            if r_index < d_index:
                r_senators.append(r_index + len(senate))
            else:
                d_senators.append(d_index + len(senate))

        return "Radiant" if r_senators else "Dire"
