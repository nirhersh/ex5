import json
import os

def names_of_registered_students(input_json_path, course_name):
    """
    This function returns a list of the names of the students who registered for
    the course with the name "course_name".

    :param input_json_path: Path of the students database json file.
    :param course_name: The name of the course.
    :return: List of the names of the students.
    """
    with open(input_json_path, "r") as f:
        students_info = json.load(f)
    return [info["student_name"] for info in students_info.values() if course_name in info["registered_courses"]]


def enrollment_numbers(input_json_path, output_file_path):
    """
    This function writes all the course names and the number of enrolled
    student in ascending order to the output file in the given path.

    :param input_json_path: Path of the students database json file.
    :param output_file_path: Path of the output text file.
    """
    with open(input_json_path, "r") as f_input, open(output_file_path, "w") as f_output:
        students_info = json.load(f_input)
        out_dict = {course : 0 for info in students_info.values() for course in info["registered_courses"]}
        for info in students_info.values():
            for course in info["registered_courses"]:
                out_dict[course] += 1
        for course in sorted(out_dict.keys()):
            f_output.write("\"{}\" {}\n".format(course, out_dict[course]))
    





def courses_for_lecturers(json_directory_path, output_json_path):
    """
    This function writes the courses given by each lecturer in json format.

    :param json_directory_path: Path of the semsters_data files.
    :param output_json_path: Path of the output json file.
    """
    file_names = [os.path.join(json_directory_path, file) for file in os.listdir(json_directory_path) if ".json" in os.path.splitext(file)]
    output_dict = dict()
    for file in file_names:
        with open(file, "r") as f:
            semester_info = json.load(f)
        for course_info in semester_info.values():
            for lecturer in course_info["lecturers"]:
                if(lecturer in output_dict.keys()):
                    if(course_info["course_name"] not in output_dict[lecturer]):
                        output_dict[lecturer].append(course_info["course_name"])
                else: 
                    output_dict[lecturer] = [course_info["course_name"]]
    with open(output_json_path, "w") as f:
        json.dump(output_dict, f, indent=4)

    

if __name__ == "__main__":
    students = names_of_registered_students("students_database.json", "Introduction to Systems Programming")
    print(students)
    enrollment_numbers("students_database.json", "out.txt")
    courses_for_lecturers("semesters_databases", "output.txt")

