points={ 'A' : 5.0, 'B': 4.0, 'C': 3.0, 'D' : 2.0, 'E' : 1.0, 'F': 0.0 }
course_units={ 'C1' : 2.0, 'C2': 3.0, 'C3': 2.0, 'C4' : 1.0, 'C5' : 1.0, 'C6': 3.0 }

# def split_even_placed(delimiter, s):
#     s = s.strip()
#     delimiter_count = 0
#     new_list=[]
#     for figure in s:
#         if figure == ' ':
#             delimiter_count += 1
#             if delimiter_count % 2 == 0 and delimiter_count > 0:
                
    

def gpa_calculator():
    scores = input()
    split_scores = scores.split(',')
    entered_courses = []
    score_sum = 0
    course_unit_sum=0
    for score in split_scores:
        score         = score.strip()
        course, grade = score.split()
        course, grade = course.upper(), grade.upper()
        if grade not in points:
            return 'Invalid grade:' + grade
        if course not in course_units:
            return 'Invalid course code:' + course
        if course in entered_courses:
            print('Ignoring duplicate entry: ' + course)
            continue
        score_sum += points[grade] * course_units[course]
        course_unit_sum+= course_units[course]
        entered_courses.append(course)
    return score_sum/course_unit_sum


print(gpa_calculator())
    