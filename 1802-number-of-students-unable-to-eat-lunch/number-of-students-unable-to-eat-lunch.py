class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        j=0
        while(students and j<len(sandwiches)):
            if (students[0]==sandwiches[0]):
                students.pop(0)
                sandwiches.pop(0)
                j = 0
            else:
                students.append(students.pop(0))
                j += 1

        return len(students) 
