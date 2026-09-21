class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Dictionary initialization
        graph = {course: [] for course in range(numCourses)}

        # Path
        course_prereqnum = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            course_prereqnum[course] += 1
        
        queue = deque()

        courses_ordering = []
        for course in range(numCourses):
            if course_prereqnum[course] == 0:
                queue.append(course)

        while queue:
            course = queue.popleft()
            courses_ordering.append(course)

            for next_course in graph[course]:
                course_prereqnum[next_course] -= 1
                if course_prereqnum[next_course] == 0:
                    queue.append(next_course)
        
        if len(courses_ordering) == numCourses:
            return courses_ordering
        else:
            return []
        