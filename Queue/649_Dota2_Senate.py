# In the world of Dota2, there are two parties: the Radiant and the Dire.

# The Dota2 senate consists of senators coming from two parties. Now the Senate
# wants to decide on a change in the Dota2 game. The voting for this change is a
# round-based procedure. In each round, each senator can exercise one of the two
# rights:

# Ban one senator's right: A senator can make another senator lose all his
# rights in this and all the following rounds. Announce the victory: If this
# senator found the senators who still have rights to vote are all from the same
# party, he can announce the victory and decide on the change in the game. Given
# a string senate representing each senator's party belonging. The character 'R'
# and 'D' represent the Radiant party and the Dire party. Then if there are n
# senators, the size of the given string will be n.

# The round-based procedure starts from the first senator to the last senator in
# the given order. This procedure will last until the end of voting. All the
# senators who have lost their rights will be skipped during the procedure.

# Suppose every senator is smart enough and will play the best strategy for his
# own party. Predict which party will finally announce the victory and change
# the Dota2 game. The output should be "Radiant" or "Dire".

from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_senators, d_senators = deque(), deque()
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
