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

    # Define workout plans for each day
    workout_plans = {
        "Monday": PullDay(),
        "Tuesday": Biceps(),
        "Wednesday": LegsWorkout(),
        "Thursday": PushDay(),
        "Friday": Shoulders(),
        "Saturday": Abs()
    }

    # Generate the workout plan based on the day of the week
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


@app.before_request
def store_todays_workout_in_session():
    # Get the current date (e.g., '2024-09-07')
    today_date = datetime.datetime.now().strftime("%Y-%m-%d")

    # Check if today's date and workout plan are already in the session
    if 'workout_plan_date' not in session or session['workout_plan_date'] != today_date:
        # If not, generate a new workout plan and store it in session
        today, workout_plan = get_todays_workout()
        session['workout_plan_date'] = today_date
        session['workout_plan'] = workout_plan
        session['today'] = today  # Store the current day (e.g., 'Monday')


@app.route('/')
def index():
    # Retrieve the stored workout plan and day from the session
    today = session.get('today', 'No workout day')
    workout_plan = session.get('workout_plan', {})
    return render_template('index.html', today=today, workout_plan=workout_plan)


@app.route('/checkin', methods=['GET', 'POST'])
def checkin():
    if request.method == 'POST':
        completed_exercises = request.form.getlist('completed_workouts')
        # Save completed_exercises to session or database if needed
        flash("Your check-in has been recorded!")
        return redirect(url_for('index'))

    # Retrieve the stored workout plan and day from the session
    today = session.get('today', 'No workout day')
    workout_plan = session.get('workout_plan', {})
    completed_exercises = request.form.getlist('completed_workouts')

    return render_template('checkin.html', today=today, workout_plan=workout_plan,
                           completed_workouts=completed_exercises)

@app.route('/custom', methods=['GET', 'POST'])
def custom_workout():
    if request.method == 'POST':
        selected_group = request.form.get('muscle_group')

        # Generate workout plan based on selected group
        if selected_group == "pull":
            workout_plan = PullDay().pullDay()
        elif selected_group == "push":
            workout_plan = PushDay().pushDay()
        elif selected_group == "legs":
            workout_plan = LegsWorkout().legDay()
        elif selected_group == "biceps":
            workout_plan = Biceps().bicepDay()
        elif selected_group == "abs":
            workout_plan = Abs().abs()
        elif selected_group == "shoulders":
            workout_plan = Shoulders().shoulderDay()
        else:
            workout_plan = {}

        # Store the custom workout in session
        session['workout_plan'] = workout_plan
        session['today'] = selected_group.capitalize()

        return redirect(url_for('index'))  # Redirect back to the homepage with the custom workout

    return render_template('muscle_groups.html')


@app.route('/reset_default', methods=['POST'])
def reset_default():
    # Regenerate today's workout and store it in the session
    today, workout_plan = get_todays_workout()
    session['workout_plan'] = workout_plan
    session['today'] = today  # Store the default day

    # Redirect to the index page to show the default workout
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
