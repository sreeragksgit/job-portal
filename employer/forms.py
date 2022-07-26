from django import forms
from employer.models import EmployerProfile,Jobs

class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model=EmployerProfile
        exclude=('user',)



    #     fields=[
    #         'company',
    #         'logo',
    #         'bio',
    #         'location'
    #     ]

class JobsForm(forms.ModelForm):
    class Meta:
        model=Jobs
        exclude=('posted_by','created_date',)
        widgets={
            'last_date':forms.DateInput(attrs={'class':'form-control','type':'date'})
        }