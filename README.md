# Fitness calculator

## Basal Metabolic Rate

### Mifflin St. Guyer's equation

*The Mifflin-St Jeor formula, the most reliable and accurate equation, according to the systematic review published by the Journal of the Academy of Nutrition and Dietetics in 2005, this equation depends on a group of elements, namely; `Age`, `height`, and `weight`, in addition to `gender`, the mathematical formulas used to calculate the basal metabolic rate (`BMR`) for males and females, as follows:*

## Fasting window

- 250 calories per hour
- refactor not wanting to calculate fasting window logic

## Repository Structure

```bash
.
├── bmr.py          # calculator script
├── LICENSE         # MIT License
├── other_methods   # WIP other methods tried
│   ├── fasting_1.py
│   └── fasting.py
├── README.md       # this file
└── test            # simple unit testing using `pytest`
    ├── out_imperial.txt
    ├── out_metric.txt
    └── test_bmr.py # pytest script
```

## `test` contains simple unit testing

## TODO

- make GUI version
- update README.md