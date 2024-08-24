from django.shortcuts import render , HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here.

#this function will add new items and show all items
def add_show(request):
    if request.method=='POST':
        fm= StudentRegistration(request.POST,request.FILES)
        print(fm)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            mw=fm.cleaned_data['mobile']
            dw=fm.cleaned_data['document']
            reg=User(name=nm,email=em,mobile=mw,file=dw)
            reg.save()
            fm=StudentRegistration()
    else:
        fm= StudentRegistration()
    stud=User.objects.all()
    return render(request, 'enroll/addandshow.html',{'form':fm,'stu':stud})
#this function will update and edit
def update_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,request.FILES,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
    return render(request,'enroll/updatestudent.html', {'form':fm})

#this function will delete

def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    
from django.shortcuts import render, redirect
from .forms import AnotherForm

def another_view(request):
    if request.method == 'POST':
        form = AnotherForm(request.POST)
        if form.is_valid():
            # Process form data
            form.cleaned_data['email'], form.cleaned_data['password']
            return redirect('/user')  # Replace with your success URL
    else:
        form = AnotherForm()
        stud=User.objects.all()
    return render(request, 'enroll/another_templates.html', {'form': form, 'stu' : stud})
