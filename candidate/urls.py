from django.urls import path
from candidate import views


urlpatterns=[
    path('candhome',views.CandidateHomeView.as_view(),name='cand-home'),
    path('profile/add',views.CandidateProfileCreateView.as_view(),name='cand-addprofile'),
    path('profile/detail',views.CandidateProfileDetail.as_view(),name='cand-detail'),
    path("joblist",views.CandidateJobListView.as_view(),name='cand-joblist'),
    path('jobs/detail/<int:id>',views.CandidateJobDetailView.as_view(),name='cand-detailsjob'),
    path('application/add/<int:id>',views.apply_now,name='apply-now'),
    path('myapplied',views.MyApplicationView.as_view(),name='my_applied'),
    path("accepted",views.AcceptedApplications.as_view(),name='accp-jobs'),
    path("update/<int:id>",views.CandidateProfileEditView.as_view(),name='c-update'),
    path("signout",views.signout,name="signout")


]