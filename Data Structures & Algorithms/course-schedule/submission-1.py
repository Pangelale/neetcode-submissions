class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        path = set()
        mapping = {}
        checked = set()

        for course in range(numCourses):
            mapping[course] = []

        for i in range(len(prerequisites)):
            course = prerequisites[i][0]
            prereq = prerequisites[i][1]

            mapping[course].append(prereq)

        def check(course):
            if course in path:
                return False
            
            if course in checked:
                return True

            path.add(course)

            for prereq in mapping[course]:
                if not check(prereq):
                    return False

            path.remove(course)
            checked.add(course)
            return True

        for course in range(numCourses):
            current_answer = check(course)
            if current_answer == False:
                return False
        
        return True
            