from django.shortcuts import render
from decimal import Decimal as D


# Create your views here.
def calculation(request):
    if request.method == "POST":
        height = float(request.POST["height"])
        weight = float(request.POST["weight"])
        height_new = (height/100)
        old_bmi = weight/(height_new**2)
        bmi = D(old_bmi).quantize(D('0.01'))
        
        
        if 0<=bmi<18.5:
            return render(request, "index.html", {"category":"Under Weight", "result":bmi})
        elif 18.5<=bmi<=24.9:
            return render(request, "index.html", {"category":"Normal Weight", "result":bmi})
        elif 24.9<=bmi<=29.9:
            return render(request, "index.html", {"category":"Pre Obesity", "result":bmi})
        elif 29.9<=bmi<=34.9:
            return render(request, "index.html", {"category":"Obesity Class - I", "result":bmi})
        elif 34.9<=bmi<=39.9:
            return render(request, "index.html", {"category":"Obesity Class - II", "result":bmi})
        elif bmi>39.9:
            return render(request, "index.html", {"category":"Obesity Class - III", "result":bmi})
        

    return render (request, "index.html", {"result":""})