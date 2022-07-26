from django.urls import path
from employer import views


urlpatterns=[
    path("emphome",views.EmployerhomeView.as_view(),name='e-home'),
    path('profile/add',views.EmployerProfileCreateView.as_view(),name='emp-profile'),
    path('profile/detail',views.EmployeeProfileDetailsView.as_view(),name='emp-detail'),
    path('job/add',views.JobCreateView.as_view(),name='emp-addjob'),
    path('job/all',views.EmployerJoblistView.as_view(),name='emp-listjob'),
    path('job/detail/<int:id>',views.JobDetailView.as_view(),name='emp-jobdetail'),
    path('jobedit/<int:id>',views.UpdateJobView.as_view(),name='job-edit'),
    path('view_applic/<int:id>',views.ViewApplication.as_view(),name='view_applic'),
    path('view_applic_details/<int:id>',views.ApplicantView.as_view(),name='applicant_detail'),
    path('a_status/<int:id>',views.update_application,name="a-status"),
    path('status/<int:id>',views.accept_application,name='ststus'),
    path("update/<int:id>",views.EmpProfileUpdate.as_view(),name="e-update")
    # emp profile update



]