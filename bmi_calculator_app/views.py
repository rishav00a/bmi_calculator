from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

def get_bmi_category(bmi):
    if ( bmi <= 18.4):
       return "Underweight","Malnutrition risk"
    elif ( bmi >= 18.5 and bmi <= 24.9):
       return "Normal weight", "Low risk"
    elif ( bmi >= 25 and bmi <= 29.9):
       return "Overweight", "Enhanced risk"
    elif ( bmi >= 30 and bmi <= 34.9):
       return "Moderately obese", "Medium risk"
    elif ( bmi >= 35 and bmi <= 39.9):
       return "Severely obese", "High risk"
    elif ( bmi >=40):
       return "Very severely obese", "Very high risk"

class CalculateBMI(APIView):
    """
    example input : \n\n\n{"records_list":[{"Gender": "Male", "HeightCm": 171, "WeightKg": 50 },{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg":
85 }, { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166,
"WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female",
"HeightCm": 167, "WeightKg": 82}]}
    """
    authentication_classes =[]
    permission_classes =[]

    def post(self, request, *args, **kwargs):
        records_list = request.data["records_list"]

        for record in records_list:
            height = record["HeightCm"]
            height_m = record["HeightCm"]/100
            weight = record["WeightKg"]
            
            bmi = round(float(weight/height_m),2)
            
            record["BMI"]= bmi
            record["BMI_category"], record["health_risk"] = get_bmi_category(bmi)
            
        count_overweight = len(list(filter(lambda rec: rec['BMI_category'] == 'Overweight', records_list)))
        return Response({
            "count_overweight":count_overweight,
            "records_list":records_list,
            
        })