# There are n cities. Some of them are connected, while some are not. If city a
# is connected directly with city b, and city b is connected directly with city
# c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other
# cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the
# ith city and the jth city are directly connected, and isConnected[i][j] = 0
# otherwise.

# Return the total number of provinces.

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        l1 = [0]*len(isConnected[0])
        for i in range(len(l1)):
            l1[i] = i
        
        def get_root(x):
            return l1[x]
        
        def union(x,y):
            Rx = get_root(x)
            Ry = get_root(y)

            if(Rx != Ry):
                for i in range(0,len(l1)):
                    if l1[i] == Ry:
                        l1[i] = Rx

        for i in range(0,len(isConnected)):
            for j in range(i+1,len(isConnected[0])):
                if isConnected[i][j] == 1:
                    union(i,j)
            
        return len(set(l1))