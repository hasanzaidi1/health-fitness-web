import random

class PushDay:

    def __init__(self):

        self.upperBodWarmUp = {
            "WEIGHTED PUSHUP": "3x10",
            "DIAMOND PUSHUP": "3x12"
        }

        # Chest day Workout
        self.upperChest = {
            "INCLINE BENCH PRESS": "3x8 (70-75-80)",
            "LOW TO HIGH CABLE CROSSOVER": "3x12 (20-25-30)",
            "Incline Dumbbell Fly": "3x10 (20-25-30)",
            "Dumbbell Pullovers": "3x10 (30-35-40)"
        }

        self.middleChest = {
            "HORIZONTAL CABLE CROSSOVER": "3x12 (20-25-30)",
            "Pectoral Flyes": "3x10 (25-30-35)",
            "Dumbbell Hex Press": "3x10 (30-35-40)",
            "Single-Arm Cable Press-Around": "3x12 (15-20-25)"
        }

        self.lowerChest = {
            "WEIGHTED DIP": "3x8 (Bodyweight + 10-20-30)",
            "HIGH TO LOW CABLE CROSSOVER": "3x12 (20-25-30)",
            "JACKHAMMER PUSHDOWN": "3x10 (25-30-35)",
            "D2 FLEXION CROSSOVER": "3x12 (20-25-30)",
            "Dip Plus": "3x8 (Bodyweight + 20-30-40)"
        }

        # New triceps categories
        self.tricepsLongHead = {
            "LYING TRICEPS EXTENSION": "3x12 (20-25-30)",
            "DRAG PUSHDOWN": "3x12 (25-30-35)",
            "OVERHEAD DUMBBELL TRICEPS EXTENSIONS": "3x10 (20-25-30)",
            "CABLE PUSHAWAY": "3x12 (30-35-40)",
            "Skullcrushers": "3x10 (25-30-35)",
            "SINGLE-ARM CABLE TRICEPS PUSHDOWN": "3x12 (15-20-25)",
            "Cable with Rope Overhead Extensions": "3x10 (20-25-30)"
        }

        self.tricepsMedialHead = {
            "Reverse Grip Cable Pushdown": "3x12 (20-25-30)",
            "Palm Out Bench Dip": "3x12 (Bodyweight)",
            "Dumbbell Tate Press": "3x10 (20-25-30)",
            "Cable Rope Pushdown (Neutral Grip)": "3x12 (25-30-35)",
            "Cable with Rope Overhead Extensions": "3x10 (20-25-30)",
            "diamond push": "3x12 (Bodyweight)"
        }

        self.tricepsLateralHead = {
            "Weighted Dips": "3x10 (Bodyweight + 10-20-30)",
            "Triceps Parallel Dips": "3x12 (Bodyweight)"
        }

        # Initialize the workout plan
        self.pushDayWOplan = {}

    def returnExercise(self, muscle_group):
        random_key = random.choice(list(muscle_group.keys()))
        random_value = muscle_group[random_key]
        return f"{random_key} - {random_value}"

    def pushDay(self):
        warmUp = self.returnExercise(self.upperBodWarmUp)
        upperChest = self.returnExercise(self.upperChest)
        midChest = self.returnExercise(self.middleChest)
        lowerChest = self.returnExercise(self.lowerChest)
        tricepsLong = self.returnExercise(self.tricepsLongHead)
        tricepsLong2 = self.returnExercise(self.tricepsLongHead)
        tricepsLateral = self.returnExercise(self.tricepsLateralHead)
        tricepsMedial = self.returnExercise(self.tricepsMedialHead)
        tricepsMedial2 = self.returnExercise(self.tricepsMedialHead)

        self.pushDayWOplan["Warm-Up"] = warmUp
        self.pushDayWOplan["Upper Chest"] = upperChest
        self.pushDayWOplan["Middle Chest"] = midChest
        self.pushDayWOplan["Lower Chest"] = lowerChest
        self.pushDayWOplan["Triceps Long Head 1"] = tricepsLong
        self.pushDayWOplan["Triceps Long Head 2"] = tricepsLong2
        self.pushDayWOplan["Triceps Lateral Head"] = tricepsLateral
        self.pushDayWOplan["Triceps Medial Head 1"] = tricepsMedial
        self.pushDayWOplan["Triceps Medial Head 2"] = tricepsMedial2

        return self.pushDayWOplan

if __name__ == "__main__":
    workout = PushDay()
    plan = workout.pushDay()
    print(plan)
