from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from volunteers import userManagement
from volunteers.models import *
from volunteers.userManagement import *

@login_required
def volunteerHome(request):
    try:
        user = request.user #authenticate(username='admin', password='adMIN')
        query_results = Userlog.objects.filter(user=user)
    except:
        print "Not logged in"
        query_results = []
    context = {'query_results': query_results}
    return render(request,'volunteers/volunteerHome.html',context)

@login_required
def volunteerSubmit(request):
    try:
        user = request.user #authenticate(username='admin', password='adMIN')
    except:
        print "ERROR UGHHH"
    date = request.POST['date']
    task = request.POST['task']
    hours = request.POST['hours']
    rate = request.POST['rate']
    print request.POST.getlist('myInputs')
    earned = request.POST.getlist('myInputs')
    totalearned = 0
    for input in earned:
        totalearned += int(input)
        print totalearned
    userlog = Userlog(user=user,date=date,task=task,hours=hours,rate=rate,voucherearned=totalearned) #request.user
    try: 
        userlog.save()
    except:
        print "ERROR"
    # return render(RequestContext(request),'volunteerHome.html')
    query_results = Userlog.objects.filter(user=user)
    context = {'query_results': query_results}
    return render(request,'volunteers/volunteerHome.html',context)

def userLogin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.process(request):
            redirect = request.GET["next"] if "next" in request.GET else reverse("volunteerHome")
            return HttpResponseRedirect(redirect)
        else:
            return render(request, "volunteers/login.html", {"form": form})
    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse("volunteerHome"))
        else:
            return render(request, "volunteers/login.html", {"form": LoginForm()})

def userRegistration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.process(request):
            return HttpResponseRedirect(reverse('userLogin'))
        else:
            return render(request, "volunteers/register.html", {"form": form})
    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse("volunteerHome"))
        else:
            return render(request, "volunteers/register.html", {"form": RegistrationForm()})

@login_required
def editProfile(request):
    if request.method == "POST":
        infoForm = EditProfileForm(request.POST)
        infoForm.process(request)
        pwForm = PasswordChangeForm(request.POST)
        if pwForm.isFilled(request):
            pwForm.process(request)
    else:
        infoForm = EditProfileForm(createUserContext(request.user))
        pwForm = PasswordChangeForm()
    return render(request, "volunteers/profile.html", {"infoForm": infoForm, "pwForm": pwForm})

def verify(request, code):
    verificationRequests = VerificationRequest.objects.filter(code=code)
    if verificationRequests:
        message = verificationRequests[0].verify()
        return HttpResponse(message)
    else:
        return HttpResponse("Invalid code.")

@login_required
def deleteAccount(request):
    userManagement.deleteAccount(request)
    return HttpResponseRedirect(reverse("editProfile"))