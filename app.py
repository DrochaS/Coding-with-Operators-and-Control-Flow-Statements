# app.py
# Demonstrates variables, operators, and control flow in Python.

def main():
    # Declare variables and use arithmetic operators
    score = 72
    extra_credit = 5
    total_score = score + extra_credit
    missed_points = 100 - total_score
    average_score = total_score / 2
    bonus_rounds = 3
    adjusted_score = total_score + bonus_rounds * 2
    remainder = adjusted_score % 7
    is_high_score = adjusted_score >= 80

    print("score:", score)
    print("extra_credit:", extra_credit)
    print("total_score:", total_score)
    print("missed_points:", missed_points)
    print("average_score:", average_score)
    print("adjusted_score:", adjusted_score)
    print("remainder when divided by 7:", remainder)
    print("high score?:", is_high_score)

    # Control flow with if, elif, else
    if adjusted_score >= 90:
        print("Result: Excellent")
    elif adjusted_score >= 80:
        print("Result: Good")
    elif adjusted_score >= 70:
        print("Result: Pass")
    else:
        print("Result: Needs improvement")

    # Compare values using equality and inequality operators
    password = "secure123"
    entry = "secure123"

    if entry == password:
        print("Password check: Access granted")
    else:
        print("Password check: Access denied")

    # More operators and control flow
    temperature = 58
    if temperature < 32:
        print("Weather: Freezing")
    elif temperature < 60:
        print("Weather: Chilly")
    else:
        print("Weather: Warm")

    age = 16
    can_drive = age >= 16
    has_license = False

    if can_drive and has_license:
        print("Driving status: Can drive")
    elif can_drive and not has_license:
        print("Driving status: Can drive with supervision")
    else:
        print("Driving status: Not allowed")


if __name__ == "__main__":
    main()
