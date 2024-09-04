import random

class Shoulders:
    def __init__(self):
        self.shoulderAnterior = {
            "Front Dumbbell Raise": "3x10 (15-20-25)",
            "Barbell Front Raise": "3x10 (30-35-40)",
            "Cable Front Raise": "3x12 (15-20-25)",
            "Plate Front Raise": "3x12 (25-35-45)"
        }

        self.shoulderLateral = {
            "Side Lateral Raise": "3x12 (15-20-25)",
            "Cable Lateral Raise": "3x12 (10-15-20)",
            "Dumbbell Lateral Raise": "3x12 (15-20-25)",
            "Lean-Away Lateral Raise": "3x12 (15-20-25)"
        }

        self.shoulderPosterior = {
            "Reverse Pec Deck Fly": "3x12 (40-45-50)",
            "Face Pulls": "3x12 (30-35-40)",
            "Bent-Over Reverse Fly": "3x12 (15-20-25)",
            "Cable Rear Delt Row": "3x12 (20-25-30)"
        }

        # Initialize the workout plan
        self.shouldersWOPlan = {}

    def returnExercise(self, muscle_group):
        random_key = random.choice(list(muscle_group.keys()))
        random_value = muscle_group[random_key]
        return f"{random_key} - {random_value}"

    def shoulderDay(self):
        anterior = self.returnExercise(self.shoulderAnterior)
        lateral = self.returnExercise(self.shoulderLateral)
        posterior = self.returnExercise(self.shoulderPosterior)

        self.shouldersWOPlan["Anterior Deltoid"] = anterior
        self.shouldersWOPlan["Lateral Deltoid"] = lateral
        self.shouldersWOPlan["Posterior Deltoid"] = posterior

        return self.shouldersWOPlan

# Example usage
if __name__ == "__main__":
    shoulder_workout = Shoulders()
    shoulder_plan = shoulder_workout.shoulderDay()
    print(shoulder_plan)
