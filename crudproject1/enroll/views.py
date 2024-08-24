from django.shortcuts import render , HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
import openpyxl
from django.db.models import Count


# Create your views here.

#this function will add new items and show all items
from django.shortcuts import render, redirect
from .forms import StudentRegistration
from .models import User
from collections import Counter

def add_show(request):
    if request.method == 'POST':
        nm = request.POST['name']
        em = request.POST['email']
        mw = request.POST['mobile']
        sw = request.POST['sex']
        dw = request.FILES['document']  # Use request.FILES for file uploads

        # Create the User instance with the correct field name
        reg = User(name=nm, email=em, mobile=mw,sex=sw, document=dw)
        reg.save()
        return redirect('/user')  # Redirect to the desired page after saving
    else:
        form = StudentRegistration()
        query = request.GET.get('q')  # Get the search term from the query parameters
        gender_filter = request.GET.get('gender')  # Get the gender filter from the query parameters
        
        # Filter users based on the search term and gender
        filters = {}
        if query:
            filters['name__icontains'] = query
        if gender_filter and gender_filter in ['Male', 'Female']:
            filters['sex'] = gender_filter
        
        stud = User.objects.filter(**filters)

        # Prepare gender distribution data for the pie chart
        gender_counts = User.objects.values_list('sex', flat=True)
        gender_distribution = dict(Counter(gender_counts))

    return render(request, 'enroll/addandshow.html', {
        'form': form,
        'stu': stud,
        'gender_distribution': gender_distribution
    })

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

def add_students_from_excel(request):
    if request.method == 'POST':
        excel_file = request.FILES['excel_file']

        # Load the workbook and select the active sheet
        wb = openpyxl.load_workbook(excel_file)
        worksheet = wb.active

        # Iterate through the rows and create User instances
        for row in worksheet.iter_rows(min_row=2):  # Assuming the first row is the header
            name = row[0].value
            email = row[1].value
            mobile = row[2].value
            document = row[3].value  # If your Excel sheet includes the document paths

            # Save each student to the database
            User.objects.create(name=name, email=email, mobile=mobile, document=document)

        return redirect('/user')
    return render(request, 'enroll/add_students_from_excel.html')
def gender_distribution(request):
    # Calculate gender distribution
    gender_counts = User.objects.values('sex').annotate(count=Count('sex'))
    gender_distribution = {item['sex']: item['count'] for item in gender_counts}
    
    return render(request, 'enroll/gender_distribution.html', {'gender_distribution': gender_distribution})
