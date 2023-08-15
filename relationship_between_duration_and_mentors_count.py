def main(courses, mentors, durations):
    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title":course, "mentors":mentor, "duration":duration}
        courses_list.append(course_dict)

    c_l_1 = sorted([[j["duration"], i] for i, j in enumerate(courses_list)], key=lambda x: x[0])
    c_l_2 = sorted([[len(j["mentors"]), i] for i, j in enumerate(courses_list)], key=lambda x: x[0])

    return {
        "relationship": c_l_1 == c_l_2,
        "courseDurationsList": list(map(lambda x: x[1], c_l_1)),
        "courseMentorsCountList": list(map(lambda x: x[1], c_l_2))
    }