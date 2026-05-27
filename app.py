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
    floor_div = adjusted_score // 10
    power = bonus_rounds ** 2
    is_high_score = adjusted_score >= 80

    print("score:", score)
    print("extra_credit:", extra_credit)
    print("total_score:", total_score)
    print("missed_points:", missed_points)
    print("average_score:", average_score)
    print("adjusted_score:", adjusted_score)
    print("remainder when divided by 7:", remainder)
    print("floor division of adjusted_score by 10:", floor_div)
    print("bonus_rounds squared:", power)
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

    if entry != "guest":
        print("User is not a guest")

    # More operators and control flow
    temperature = 58
    if temperature < 32:
        print("Weather: Freezing")
    elif temperature < 60:
        print("Weather: Chilly")
    else:
        print("Weather: Warm")

    is_warm = temperature > 75
    is_cool = temperature <= 60
    print("Is it warm?", is_warm)
    print("Is it cool?", is_cool)

    age = 16
    can_drive = age >= 16
    has_license = False

    if can_drive and has_license:
        print("Driving status: Can drive")
    elif can_drive and not has_license:
        print("Driving status: Can drive with supervision")
    else:
        print("Driving status: Not allowed")

    # Logical OR operator
    is_weekend = True
    is_holiday = False
    if is_weekend or is_holiday:
        print("Status: Time to relax!")


if __name__ == "__main__":
    main()
