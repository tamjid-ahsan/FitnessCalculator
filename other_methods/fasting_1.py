import datetime

def calculate_bmr(weight, height, age, sex):
  """Calculates the basal metabolic rate (BMR) in calories per day.

  Args:
    weight: Weight in kilograms.
    height: Height in centimeters.
    age: Age in years.
    sex: Sex, either "male" or "female".

  Returns:
    The BMR in calories per day.
  """

  if sex == "male":
    bmr = 66 + (6.3 * weight) + (12.9 * height) - (6.8 * age)
  else:
    bmr = 655 + (4.3 * weight) + (4.7 * height) - (4.7 * age)

  return bmr

def calculate_intermittent_fasting_window(bmr, activity_level, fasting_hours):
  """Calculates the intermittent fasting window in hours.

  Args:
    bmr: Basal metabolic rate in calories per day.
    activity_level: Activity level, either "sedentary", "lightly active", "moderately active", or "very active".
    fasting_hours: The desired number of fasting hours.

  Returns:
    The intermittent fasting window in hours.
  """

  # Calculate the total daily calorie needs.
  total_calories = bmr * activity_level

  # Calculate the number of calories to be consumed during the eating window.
  eating_window_calories = total_calories - (fasting_hours * 100)

  # Calculate the length of the eating window in hours.
  eating_window_hours = eating_window_calories / 100

  return eating_window_hours

def main():
  """Calculates the intermittent fasting window based on the user's BMR, activity level, and desired fasting hours."""

  # Get the user's weight, height, age, and sex.
  weight = float(input("Enter your weight in kilograms: "))
  height = float(input("Enter your height in centimeters: "))
  age = int(input("Enter your age in years: "))
  sex = input("Enter your sex (male or female): ")

  # Calculate the user's BMR.
  bmr = calculate_bmr(weight, height, age, sex)

  # Get the user's activity level.
  activity_level = input("Enter your activity level (sedentary, lightly active, moderately active, or very active): ")

  # Get the user's desired fasting hours.
  fasting_hours = int(input("Enter your desired fasting hours: "))

  # Calculate the intermittent fasting window.
  intermittent_fasting_window = calculate_intermittent_fasting_window(bmr, activity_level, fasting_hours)

  # Print the intermittent fasting window.
  print("Your intermittent fasting window is {} hours.".format(intermittent_fasting_window))

if __name__ == "__main__":
  main()
