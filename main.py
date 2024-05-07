# main.py
from flask import Flask, render_template, request
from config import Config
from models import UniversityApp

# Initialize Flask app
app = Flask(__name__)

# Instantiate UniversityApp object
university_app = UniversityApp()
university_app.load_data()

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/course_schedule', methods=['GET', 'POST'])
def course_schedule():
    if request.method == 'POST':
        course_id = request.form['course_id']
        course_schedule = university_app.get_course_schedule(course_id)
        if course_schedule:
            return render_template('course_schedule.html', course_id=course_id, schedule=course_schedule)
        else:
            return "Course not found!"
    return render_template('course_form.html')

if __name__ == "__main__":
    app.run(debug=True)
