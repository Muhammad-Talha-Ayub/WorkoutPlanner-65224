def calculate_bmi(weight, height_cm):
    if weight <= 0 or height_cm <= 0:
        raise ValueError("Weight and height must be positive numbers.")
    height_m = height_cm / 100
    return round(weight / (height_m ** 2), 2)

def workout_plan(bmi):
    if bmi < 18.5:
        return (
            "Underweight",
            "Workout 20 min/day",
            "High-calorie diet",
            "Home",
            ["Whole milk", "Nuts and nut butter", "Rice and potatoes", "Eggs", "Lean meats"]
        )
    elif 18.5 <= bmi < 24.9:
        return (
            "Normal",
            "Workout 30 min/day",
            "Balanced diet",
            "Home",
            ["Fruits", "Vegetables", "Whole grains", "Lean protein", "Dairy"]
        )
    elif 25 <= bmi < 29.9:
        return (
            "Overweight",
            "Workout 45 min/day",
            "Low-carb diet",
            "Gym",
            ["Leafy greens", "Chicken breast", "Cauliflower rice", "Boiled eggs", "Avocados"]
        )
    else:
        return (
            "Obese",
            "Workout 60 min/day",
            "Strict low-fat diet",
            "Gym",
            ["Steamed vegetables", "Grilled fish", "Oatmeal", "Low-fat yogurt", "Berries"]
        )

if __name__ == "__main__":
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in cm: "))

        bmi = calculate_bmi(weight, height)
        category, workout, diet, location, foods = workout_plan(bmi)

        print(f"\nYour BMI is: {bmi} ({category})")
        print(f"Workout Recommendation: {workout}")
        print(f"Diet Plan: {diet}")
        print(f"Workout Location: {location}")
        print("Suggested Foods:")
        for food in foods:
            print(f"- {food}")

    except ValueError as e:
        print("Invalid input:", e)
