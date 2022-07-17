from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from Ariza.models import Ariza
from math import ceil
from .models import *
import json

@login_required(login_url='login')
def homeView(request):
    all_spent = sum(i.amount for i in  Homiy.objects.all())
    all_request = sum([i.kontrakt for i in Student.objects.all()])
    differ = all_request-all_spent
    return render(request, 'main.html', {"spent":all_spent, 'request':all_request, 'differ':differ})

@login_required(login_url='login')
def homiyView(request):
    print(request.GET)
    try:
        viewpage = int(request.GET['view_page'])
    except:
        viewpage = 10
    try:
        page = int(request.GET['page'])
    except:
        page = 1
    if not (viewpage):
        viewpage = 10
    if not (page):
        page = 1
    try:
        ariza_state = request.GET['ariza-state']
        payment = request.GET['payment']
        date = request.GET['date']
        if ariza_state == 'all':
            if payment == 'all':
                if not date:
                    all = Ariza.objects.all().order_by('id')
                else:
                    all = Ariza.objects.filter(created_at__lt=date)
            else:
                if not date:
                    all = Ariza.objects.filter(amount=int(payment)).order_by('id')
                else:
                    all = Ariza.objects.filter(created_at__lt=date, amount=int(payment))

        else:
            if payment == 'all':
                if not date:
                    all = Ariza.objects.filter(status=ariza_state).order_by('id')
                else:
                    all = Ariza.objects.filter(created_at__lt=date, status=ariza_state).order_by('id')
            else:
                if not date:
                    all = Ariza.objects.filter(amount=int(payment), status=ariza_state).order_by('id')
                else:
                    all = Ariza.objects.filter(created_at__lt=date, amount=int(payment), status=ariza_state).order_by(
                        'id')
    except:
        all = Ariza.objects.all().order_by('id')
    jami = len(all)
    pages = ceil(jami / viewpage)

    viewpages = [
        {'number': 10},
        {'number': 15},
        {'number': 20}
    ]
    if jami >= page * viewpage:
        arizas = all[(page - 1) * viewpage:viewpage]
    else:
        arizas = all[(page - 1) * viewpage:]
    data = []
    sanoq = (page - 1) * viewpage + 1
    for i in arizas:
        data.append({
            'id': i.id,
            'N': sanoq,
            'fish': i.fish,
            'phone': i.phone,
            'amount': i.amount,
            'sana': i.created_at.strftime("%d.%m.%y"),
            'status': i.status,
        })
        sanoq += 1
    arizas = data
    context = {
        'jami': jami,
        'pages': range(1, pages + 1),
        'viewpages': viewpages,
        'viewpage': viewpage,
        'arizas': arizas,
        'min': (page - 1) * viewpage + 1,
        'max': (page - 1) * viewpage + len(arizas),
        'page': page
    }
    return render(request, 'homiylar.html', context)

@login_required(login_url='login')
def singleHomiyView(request, id):
    if request.method == "POST":
        print(request.POST)
        ariza = Ariza.objects.get(id=id)
        fish = request.POST.get("fname")
        phone = request.POST.get('pnumber')
        status = request.POST.get('holat')
        amount = request.POST.get("summasi")
        paymentType = request.POST.get("turi")
        type = request.POST.get('type')
        tashkilot = request.POST.get('community')
        if fish:
            ariza.fish = fish
        if phone:
            ariza.phone = phone
        if status:
            ariza.status = status
        if amount:
            ariza.amount = int(amount)
        if paymentType in [i[0] for i in ariza.payment_type_options]:
            ariza.paymentType = paymentType
        if type in [i[0] for i in ariza.type_options]:
            ariza.type = type
        if status in [i[0] for i in ariza.status_options]:
            ariza.status = status
        if type == 'yuridik' and tashkilot:
            ariza.tashkilot = tashkilot
        ariza.save()
    try:
        ariza = Ariza.objects.get(id=id)
    except:
        return render(request, '404.html', )
    return render(request, 'homiyperson.html', {'ariza': ariza})

@login_required(login_url='login')
def studentsView(request):
    print(request.GET)
    try:
        viewpage = int(request.GET['view_page'])
    except:
        viewpage = 10
    try:
        page = int(request.GET['page'])
    except:
        page = 1
    if not (viewpage):
        viewpage = 10
    if not (page):
        page = 1
    try:
        turi = request.GET.get('filter-turi')
        otm = request.GET.get('filter-otm')
        if turi == 'all':
            if otm == 'all':
                all = Student.objects.all().order_by('id')
            else:
                all = Student.objects.filter(otm_id=int(otm))
        else:
            if otm == 'all':
                all = Student.objects.filter(t_turi=turi).order_by('id')
            else:
                all = Student.objects.filter(otm_id=int(otm), t_turi=turi)
    except:
        all = Student.objects.all().order_by('id')
    jami = len(all)
    pages = ceil(jami / viewpage)

    viewpages = [
        {'number': 10},
        {'number': 15},
        {'number': 20}
    ]
    if jami >= page * viewpage:
        students = all[(page - 1) * viewpage:viewpage]
    else:
        students = all[(page - 1) * viewpage:]
    data = []
    sanoq = (page - 1) * viewpage + 1
    for i in students:
        student = {
            'id': i.id,
            'N': sanoq,
            'fish': i.fish,
            'phone': i.phone,
            'kontakt': i.kontrakt,
            'turi': i.t_turi,
            'otm': i.otm.name,
            'homiy_amount': sum([j.amount for j in Homiy.objects.filter(student=i)])
        }
        if not student['homiy_amount']:
            student['homiy_amount'] = 0
        data.append(student)
        sanoq += 1
    students = data
    otm = University.objects.all()
    context = {
        'jami': jami,
        'pages': range(1, pages + 1),
        'viewpages': viewpages,
        'viewpage': viewpage,
        'students': students,
        'otms': otm,
        'min': (page - 1) * viewpage + 1,
        'max': (page - 1) * viewpage + len(students),
        'page': page
    }
    return render(request, 'students.html', context)

@login_required(login_url='login')
def addStudentView(request):
    if request.method == "POST":
        fish = request.POST.get('name')
        phone = request.POST.get('phone')
        otm = request.POST.get('otm')
        turi = request.POST.get('turi')
        amount = request.POST.get('amount')
        if fish and phone and otm and turi in ('bakalavr', 'magistr') and amount.isdigit():
            try:
                Student.objects.create(otm_id=int(otm), fish=fish, phone=phone, t_turi=turi,
                                       kontrakt=int(amount)).save()
                return redirect('students')
            except:
                pass
    universities = University.objects.all()
    context = {
        "universities": universities
    }
    return render(request, 'addstudent.html', context)

@login_required(login_url='login')
def singleStudentView(request, id):
    if request.method == "POST":
        homiy_id = int(request.POST.get('homiy'))
        amount = int(request.POST.get('amount'))
        Homiy.objects.create(homiy_id=homiy_id, student_id=id, amount=amount)
    try:
        student = Student.objects.get(id=id)
        data = {
            'fish': student.fish,
            'otm': student.otm.name,
            'phone': student.phone,
            't_turi': student.t_turi,
            'kontrakt': student.kontrakt,
            'homiy_amount': sum([j.amount for j in Homiy.objects.filter(student=student)])
        }
        if not data['homiy_amount']:
            data['homiy_amount'] = 0
        homiylar = Homiy.objects.filter(student=student)
        homiys = []
        sanoq = 1
        for i in homiylar:
            homiys.append({
                'N': sanoq,
                'fish': i.homiy.fish,
                'amount': i.amount,
                'id': i.id
            })
            sanoq += 1
        all_homiy = Ariza.objects.filter(status='tasdiqlangan')
        all = []
        for i in all_homiy:
            spent = sum([j.amount for j in Homiy.objects.filter(homiy=i)])
            if i.amount > spent:
                all.append({
                    'fish': i.fish,
                    'allamount': i.amount,
                    'spent': spent,
                    'balance': i.amount - spent,
                    'id': i.id
                })
        context = {'student': data, 'homiylar': homiys, 'available_homiys': all}
        if all:
            context['max'] = all[0]['balance']
        else:
            context['max'] = 0
    except:
        return render(request, '404.html')

    return render(request, 'studentperson.html', context)

@login_required(login_url='login')
def checkBalanceView(request):
    if request.method == "POST":
        data = json.loads(request.body)
        homiy_id = data['homiy_id']
        try:
            i = Ariza.objects.get(id=int(homiy_id))
            spent = sum([j.amount for j in Homiy.objects.filter(homiy=i)])
            balance = i.amount - spent
            return JsonResponse({'data': 'ok', "balance": balance})
        except:
            return JsonResponse({'data': 'false'})
    return render(request, '404.html')

@login_required(login_url='login')
def homiySearchView(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            key = data['key']
            homiys = Ariza.objects.filter(fish__icontains=key)
            data = []
            sanoq=1
            for i in homiys:
                data.append({
                    'N':sanoq,
                    'fish':i.fish,
                    'phone':i.phone,
                    'amount':i.amount,
                    'spent': sum([i.amount for i in Homiy.objects.filter(homiy=i)]),
                    'date': i.created_at.strftime('%d.%m.%y'),
                    'status':i.status,
                    'id':i.id,
                })
                sanoq+=1
            return JsonResponse({'state': 'ok', 'data':data})
        except :
            pass

    return render(request, '404.html')
@login_required(login_url='login')
def talabaSearchView(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            key = data['key']
            students = Student.objects.filter(fish__icontains=key)
            data = []
            sanoq=1
            for i in students:
                data.append({
                    'N':sanoq,
                    'fish':i.fish,
                    'turi':i.t_turi,
                    'otm':i.otm.name,
                    'homiy_amount':sum([j.amount for j in Homiy.objects.filter(student=i)]) ,
                    'kontrakt': i.kontrakt,
                    'id':i.id,
                })
                sanoq+=1
            return JsonResponse({'state': 'ok', 'data':data})
        except :
            pass

    return render(request, '404.html')