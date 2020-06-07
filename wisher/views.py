from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login ,logout
from wisher.models import birthdays
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.
def afterlogin(request):
    infoss = birthdays.objects.filter(user__exact = request.user).all()

    params = {
            'result':infoss,
    }
        
    return render(request,'index.html',params)    



def beforelogin(request):
    
    return render(request,'beforelogin.html')

def handlesignup(request):
    if request.method == 'POST':
        username = request.POST['susername']
        firstname = request.POST['sfirstname']
        lastname =request.POST['slastname']
        email =request.POST['semail']
        password =request.POST['spassword']
        password2 = request.POST['spassword2']

           
        if len(username) > 10:
            messages.error(request,"Username must be under 10 characters")
            return redirect('home')
        

        if password != password2:
            messages.error(request,"passwords do not match")
            return redirect('home')
        
        if username.isalnum():
            messages.error(request,"do no include numbers in username")
         
        myuser = User.objects.create_user(username ,email ,password)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()
        messages.success(request, 'Profile is created.')
        return redirect('beforelogin')
    else:
        return HttpResponse("Error 404")

def handlelogin(request):
    if request.method == 'POST':
        password = request.POST['lpassword']
        email = request.POST['lemail']
        username = User.objects.get(email=email.lower()).username

        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request,"succesfully logged in.")
            return redirect('afterlogin')
        
        else:
            messages.error(request, "Invalid Credentials , please try again")
            return redirect('beforelogin')
        

def handlelogout(request):
    logout(request)
    messages.success(request, "Logout Succesfully.")
    return redirect('beforelogin')


def about(request):
    return render(request,"about.html")

def addbirthday(request):
    return render(request,"addbirthday.html")

def addtodb(request):
    if request.method == 'POST':
        username = request.user
        humanname = request.POST['humanname']
        humanbirthdate = request.POST['humanbirthdate']
        humanemail = request.POST['humanemail']
        humanmsg = request.POST['humanmsg']
        birthdayready = birthdays(user = username, human=humanname ,birthdate=humanbirthdate , emailtosend=humanemail , msg = humanmsg)
        birthdayready.save()
        messages.success(request,"birthday succesfully added.")
        return redirect("afterlogin")


    else:
        return HttpResponse('404 error!')

def remove(request):
    if request.method == 'POST':
        username = request.POST['nameofuser']
        email = request.POST['emailofuser']
        removeuser = birthdays.objects.filter(human__exact = username).filter(emailtosend = email).get()
        removeuser.delete()
        messages.success(request,"removed succesfully")
        return redirect("afterlogin")

def update(request):
    if request.method == 'POST':
        username = request.POST['nameofuserup']
        email = request.POST['emailofuserup']
        updateuser = birthdays.objects.filter(human__exact = username).filter(emailtosend__exact = email).get()
        params = {
            'result':updateuser,
        }
        print(updateuser)
        return render(request,"addbirthday.html",params)

def updatenow(request):
    if request.method == 'POST':
        username = request.user
        humanname = request.POST['humanname']
        humanbirthdate = request.POST['humanbirthdate']
        humanemail = request.POST['humanemail']
        humanmsg = request.POST['humanmsg']
        updateuser = birthdays.objects.filter(user = username, human=humanname).get()
        updateuser.emailtosend = humanemail
        updateuser.birthdate = humanbirthdate
        updateuser.msg = humanmsg
        updateuser.save()        
        
        messages.success(request,"your request is full-filed.")
        return redirect("afterlogin")


def sendemail(request):
    if request.method == 'POST':
        name = request.POST['nameofusersm']
        email = request.POST['emailofusersm']
        receiver = birthdays.objects.filter(user__exact = request.user).filter(emailtosend__exact = email).filter(human__exact = name).get()
        subject = 'Happy birthday'
        html_message = render_to_string('about.html', {'context': 'values'})
        plain_message = strip_tags(html_message)
        from_email = 'From harahismast@gmail.com'
        to = email
        send_mail(subject, plain_message, from_email, [to], html_message=html_message,fail_silently = False)
        messages.success(request,"mail to ",name," has been sent succesfully!")
        receiver.delete()
        return redirect("afterlogin")