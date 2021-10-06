from django.core import paginator
from django.forms.forms import Form
from django.shortcuts import redirect, render
from  .models import Job
from django.core.paginator import Paginator
from .form import ApplyForm ,JobForm
from job import form
from django.urls import reverse

# Create your views here.
def job_list(request):
    job_list = Job.objects.all()
    paginator = Paginator(job_list,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    contxet = {'jobs' :page_obj}
    return render(request,'job/job_list.html',contxet)
    

def job_details(request,slug):
    job_details = Job.objects.get(slug=slug)
    if request.method=='POST':
        form = ApplyForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_details
            myform.save()
           
    else:
        form = ApplyForm()

    context = {'job':job_details,'form1':form}
    return render(request,'job/job_details.html',context)


def add_job(request):
    if request.method=='POST':
        form = JobForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form = JobForm()
    return render(request,'job/add_job.html',{'form':form})