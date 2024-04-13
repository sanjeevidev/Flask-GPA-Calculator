from flask import Flask, render_template, request

app = Flask(__name__)

# Dictionary of credits for each course
credit = {'pspp': 3, 'english': 3, 'maths':4, 'physics':3, 'chemistry':3, 'pspp_lab':2, 'phy_che_lab':2}

# Dictionary of grade points for each grade
course_grade = {'O': 10, 'A+': 9, 'A': 8, 'B+': 7, 'B':6,'C': 5}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_score', methods=['POST'])
def calculate_score():
    total_score = 0
    # total_scores =[]
    total_credit = 0
    
    for i in range(1, 8):
        course = request.form.get(f'course{i}')
        grade = request.form.get(f'grade{i}')
        
        if course in credit and grade in course_grade:
            course_credit = credit[course]
            grade_points = course_grade[grade]
            total_score += course_credit * grade_points
            total_credit += course_credit
        elif course and grade:
            return "Invalid course or grade entered."
                
    return f"The final cumulative score is: {total_score / total_credit}"
    # return f"Your score -> {total_scores}"

if __name__ == '__main__':
    app.run(debug=True)