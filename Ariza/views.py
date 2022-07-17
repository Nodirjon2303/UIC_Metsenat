import json

from django.shortcuts import render
from .models import Ariza

def arizaView(request):
    if request.method == "POST":
        try:
        # print(request.POST)
            context = {}
            fish = request.POST.get('fname')
            number = request.POST.get('number')
            payment_amount = request.POST['payment']
            other_payment = request.POST['otherpayment']
            cname = request.POST.get("cname")
            if cname:
                type = 'yuridik'
            else:
                type = 'jismoniy'
            if other_payment:
                amount = int(other_payment)
            else:
                amount = int(payment_amount)

            Ariza.objects.create(type=type, fish=fish,phone=number, amount=amount, tashkilot=cname).save()
            # print(fish, number, payment_amount, cname, other_payment)
            return render(request, 'index.html', {"status":'ok'})
        except :
            return render(request, 'index.html', {"status": 'false' })
    return render(request, 'index.html', {'status': 'None'})
