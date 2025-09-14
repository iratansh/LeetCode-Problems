"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # input format: [a, b, [c, d]] such that a is the id of the current node, b is the importance of the current node and c, d are the left and right childs respectively
        # need to basically sum over the imporance of the subtree 

        mapping = {employee.id: employee for employee in employees}
        
        def dfs(emp_id):
            employee = mapping[emp_id]
            total = employee.importance
            for sub_id in employee.subordinates:
                total += dfs(sub_id)
            return total
        
        
        return dfs(id)
        
        
