from flask import Flask, render_template, request, redirect, url_for, flash
import datetime
from exercises.pullDay import PullDay
from exercises.pushDay import PushDay
from exercises.legDay import LegsWorkout
from exercises.biceps import Biceps
from exercises.shoulders import Shoulders
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Securely generated secret key


# Define workout plans and their corresponding methods
def get_todays_workout():
    day_of_week = datetime.datetime.now().strftime("%A")
    workout_plans = {
        "Monday": PullDay(),
        "Tuesday": Biceps(),
        "Wednesday": LegsWorkout(),
        "Thursday": PushDay(),
        "Friday": Shoulders(),
        # Add more mappings as needed
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
        else:
            plan = {}
        return day_of_week, plan
    return day_of_week, {}


def is_end_of_day():
    current_time = datetime.datetime.now().time()
    return current_time >= datetime.time(9, 30)


@app.route('/')
def index():
    if is_end_of_day():
        return redirect(url_for('end_of_day_checkin'))

    today, workout_plan = get_todays_workout()
    return render_template('index.html', today=today, workout_plan=workout_plan)


@app.route('/end_of_day', methods=['GET', 'POST'])
def end_of_day_checkin():
    if request.method == 'POST':
        # Handle check-in logic
        completed_exercises = request.form.getlist('completed')
        skipped_exercises = request.form.getlist('skipped')
        flash("Your check-in has been recorded!")
        return redirect(url_for('index'))

    today, workout_plan = get_todays_workout()
    return render_template('end_of_day.html', today=today, workout_plan=workout_plan)


if __name__ == "__main__":
    app.run(debug=True)
