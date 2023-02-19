from django.shortcuts import render
from django.http import HttpResponse
from joblib import load


model = load('./model/pipeline.joblib')

Gho_Code={
    "WHOSIS_000015":2,
    "WHOSIS_000001":0,
    "WHOSIS_000002":1
}

Region_Code={
    "EUR":3,
    "AFR":0,
    "AMR":1,
    "WPR":5,
    "EMR":2,
    "SEAR":4
}

Group_Code={
    "WB_LMI":2,
    "WB_HI":0,
    "WB_UMI":3,
    "WB_LI":1
}

Group_Display={
    "Lower_middle_income":2,
    "High_income":0,
    "Upper_middle_income":3,
    "Low_income": 1,
    "Balanced_income":4
}

Sex_Display={
    "Female":1,
    "Male":2,
    "Both_genders":0
}

def prediction(request):
    if request.method == 'POST':
        beer_servings = request.POST['beer_servings']
        spirit_servings=request.POST['spirit_servings']
        wine_servings = request.POST['wine_servings']
        total_litres_of_pure_alcohol = request.POST['total_litres_of_pure_alcohol']
        GhoCode = Gho_Code.get(request.POST['GhoCode'])
        YearDisplay = request.POST['YearDisplay']
        RegionCode =Region_Code.get(request.POST['RegionCode'])
        WorldBankIncomeGroupGroupCode = Group_Code.get(request.POST['WorldBankIncomeGroupGroupCode'])
        WorldBankIncomeGroupDisplay = Group_Display.get(request.POST['WorldBankIncomeGroupDisplay'])
        SexDisplay =Sex_Display.get(request.POST['SexDisplay'])

        predict = model.predict([[beer_servings, spirit_servings, wine_servings, total_litres_of_pure_alcohol,
                               YearDisplay,GhoCode,RegionCode,WorldBankIncomeGroupGroupCode,
                               WorldBankIncomeGroupDisplay,SexDisplay]])

        return render(request, 'index.html', {'result': predict})
    return render(request, 'index.html')

