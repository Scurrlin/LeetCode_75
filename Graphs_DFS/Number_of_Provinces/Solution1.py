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