class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # this means that it will be 1 of 2 nodes in edges[0], either edge[0][0] or edges[0][1]
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        else:
            return edges[0][1]
