import random

class PullDay:
    def __init__(self):
        self.lats = {
            "Lat Pulldown": "3x12 (130-140-150)",
            "V bar Lat Pulldown": "3x8 (130-135-140)",
            "Seated Row Machine": "3x10 (100-105-110)",
            "Cable Rope Pulldown": "3x10 (47-50-52)",
            "Wide Hand Pullups Body weight": "9-8-8",
            "Underhand close grip Pulldown": "3x10 (130-135-140)"
        }

        self.traps = {
            "Dumbbell Shrugs": "3x12 (50-55-60)",
            "EZ bar Upright Row": "3x10 (60-65-70)",
            "Face Pulls (with rope)": "3x15 (40-45-50)",
            "Rear Delt Fly (with rope)": "3x15 (25-30-35)"
        }

        self.rearDelts = {
            "Bent-Over Row": "3x10 (100-105-110)",
            "Face Pulls (with rope)": "3x15 (40-45-50)",
            "Seated Bent-over lateral raise": "3x12 (15-20-25)",
            "Rear Delt Fly (with rope)": "3x15 (25-30-35)"
        }

        self.spinalErectors = {
            "Deadlift": "3x5 (200-210-220)",
            "Bent-Over Row": "3x10 (100-105-110)",
            "Back Extensions": "3x12 (Bodyweight)",
            "Glute Bridge": "3x10 (Bodyweight)",
            "Prone Superman": "3x15 (Bodyweight)"
        }

        # Initialize the workout plan
        self.pullDayWOplan = {}

    def returnExercise(self, muscle_group):
        random_key = random.choice(list(muscle_group.keys()))
        random_value = muscle_group[random_key]
        return f"{random_key} - {random_value}"

    def pullDay(self):
        latsWO = self.returnExercise(self.lats)
        latsWO2 = self.returnExercise(self.lats)
        spinalErectorsWO = self.returnExercise(self.spinalErectors)
        spinalErectorsWO2 = self.returnExercise(self.spinalErectors)
        rearDeltWO = self.returnExercise(self.rearDelts)
        trapsWO = self.returnExercise(self.traps)

        self.pullDayWOplan["Lats"] = latsWO
        self.pullDayWOplan["Lats2"] = latsWO2
        self.pullDayWOplan["Spinal Erectors"] = spinalErectorsWO
        self.pullDayWOplan["Spinal Erectors2"] = spinalErectorsWO2
        self.pullDayWOplan["Rear Delts"] = rearDeltWO
        self.pullDayWOplan["Traps"] = trapsWO

        return self.pullDayWOplan

# Example usage
if __name__ == "__main__":
    workout = PullDay()
    plan = workout.pullDay()
    print(plan)
