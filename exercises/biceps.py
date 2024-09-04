import random

class Biceps:
    def __init__(self):

        self.bicepsShortHead = {
            "Reverse curls": "3x10 (30-35-40)",
            "Hammer curls": "3x12 (25-30-35)",
            "Reverse grip - EZ bar curls": "3x10 (40-45-50)",
            "Barbell curls with wide grip": "3x10 (40-45-50)"
        }

        self.bicepsLongHead = {
            "PRONATED CROSS BODY CURL": "3x10 (20-25-30)",
            "Chin-up": "3x12 (Bodyweight)",
            "Concentration Curl": "3x12 (15-20-25)",
            "Preacher Curl": "3x10 (30-35-40)",
            "Bayesian Cable Curl": "3x12 (20-25-30)",
            "Close-Grip Barbell Curl": "3x10 (40-45-50)"
        }

        self.brachialis = {
            "Hammer Curl": "3x12 (25-30-35)",
            "Crossbody Hammer Curl": "3x10 (25-30-35)",
            "NARROW GRIP PULL UP": "3x10 (Bodyweight)"
        }

        # Initialize the workout plan
        self.bicepsWOPlan = {}

    def returnExercise(self, muscle_group):
        random_key = random.choice(list(muscle_group.keys()))
        random_value = muscle_group[random_key]
        return f"{random_key} - {random_value}"

    def bicepDay(self):
        bicepsLH1 = self.returnExercise(self.bicepsLongHead)
        bicepsLH2 = self.returnExercise(self.bicepsLongHead)
        bicepsSH1 = self.returnExercise(self.bicepsShortHead)
        bicepsSH2 = self.returnExercise(self.bicepsShortHead)
        brachialis = self.returnExercise(self.brachialis)

        self.bicepsWOPlan["Biceps Long Head 1"] = bicepsLH1
        self.bicepsWOPlan["Biceps Long Head 2"] = bicepsLH2
        self.bicepsWOPlan["Biceps Short Head 1"] = bicepsSH1
        self.bicepsWOPlan["Biceps Short Head 2"] = bicepsSH2
        self.bicepsWOPlan["Brachialis"] = brachialis

        return self.bicepsWOPlan

    # Example usage
if __name__ == "__main__":
    workout = Biceps()
    plan = workout.bicepDay()
    print(plan)


