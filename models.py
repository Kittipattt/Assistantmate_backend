import csv
import os


class Course:
    def __init__(self, course_id, course_name, major, section, day, time, teacher):
        self.course_id = course_id
        self.course_name = course_name
        self.major = major
        self.section = section
        self.day = day
        self.time = time
        self.teacher = teacher


class UniversityApp:
    def __init__(self):
        self.courses = {}

    @classmethod
    def load_data(cls):
        file_path = os.path.join("resource", "course_data.csv")
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                course_id = int(row['CourseId'])  # Convert to integer
                course_name = row['CourseName']
                major = row['major']
                section = row['section']
                day = row['day']
                time = row['time']
                teacher = row['Teacher']
                cls.courses[course_id] = Course(course_id, course_name, major, section, day, time, teacher)

    def get_course_schedule(self, course_id):
        return self.courses.get(course_id, None)


# Usage
university_app = UniversityApp()
university_app.load_data()
