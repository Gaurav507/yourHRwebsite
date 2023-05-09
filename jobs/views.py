from django.shortcuts import render, HttpResponse, redirect
from . import models
from django.views.generic import ListView,DetailView,CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

# Create your views here.

jobs = [
    {
        'role' : 'Front-end Developer',
        'Company' : 'Kudosware',
        'CTC' : '$50,000',
        'Location' : 'Delhi',
        'Experience' : '2-4 yrs'
    },
    {
        'role' : 'Back-end Developer',
        'Company' : 'Kudosware',
        'CTC' : '$100,000',
        'Location' : 'Delhi',
        'Experience' : '2-4 yrs'
    },
    {
        'role' : 'Full Stack Developer',
        'Company' : 'Kudosware',
        'CTC' : '$150,000',
        'Location' : 'Delhi',
        'Experience' : '2-4 yrs'
    },
]
def home(request):
    jobs = models.jobDesc.objects.all()
    context = {
        'jobs' : jobs,
    }
    return render(request, "jobs/home.html",context)

def about(request):
    return render(request, "jobs/about.html",{'title' : 'Jobs-About'})

class jobSeekerListView(ListView):
    model = models.jobSeeker  #class basedviews >>>>> functions to create view

class jobsListView(ListView):
    model = models.jobDesc

class jobsDetailView(DetailView):
    model = models.jobDesc

class jobSeekerCreateView(LoginRequiredMixin, CreateView):  #createView classBased views expect templates with naming convention modelName_form.html & createView and updateview > > modelName_create.html
    model = models.jobSeeker
    fields = ['fullName','mobileNum','bio','resume','website']
    success_url = reverse_lazy('jobs-home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(jobSeekerCreateView,self).form_valid(form)

class jobProviderCreateView(LoginRequiredMixin, CreateView):
    model = models.jobProvider
    fields = ['fullName','company','mobileNum','jobDesc']
    success_url = reverse_lazy('jobs-home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(jobProviderCreateView,self).form_valid(form)
    
class jobCreateView(LoginRequiredMixin, CreateView):  #createView classBased views expect templates with naming convention modelName_form.html & createView and updateview > > modelName_create.html
    model = models.jobDesc
    fields = ['role','companyName','aboutCompany','email','location','salary','experience','qualifications','responsibilities']
    success_url = reverse_lazy('jobs-home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(jobCreateView,self).form_valid(form)

    
@login_required
def handle_login(request):
    # frst we want to check if the user has an account -> takw them home
    #if they don't have an account then we want to render a template where they can select which type of account they want to create 
    if request.user.get_jobSeeker() or request.user.get_jobProvider():
        return redirect(reverse_lazy('jobs-home'))
    
    return render(request, 'jobs/choose_account.html',{})

def search(request):
    query = request.GET['query']
    jobs = models.jobDesc.objects.all()
    filteredjobs = models.jobDesc.objects.filter(role__icontains = query)
    context = {'jobs' : jobs, 'filteredjobs': filteredjobs}
    return render(request, 'jobs/search.html',context)

@login_required
def profile(request):
    test = request.user
    jobSeeker = models.jobSeeker.objects.filter(owner = test).all()
    jobProvider = models.jobProvider.objects.filter(owner = test).all()
    user = test.id
    context = {'user':user,'test':test,'jobSeeker' : jobSeeker,'jobProvider':jobProvider}

    return render(request, 'jobs/profile.html',context)


