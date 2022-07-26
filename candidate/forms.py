from django import forms
from candidate.models import Candidateprofile


class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model=Candidateprofile
        exclude=('user',)


