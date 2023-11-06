import warnings
import math


def main(debug=False):
    welcome()
    gender = get_sex()
    age = get_age()
    measurement_type = get_measurement_type()
    if measurement_type.lower() == "metric":
        weight = get_weight()
        height = get_height()
    if measurement_type.lower() == "imperial":
        weight = get_weight_imperial()
        height = get_height_imperial()
    if debug:
        print(
            f'gender: {gender}, weight: {weight}, height: {height}, age: {age}')
    # rest_bmr = calculate_bmr(gender, weight, height, age)
    rest_bmr = calculate_bmr(weight, height, age, gender)
    output, activity_level = total_calculation(rest_bmr)
    print(f"{'-'*80}")
    print(output)
    print(f"{'-'*80}")
    calculate_fasting_window: str = str(
        input("Do you want to calculate intermittent fasting window? \n\t> "))
    if calculate_fasting_window in [True, "Yes", 1]:
        fasting_window = calculate_intermittent_fasting_window(rest_bmr)
        print(
            f"\nFasting window is {math.ceil(fasting_window.get(activity_level))} hour, rounded up.")
    else:
        print("Thanks")


def welcome():
    print(
        f"Welcome to your calories calculator powered by python!\nFind out How many calories should you consume daily.\n{'-'*50}")


def get_sex():
    sexes = ["male", "female", "M", "F", "f", "m", "Male", "Female"]
    while True:
        sex = str(input("Do you identify as male or female? \n\t> "))
        while sex not in sexes:
            sex = str(input("Please enter either 'male' or 'female' \n\t> "))
        else:
            return sex
            break


def get_age():
    age_yrs = int(input("Enter your age in years: "))
    while age_yrs <= 0:
        age_yrs = int(input("Invalid Input. Please enter your age in years: "))
    else:
        return age_yrs


def get_measurement_type():
    measurement_types: list[str] = ["Imperial", "Metric", "imperial", "metric"]
    while True:
        measurement_type: str = str(
            input("Use 'Imperial' or 'Metric' units? \n\t> "))
        while measurement_type not in measurement_types:
            measurement_type: str = str(
                input("Please enter either 'Imperial' or 'Metric' \n\t> "))
        else:
            return measurement_type
        break


def get_weight():
    weight_kg = float(input("Enter your weight in kilograms: "))
    while weight_kg <= 0:
        weight_kg = float(
            input("Invalid input. Please enter your weight in kilograms: "))
    else:
        return weight_kg


def get_height():
    height_cm = float(input("Enter your height in Centimeters: "))
    while height_cm <= 0:
        height_cm = float(
            input("Invalid input. Please enter your height in Centimeters: "))
    else:
        return height_cm


def get_weight_imperial():
    weight_lbs = float(input("Enter your weight in Pounds (lbs): "))
    while weight_lbs <= 0:
        weight_lbs = float(
            input("Invalid input. Please enter your weight in Pounds (lbs): "))
    else:
        return weight_lbs * 0.453592  # conversion to kg for calculation


def get_height_imperial():
    print("Input your height in Feet and Inches")
    height_ft = int(input("\tEnter your height in Feet:\t"))
    height_in = int(input("\tEnter your height in Inches:\t"))
    while height_ft <= 0 and height_in <= 0:
        height_ft = int(input("\tEnter your height in Feet:\t"))
        height_in = int(input("\tEnter your height in Inches:\t"))
    else:
        height_in += height_ft * 12
        height_cm = round(height_in * 2.54, 1)
        return height_cm


# def calculate_bmr(gender, weight, height, age):
#     # male = ["male", "M" , "m", "Male"]
#     female = ["female", "F", "f", "Female"]
#     if gender == female:
#         women = (weight * 10) + (height * 6.25) - (age * 5) - 161
#         return int(women)
#     else:
#         men = (weight * 10) + (height * 6.25) - (age * 5) + 5
#         return int(men)
    
def calculate_bmr(weight, height, age, sex):
    if sex == "male":
        bmr = 66 + (6.3 * weight) + (12.9 * height) - (6.8 * age)
    else:
        bmr = 655 + (4.3 * weight) + (4.7 * height) - (4.7 * age)
    return bmr


def get_user_activity():
    activity_lvl = ["sedentary", "light", "moderate", "active"]
    while True:
        user_lvl = str(input(f"\nWhat is your activity level?\n\n\tSedentary is little to no exercise.\n\tLightly active is light exercise/sports 1 - 3 days/week.\n\tModerately active is moderate exercise/sports 3 - 5 days/week.\n\tVery active is hard exercise every day, or 2 xs/day 6 - 7 days/week.\n\nPlease enter: 'sedentary', 'light', 'moderate',  or 'active': \n\t> "))

        while user_lvl.lower() not in activity_lvl:
            user_lvl = str(input(
                "Invalid input. Please enter: 'sedentary', 'light', 'moderate',  or 'active': \n\t> "))
        else:
            return user_lvl.lower()
            break


def get_sedentary(rest_bmr):
    sedentary = rest_bmr * 1.25
    return sedentary


def get_light_activity(rest_bmr):
    light = rest_bmr * 1.375
    return light


def get_moderate_activity(rest_bmr):
    moderate = rest_bmr * 1.550
    return moderate


def get_very_active(rest_bmr):
    active = rest_bmr * 1.725
    return active


def total_calculation(rest_bmr):
    user_activity_lvl = get_user_activity()

    maintain = {
        "sedentary": get_sedentary(rest_bmr),
        "light": get_light_activity(rest_bmr),
        "moderate": get_moderate_activity(rest_bmr),
        "active": get_very_active(rest_bmr)
    }

    if user_activity_lvl == "sedentary":
        return ("You need to consume " + str(round(maintain["sedentary"])) + " calories a day to maintain your current weight.", user_activity_lvl)

    if user_activity_lvl == "light":
        return ("You need to consume " + str(round(maintain["light"])) + " calories a day to maintain your current weight.", user_activity_lvl)

    if user_activity_lvl == "moderate":
        return ("You need to consume " + str(round(maintain["moderate"])) + " calories a day to maintain your current weight.", user_activity_lvl)

    if user_activity_lvl == "active":
        return ("You need to consume " + str(round(maintain["active"])) + " calories a day to maintain your current weight.", user_activity_lvl)


def calculate_intermittent_fasting_window(bmr):
    """Calculates intermittent fasting window based on BMR and activity level.

    Args:
      bmr: BMR in kilocalories per day.

    Returns:
      Intermittent fasting window in hours.
    """
    maintain = {
        "sedentary": get_sedentary(bmr),
        "light": get_light_activity(bmr),
        "moderate": get_moderate_activity(bmr),
        "active": get_very_active(bmr)
    }
    fasting_goal_dict: dict = {"sedentary": 0, "light": .1,
                               "brisk": .2, "moderate": .3, "fast": .4, "rapid": .5}
    print("\tINFO: ", ", ".join([f'{label.title()}: {value}' for label,
          value in fasting_goal_dict.items()]))
    fasting_goal = float(
        input("\tEnter your intermittent fasting goal (0.0 to 0.5): \n\t> "))
    if fasting_goal == 0:
        fasting_goal = 0.000000000000000000000000000000000001
    elif fasting_goal > .5:
        warnings.warn(
            f"The value {fasting_goal} is out of range. The valid range is 0.0 to 0.5.")
    window: dict = {key: (value*fasting_goal)/50 for key,
                    value in maintain.items()}
    return window


if __name__ == '__main__':
    main()
