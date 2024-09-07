from flask import Flask, render_template, request, redirect, url_for, flash, session
import datetime
from exercises.pullDay import PullDay
from exercises.pushDay import PushDay
from exercises.legDay import LegsWorkout
from exercises.biceps import Biceps
from exercises.abs import Abs
from exercises.shoulders import Shoulders
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Securely generated secret key

def get_todays_workout():
    day_of_week = datetime.datetime.now().strftime("%A")
    workout_plans = {
        "Monday": PullDay(),
        "Tuesday": Biceps(),
        "Wednesday": LegsWorkout(),
        "Thursday": PushDay(),
        "Friday": Shoulders(),
        "Saturday": Abs()
    }

    workout_plan = workout_plans.get(day_of_week, None)
    if workout_plan:
        if day_of_week == "Monday":
            plan = workout_plan.pullDay()
        elif day_of_week == "Tuesday":
            plan = workout_plan.bicepDay()
        elif day_of_week == "Wednesday":
            plan = workout_plan.legDay()
        elif day_of_week == "Thursday":
            plan = workout_plan.pushDay()
        elif day_of_week == "Friday":
            plan = workout_plan.shoulderDay()
        elif day_of_week == "Saturday":
            plan = workout_plan.abs()
        else:
            plan = {}
        return day_of_week, plan
    return day_of_week, {}

# Global Variable declaration for workout
today, workout_plan = get_todays_workout()

@app.route('/')
def index():
    return render_template('index.html', today=today, workout_plan=workout_plan)

@app.route('/checkin', methods=['GET', 'POST'])
def checkin():
    if request.method == 'POST':
        completed_exercises = request.form.getlist('completed_workouts')
        # Save completed_exercises to session or database if needed
        flash("Your check-in has been recorded!")
        return redirect(url_for('index'))

    completed_exercises = request.form.getlist('completed_workouts')
    return render_template('checkin.html', today=today, workout_plan=workout_plan, completed_workouts=completed_exercises)

if __name__ == "__main__":
    app.run(debug=True)
