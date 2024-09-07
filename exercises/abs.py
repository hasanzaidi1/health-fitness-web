import random


class Abs(object):
    def __init__(self):
        self.absHIIT = {
            "Flutter Kicks": "30s",
            "KTTH (Knees to the Heaven)": "30s",
            "Crunches": "30s",
            "Planks": "(40s-1m)",
            "Leg Circles": "30s",
            "Side Planks": "(30s each side)",
            "Leg Raises": "30s",
            "Russian Twists": "30s 25lbs",
            "Side Toe Touches": "30s"
        }

        self.upperAbs = {
            "Cable Crunches": "3 x Failure",
            "Decline Crunches": "3 x Failure",
            "Planks": "40s to 1m",
            "Crunches": "3 x Failure",
            "High Toe Touches": "3 x Failure"
        }

        self.lowerAbs = {
            "Flutter Kicks": "3 x Failure",
            "KTTH (Knees to the Heaven)": "3 x Failure",
            "Planks": "(40s-1m)",
            "Leg Raises": "3 x Failure"
        }

        self.sideObliques = {
            "Russian Twists": "3 x failure (25-30-35)",
            "Side Planks": "(30s each side)",
            "Side Toe Touches": "3 x Failure"
        }

        # Initialize the workout plan
        self.absWO = {}

    def returnExercise(self, muscle_group):
        if not muscle_group:
            raise ValueError("No exercises left to choose from.")

        # Randomly select an exercise and remove it from the group to prevent repeats
        random_key = random.choice(list(muscle_group.keys()))
        random_value = muscle_group.pop(random_key)
        return f"{random_key} - {random_value}"

    def abs(self):
        # Clone the dictionaries so the original ones are not modified
        sideObliques_copy = self.sideObliques.copy()
        lowerAbs_copy = self.lowerAbs.copy()
        upperAbs_copy = self.upperAbs.copy()
        absHIIT_copy = self.absHIIT.copy()

        # Helper function to safely get exercises
        def safe_return_exercise(group_copy):
            return self.returnExercise(group_copy) if group_copy else "No exercise available"

        sideObliques1 = safe_return_exercise(sideObliques_copy)
        sideObliques2 = safe_return_exercise(sideObliques_copy)
        lowerAbs1 = safe_return_exercise(lowerAbs_copy)
        lowerAbs2 = safe_return_exercise(lowerAbs_copy)
        upperAbs1 = safe_return_exercise(upperAbs_copy)
        upperAbs2 = safe_return_exercise(upperAbs_copy)
        HIIT1 = safe_return_exercise(absHIIT_copy)
        HIIT2 = safe_return_exercise(absHIIT_copy)
        HIIT3 = safe_return_exercise(absHIIT_copy)
        HIIT4 = safe_return_exercise(absHIIT_copy)

        self.absWO["Lower Abs 1"] = lowerAbs1
        self.absWO["Obliques (side) 1"] = sideObliques1
        self.absWO["Upper Abs 1"] = upperAbs1
        self.absWO["Lower Abs 2"] = lowerAbs2
        self.absWO["Obliques (side) 2"] = sideObliques2
        self.absWO["Upper Abs 2"] = upperAbs2
        self.absWO["HIIT"] = "-------------"
        self.absWO["HIIT1"] = HIIT1
        self.absWO["HIIT2"] = HIIT2
        self.absWO["HIIT3"] = HIIT3
        self.absWO["HIIT4"] = HIIT4

        return self.absWO


# Example usage
if __name__ == "__main__":
    workout = Abs()
    plan = workout.abs()

    print("Abs Workout Plan:", plan)


