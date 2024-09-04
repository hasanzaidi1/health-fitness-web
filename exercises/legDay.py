import random


class LegsWorkout:
    def __init__(self):
        self.legWarmUp = {
            "Jump Lunges": "3x15 (Bodyweight)",
            "Deadlifts": "4x6 (70-80-90kg)",
            "Jump Rope": "3x60 seconds",
            "Resistance Band Side to Side Lunges": "3x12 each side (Resistance Band)"
        }

        self.glutes = {
            "Resistance Band Glute Kick": "3x15 each side (Resistance Band)",
            "Cable Pull Through": "4x12 (30-35-40kg)",
            "Deadlifts": "4x6 (80-90-100kg)",
            "Kettlebell Swing": "3x15 (20-25-30kg)",
            "Hip Thrust": "4x8 (60-70-80kg)",
            "Sumo Deadlift": "4x6 (80-90-100kg)",
            "Reverse Lunges": "3x12 each side (20-25-30kg)",
            "Leg Curls": "3x12 (40-45-50kg)",
            "Toe Up Hip Lift": "3x15 (Bodyweight)",
            "Step Up": "3x12 each side (20-25-30kg)",
            "Toe Down (Stab) Hip Lift": "3x15 (Bodyweight)"
        }

        self.quads = {
            "Leg Press": "4x10 (100-120-140kg)",
            "Leg Extension": "3x12 (40-50-60kg)",
            "Jump Lunges": "3x15 (Bodyweight)",
            "Dumbbell Lunge": "3x12 each side (20-25-30kg)",
            "Dumbbell Rear Lunge": "3x12 each side (20-25-30kg)",
            "Frog Squat": "3x15 (Bodyweight)"
        }

        self.hams = {
            "Deadlifts": "4x6 (80-90-100kg)",
            "Romanian Deadlift": "4x8 (60-70-80kg)",
            "Lying Leg Curls": "3x12 (30-35-40kg)",
            "Seated Ham Curls": "3x12 (40-45-50kg)",
            "Good Mornings": "3x12 (40-50-60kg)",
            "Kettlebell Swing": "3x15 (20-25-30kg)",
            "Stiff-Legged Deadlift": "4x8 (60-70-80kg)",
            "Sumo Deadlifts": "4x6 (80-90-100kg)"
        }

        self.calfs = {
            "Seated Calf Raise": "4x15 (40-50-60kg)",
            "Standing Calf Raise": "4x15 (Bodyweight)",
            "1-½ Calf Raises": "3x15 (Bodyweight)"
        }

        # Initialize the workout plan
        self.legDayWOplan = {}

    def returnExercise(self, muscle_group):
        random_key = random.choice(list(muscle_group.keys()))
        random_value = muscle_group[random_key]
        return f"{random_key} - {random_value}"

    def legDay(self):
        legsWarmUp = self.returnExercise(self.legWarmUp)
        glutes = self.returnExercise(self.glutes)
        glutes2 = self.returnExercise(self.glutes)
        quads = self.returnExercise(self.quads)
        quads2 = self.returnExercise(self.quads)
        hams = self.returnExercise(self.hams)
        calfs = self.returnExercise(self.calfs)


        self.legDayWOplan["Legs Warm Up"] = legsWarmUp
        self.legDayWOplan["Glutes 1"] = glutes
        self.legDayWOplan["Glutes 2"] = glutes2
        self.legDayWOplan["Quads 1"] = quads
        self.legDayWOplan["Quads 2"] = quads2
        self.legDayWOplan["Hams"] = hams
        self.legDayWOplan["Calfs"] = calfs


        return self.legDayWOplan

    # Example usage
if __name__ == "__main__":
    workout = LegsWorkout()
    plan = workout.legDay()
    print(plan)
