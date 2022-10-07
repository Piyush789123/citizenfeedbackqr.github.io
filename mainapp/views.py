from pstats import Stats
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .utils import generate_graph, generate_qrcode, send_otp,feedback_type, generate_piechart
from mainapp.forms import MyLoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



from .models import Feedback, VerificationCodes

# Create your views here.

def home(request):
    if request.method == "POST":
        phone = request.POST['phone']
        request.session['phone'] = phone
        send_otp(phone)
        return HttpResponseRedirect("/otp")

    return render(request,'home.html')
    
def otp_verify(request):
    if not request.session.get("phone"):
        return HttpResponseRedirect("/")

    if request.method == 'POST':
        otp = request.POST['otp']
        phone = request.session['phone']
        print("➡ email :", phone)
        verification_code = VerificationCodes.objects.filter(phone=phone,otp = otp).last()
        print("➡ verification_code :", verification_code)

        if verification_code:
            verification_code.delete()
            messages.info(request, "You are successfully logged in.")
            request.session["otp_verified"] = True
            del request.session['phone']
            return HttpResponseRedirect("/feedback")
    return render(request, 'otp.html')

def adm(request):
    form=MyLoginForm()
    if request.method=="POST":
      form=MyLoginForm(request.POST)
      if form.is_valid():
        username = request.POST['username']
        passwd = request.POST['pass']
        user = authenticate(request,username=username,password = passwd)
        if user is not None:
            login(request,user)
            messages.success(request, "Success")
            return HttpResponseRedirect("/stats")

      else:
        print(form.errors)
        print("fail")
        messages.error(request, " Invalid Captcha")
    return render(request,"admin_login.html",{"form":form})

@login_required
def mainadm(request):
    display_qr=False
    feedbacks = Feedback.objects.all()
    total_feedbacks = feedbacks.count()
    if request.method == 'POST':

        
        print("➡ total_feedbacks :", total_feedbacks)
        city = request.POST['site']
        print("➡ city :", city)
        generate_qrcode(city)
        display_qr=False
        if city:
            display_qr = True
        context = {"city":city,'show_qr':display_qr, 'total_feedbacks':total_feedbacks}
    else:
        context = {'show_qr':display_qr,'total_feedbacks':total_feedbacks}    

    return render(request,'admin.html',context)
    

def feedback(request):

    data = request.GET
    city = data.get("city")
    if city:
        request.session["city"] = city 


    if not request.session.get("otp_verified"):
        return HttpResponseRedirect("/")

    if request.method == 'POST':
        how_do_you_come = request.POST.get('site',None)
        waiting_time = request.POST.get('waiting_time',None)
        overall = request.POST.get('rating1',None)
        servicing = request.POST.get('rating2',None)
        behaviour = request.POST.get('rating3',None)
        feedback = request.POST.get('description',None)
        police_name = request.POST.get('police_name',None)
        type_feedback = feedback_type(overall,servicing,behaviour)
        rec = Feedback(reason_to_come = how_do_you_come,waiting_time= waiting_time, overall=overall, behaviour=behaviour, servicing = servicing, type_feedback=type_feedback, city=request.session["city"],police_name=police_name, feedback=feedback)
        rec.save()
        
        
        del request.session["otp_verified"]
        messages.success(request,"Form Successfully submitted!!")

    return render(request,'feedback.html')

# def feedbacks(request):
#     data = Feedback.objects.all().filter(type_feedback = 'positive')
#     print(data)
#     return HttpResponse(data)

def bar_graph(request):

    feedbacks = Feedback.objects.all()
    
    total_feedbacks = []
    cities = []
    if request.method == 'POST':
        cities = request.POST.getlist('site')
        pie_city = request.POST['city']
        for city in cities:
            total_feeds = feedbacks.filter(city=city)
            total_feedbacks.append(total_feeds.count())

        negative = feedbacks.filter(city__icontains=pie_city.lower(), type_feedback="negative")

        positive = feedbacks.filter(city__icontains=pie_city.lower(), type_feedback="positive")

        generate_graph(cities=cities,total_feedbacks=total_feedbacks)
        generate_piechart(pie_city,positive.count(),negative.count())

    return render(request, "graph.html")
