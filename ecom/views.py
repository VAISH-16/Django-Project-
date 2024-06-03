from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm,ContactForm
from django.contrib.auth import login,logout,authenticate
from cart.models import Contact
# Create your views here.
def home(request):
    return render(request,"index.html")

# Register page
# -----------------------------------------------------------------------
def register(request):
    msg=None
    if request.method=='GET':
        form=CustomUserCreationForm()
    # form=UserCreationForm()
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            msg="Registeration successsfulll"
        else:
            msg="Failed"
    return render(request,'register.html',{'form':form,'msg':msg})

# user login
# =======================================
def user_login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user is None:
            message = "Login Failed!!"
            return render(request,"login.html",{"message":message})
        if user is not None:
            login(request,user)
            return HttpResponseRedirect("/courses/")
        
# user logout
# =======================================
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/login/")

# -------------------------------
# Contact Us
# ==================================

def contact(request):
    msg = None
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            email_id = form.cleaned_data.get('email_id')
            message = form.cleaned_data.get('message')
            comment = form.cleaned_data.get('comment')
            contact_entry = Contact(
                first_name=first_name,
                email=email_id,
                message=message,
                comment=comment
            )
            contact_entry.save()
            msg = "We'll get back to you soon!"
        else:
            msg = "Failed"
    else:
        form = ContactForm()  # Initialize an empty form for GET requests

    return render(request, 'contact.html', {'form': form, 'msg': msg})