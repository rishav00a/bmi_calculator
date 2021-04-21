# BMI Calculator

## [Demo](https://rishav-bmi-clac.herokuapp.com/)

### [Go to code](https://github.com/rishav00a/bmi_calculator/blob/main/bmi_calculator_app/views.py)

### Example input

```
{
  "records_list":[
      {"Gender": "Male", "HeightCm": 171, "WeightKg": 50 },
      {"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, 
      { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 }, 
      { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, 
      { "Gender": "Female", "HeightCm": 166, "WeightKg": 62}, 
      {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, 
      {"Gender": "Female","HeightCm": 167, "WeightKg": 82}
   ]
}
```

### Example outut

```
{
    "count_overweight": 1,
    "records_list": [
        {
            "Gender": "Male", "HeightCm": 171, "WeightKg": 50, "BMI": 29.24, "BMI_category": "Overweight", "health_risk": "Enhanced risk"
        },
        {
            "Gender": "Male", "HeightCm": 171, "WeightKg": 96, "BMI": 56.14, "BMI_category": "Very severely obese", "health_risk": "Very high risk"
        },
        {
            "Gender": "Male", "HeightCm": 161, "WeightKg": 85, "BMI": 52.8, "BMI_category": "Very severely obese", "health_risk": "Very high risk"
        },
        {
            "Gender": "Male", "HeightCm": 180, "WeightKg": 77, "BMI": 42.78, "BMI_category": "Very severely obese", "health_risk": "Very high risk"
        },
        {
            "Gender": "Female", "HeightCm": 166, "WeightKg": 62, "BMI": 37.35, "BMI_category": "Severely obese", "health_risk": "High risk"
        },
        {
            "Gender": "Female", "HeightCm": 150, "WeightKg": 70, "BMI": 46.67, "BMI_category": "Very severely obese", "health_risk": "Very high risk"
        },
        {
            "Gender": "Female", "HeightCm": 167, "WeightKg": 82, "BMI": 49.1, "BMI_category": "Very severely obese", "health_risk": "Very high risk"
        }
    ]
}

```



### Test the API using CURL

```
curl --location --request POST 'https://rishav-bmi-clac.herokuapp.com/' \
--header 'Content-Type: application/json' \
--data-raw '{"records_list":[{"Gender": "Male", "HeightCm": 171, "WeightKg": 50 },{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg":
85 }, { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166,
"WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female",
"HeightCm": 167, "WeightKg": 82}]}'


```
