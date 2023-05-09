from django.urls import path
from .views import about,home,jobsListView,jobsDetailView,jobSeekerCreateView,jobProviderCreateView,handle_login,search,profile,jobCreateView

urlpatterns = [
    path('', jobsListView.as_view(), name="jobs-home"),
    path('jobInfo/<int:pk>/', jobsDetailView.as_view(), name="job-detail"),
    path('jobApplicant/create/', jobSeekerCreateView.as_view(), name="create-applicant"),
    path('jobProvider/create/', jobProviderCreateView.as_view(), name="create-provider"),
    path('job/create/', jobCreateView.as_view(), name="create-job"),
    path('chooseAccountType/',handle_login,name='handle-login'),
    path('about/', about, name="jobs-about"),
    path('search/', search, name='query'),
    path('profile/', profile, name='user-profile'),
]
