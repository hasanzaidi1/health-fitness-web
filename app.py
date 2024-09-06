from flask import Flask, render_template, request, redirect, url_for, flash, session
import datetime
from exercises.pullDay import PullDay
from exercises.pushDay import PushDay
from exercises.legDay import LegsWorkout
from exercises.biceps import Biceps
from exercises.shoulders import Shoulders
import os
import pymongo

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Securely generated secret key

# MongoDB connection
mongo_uri = os.getenv("MONGO_URI")
if not mongo_uri:
    raise ValueError("No MongoDB URI found in environment variables.")
client = pymongo.MongoClient(mongo_uri)
db = client['Health_Fitness_app']  # Replace 'workout_db' with your desired database name
skipped_collection = db['workoutStatus']  # Collection for storing skipped exercises

def get_todays_workout():
    day_of_week = datetime.datetime.now().strftime("%A")
    workout_plans = {
        "Monday": PullDay(),
        "Tuesday": Biceps(),
        "Wednesday": LegsWorkout(),
        "Thursday": PushDay(),
        "Friday": Shoulders(),
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
    return current_time >= datetime.time(20, 30)

# Global Variable declaration for workout
today, workout_plan = get_todays_workout()

@app.route('/')
def index():
    if is_end_of_day():
        return redirect(url_for('end_of_day_checkin'))

    return render_template('index.html', today=today, workout_plan=workout_plan)

@app.route('/end_of_day', methods=['GET', 'POST'])
def end_of_day_checkin():
    if request.method == 'POST':
        completed_exercises = request.form.getlist('completed_workouts')  # Get the list of completed exercises

        # Determine the skipped exercises by comparing the full workout plan with completed ones
        skipped_exercises = [exercise for exercise in workout_plan.keys() if exercise not in completed_exercises]

        # If there are skipped exercises, insert them into MongoDB
        if skipped_exercises:
            skipped_entry = {
                "date": datetime.datetime.now(),
                "day": today,
                "skipped_exercises": skipped_exercises
            }
            skipped_collection.insert_one(skipped_entry)  # Insert the skipped exercises into MongoDB
            flash("Skipped exercises have been recorded.")

        # Flash message for successful check-in
        flash("Your check-in has been recorded!")
        return redirect(url_for('index'))


    # Render end of day check-in page
    completed_exercises = request.form.getlist('completed_workouts')
    return render_template('end_of_day.html', today=today, workout_plan=workout_plan, completed_workouts=completed_exercises)

if __name__ == "__main__":
    app.run(debug=True)
