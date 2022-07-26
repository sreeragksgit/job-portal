from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView
from candidate.models import Candidateprofile
from candidate.forms import CandidateProfileForm
from django.urls import reverse_lazy
from employer.models import Jobs,Applications
from candidate.filters import JobFilter
# logout
from django.contrib.auth import logout
from users.decorator import signin_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(signin_required,name='dispatch')
class CandidateHomeView(TemplateView):
    template_name = 'cand-home.html'

    def get(self, request, *args, **kwargs):
        filter=JobFilter(request.GET,queryset=Jobs.objects.all())
        return render(request,"cand-home.html",{'filter':filter})

@method_decorator(signin_required,name='dispatch')
class CandidateProfileCreateView(CreateView):
    model = Candidateprofile
    form_class = CandidateProfileForm
    template_name = "cand-profile.html"
    success_url = reverse_lazy('cand-home')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

@method_decorator(signin_required,name='dispatch')
class CandidateProfileDetail(TemplateView):
    template_name = 'cand-myprofiledetail.html'

@method_decorator(signin_required,name='dispatch')
class CandidateJobListView(ListView):
       model = Jobs
       template_name = "cand-listjob.html"
       context_object_name = 'jobs'
       page_kwarg = 'id'
       ordering = ['id']
       paginate_by = 2

@signin_required
def apply_now(request, *args, **kwargs):
    job_id = kwargs.get('id')
    job = Jobs.objects.get(id=job_id)
    applicant = request.user
    Applications.objects.create(applicant=applicant, job=job)
    return redirect('cand-home')


@method_decorator(signin_required,name='dispatch')
class CandidateJobDetailView(DetailView):
    model = Jobs
    template_name = 'cand-detailjob.html'
    context_object_name = 'job'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        qs=Applications.objects.filter(applicant=self.request.user,job=self.object)
        print(qs)
        context['status']=qs
        return context


@method_decorator(signin_required,name='dispatch')
class MyApplicationView(ListView):  #list the applied job view
    model = Applications
    template_name = 'applied_joblist.html'
    context_object_name = 'applied'

    def get_queryset(self):
        return Applications.objects.filter(applicant=self.request.user)


@method_decorator(signin_required,name='dispatch')
class AcceptedApplications(ListView):
    model = Applications
    template_name = 'Accepted.html'
    context_object_name = 'application'


    def get_queryset(self):
        return Applications.objects.filter(applicant=self.request.user,status='accepted')


@signin_required
def signout(request):
    logout(request)
    return redirect('sign-in')





    # candidateprofile edit

@method_decorator(signin_required,name='dispatch')
class CandidateProfileEditView(UpdateView):
    model = Candidateprofile
    form_class = CandidateProfileForm
    template_name = 'cant-pro-update.html'
    success_url = reverse_lazy('cand-detail')
    pk_url_kwarg = 'id'
