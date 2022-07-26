from django.shortcuts import render,redirect
from django.views.generic import CreateView,FormView
from users.models import User
from users.forms import UserRegistrationForm,LoginForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login

# Create your views here.

class SingupView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('sign-in')


class SinginView(FormView):
     model= User
     form_class = LoginForm
     template_name = 'login.html'


     def post(self, request, *args, **kwargs):
         form=LoginForm(request.POST)
         if form.is_valid():
             username=form.cleaned_data.get('username')
             password=form.cleaned_data.get('password')
             user=authenticate(request,username=username,password=password)
             if not user:
                 print('login fail')
                 return render(request,'login.html',{'form':form})
             login(request,user)
             if request.user.is_candidate:
                 return redirect('cand-home')
             else:
                 return redirect('e-home')
                 #render(request,'emplyer_home.html')

