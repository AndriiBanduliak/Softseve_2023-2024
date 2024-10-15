import json


class Student:
    def __init__(self, full_name, avg_rank, courses):
        self.full_name = full_name
        self.avg_rank = avg_rank
        self.courses = courses

    def __str__(self):
        return f"{self.full_name} ({self.avg_rank}): {self.courses}"

    def to_dict(self):
        return {
            "full_name": self.full_name,
            "avg_rank": self.avg_rank,
            "courses": self.courses
        }

    @classmethod
    def from_json(cls, json_file):
        with open(json_file, 'r') as file:
            data = json.load(file)
            if isinstance(data, list):  # If the file contains a list of students
                return [cls(entry['full_name'], entry['avg_rank'], entry['courses']) for entry in data]
            else:  # If the file contains a single student
                return cls(data['full_name'], data['avg_rank'], data['courses'])

    def serialize_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.to_dict(), file)


class Group:
    def __init__(self, title, students):
        self.title = title
        self.students = students

    def __str__(self):
        student_info = [f"{student.full_name} ({student.avg_rank}): {
            student.courses}" for student in self.students]
        return f"{self.title}: {student_info}"

    def to_dict(self):
        return {
            "title": self.title,
            "students": [student.to_dict() for student in self.students]
        }

    @classmethod
    def serialize_to_json(cls, list_of_groups, filename):
        data = [group.to_dict() for group in list_of_groups]
        with open(filename, 'w') as file:
            json.dump(data, file)

    @classmethod
    def create_group_from_file(cls, students_file):
        title = students_file.split('.')[0]
        students = []
        with open(students_file, 'r') as file:
            students_data = json.load(file)
            if isinstance(students_data, list):
                for student_data in students_data:
                    student = Student(
                        student_data['full_name'], student_data['avg_rank'], student_data['courses'])
                    students.append(student)
            else:
                student = Student(
                    students_data['full_name'], students_data['avg_rank'], students_data['courses'])
                students.append(student)
        return cls(title, students)
