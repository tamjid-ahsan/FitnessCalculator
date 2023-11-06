# Intermittent Fasting Calculator Python
# Based on BMR

def calculate_bmr(weight, height, age, sex):
  """Calculates BMR based on Mifflin-St Jeor equation.

  Args:
    weight: Weight in kilograms.
    height: Height in centimeters.
    age: Age in years.
    sex: Gender, either "male" or "female".

  Returns:
    BMR in kilocalories per day.
  """

  if sex == "male":
    bmr = 66 + (6.3 * weight) + (12.9 * height) - (6.8 * age)
  else:
    bmr = 655 + (4.3 * weight) + (4.7 * height) - (4.7 * age)

  return bmr

def calculate_intermittent_fasting_window(bmr, activity_level):
  """Calculates intermittent fasting window based on BMR and activity level.

  Args:
    bmr: BMR in kilocalories per day.
    activity_level: Activity level, either "sedentary", "lightly active",
      "moderately active", or "very active".

  Returns:
    Intermittent fasting window in hours.
  """

  if activity_level == "sedentary":
    window = 16
  elif activity_level == "lightly active":
    window = 15
  elif activity_level == "moderately active":
    window = 14
  elif activity_level == "very active":
    window = 13
  else:
    raise ValueError("Invalid activity level.")

  # Adjust window based on BMR.
  if bmr > 2000:
    window -= 1
  elif bmr > 1500:
    window -= 0.5

  return window

def main():
  """Prompts the user for their information and calculates their intermittent fasting window."""

  weight = float(input("Enter your weight in kilograms: "))
  height = float(input("Enter your height in centimeters: "))
  age = int(input("Enter your age in years: "))
  sex = input("Enter your gender (male or female): ")
  activity_level = input("Enter your activity level (sedentary, lightly active, moderately active, or very active): ")

  bmr = calculate_bmr(weight, height, age, sex)
  window = calculate_intermittent_fasting_window(bmr, activity_level)

  print("Your BMR is {} kilocalories per day.".format(bmr))
  print("Your intermittent fasting window is {} hours.".format(window))

if __name__ == "__main__":
  main()
