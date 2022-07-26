from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from employer.forms import EmployerProfileForm,JobsForm
from employer.models import EmployerProfile,Jobs,Applications
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView
from django.core.mail import send_mail
from django.contrib import messages
from users.decorator import signin_required
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(signin_required,name='dispatch')
class EmployerhomeView(TemplateView):
    template_name = 'emp-home.html'

@method_decorator(signin_required,name='dispatch')
class EmployerProfileCreateView(CreateView):
    model = EmployerProfile
    form_class = EmployerProfileForm
    template_name = 'emp-profile.html'
    success_url = reverse_lazy('e-home')

    # def post(self, request, *args, **kwargs):
    #     form=EmployerProfileForm(request.POST,files=request.FILES)
    #     if form.is_valid():
    #         profile=form.save(commit=False)
    #         profile.user=request.user
    #         profile.save()
    #         print('profile created')
    #         return redirect('e-home')
    #     else:
    #         return render(request,self.template_name,{'form':form})

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)

@method_decorator(signin_required,name='dispatch')
class EmployeeProfileDetailsView(TemplateView):
    template_name = 'emp-myprofile.html'

@method_decorator(signin_required,name='dispatch')
class JobCreateView(CreateView):
    model = Jobs
    form_class = JobsForm
    template_name = "emp-postjob.html"
    success_url = reverse_lazy('e-home')


    def form_valid(self, form):
        form.instance.posted_by=self.request.user
        messages.success(self.request,'job has been successfully')
        return super().form_valid(form)


@method_decorator(signin_required,name='dispatch')
class EmployerJoblistView(ListView):
    model = Jobs
    context_object_name ='jobs'
    template_name = 'emp-joblist.html'
    # ordering = ('-created_date')

    def get_queryset(self):
        return Jobs.objects.filter(posted_by=self.request.user).order_by('-created_date')


@method_decorator(signin_required,name='dispatch')
class JobDetailView(DetailView):
    model = Jobs
    template_name = 'emp-jobdetail.html'
    context_object_name = 'job'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        qs=Applications.objects.filter(applicant=self.request.user,job=self.object)
        print(qs)
        context['status']=qs
        return context

# update job viwe addikanam
@method_decorator(signin_required,name='dispatch')
class UpdateJobView(UpdateView):
    model = JobsForm
    template_name = "edit_job.html"
    success_url = reverse_lazy("job-details")
    pk_url_kwarg = 'id'


    def get_queryset(self):
        return Jobs.objects.get(posted_by=self.request.user)

@method_decorator(signin_required,name='dispatch')
class ViewApplication(ListView):
    model = Applications
    template_name = "all_applications.html"
    context_object_name = 'all_app'

    def get_queryset(self):
        return Applications.objects.filter(job=self.kwargs.get('id'),status="applied")


@method_decorator(signin_required,name='dispatch')
class ApplicantView(DetailView):
    model = Applications
    template_name = 'applicant_details.html'
    context_object_name = 'applic'
    pk_url_kwarg = 'id'

@signin_required
def update_application(request,*args,**kwargs):
    app_id=kwargs.get('id')
    qs=Applications.objects.get(id=app_id)
    qs.status="rejected"
    qs.save()
    return redirect("e-home")


@signin_required
def accept_application(request,*args,**kwargs):
    app_id=kwargs.get('id')
    qs=Applications.objects.get(id=app_id)
    qs.status='accepted'
    qs.save()
    send_mail(
        'job notification',
        "you are accepted for...",
        ["kssreerag1999@gmail.com"],
        ['anandpashok@gmail.com'],
        fail_silently=False,
    )
    return redirect('e-home')

class EmpProfileUpdate(UpdateView):
    model = EmployerProfile
    form_class = EmployerProfileForm
    template_name = 'emp-pro-update.html'
    success_url = reverse_lazy('e-home')
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        messages.success(self.request,'profile has been updated')
        return super().form_valid(form)