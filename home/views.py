from django.shortcuts import render , HttpResponse ,redirect
from django.contrib import messages
from home.models import Employees
import logging

logging.basicConfig(filename='logs/app_logs.log', level=logging.DEBUG)

# Create your views here.
# def index(request):

    # emp=Employees.objects.all()
    # context={
    #     'emp':emp,
    # }
    # return render(request,'index.html',context)
   # return HttpResponse("this is homepage")


def index(request):

    logger.info("Accessing the index view")

    emp = Employees.objects.all()
    context = {'emp': emp}
    return render(request, 'index.html', context)
      
   

def about(request):
    return HttpResponse("this is aboutpage")

def add(request):
    if request.method == "POST":
        logger.debug(f"Adding new employee: {request.POST}")
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        
        existing_user=Employees.objects.filter(email=email).exists()

        if not existing_user:
          emp=Employees(
            name = name,
            email = email,
            address = address,
            phone = phone
          )
          emp.save()
          logger.info(f"Employee {name} added successfully")
          return redirect('home')

        else:
            messages.error(request,'user with this email already exists. please try to sign in')
            return redirect('error')


def edit(request):
    emp=Employees.objects.all()
    context = {
        'emp':emp,
    }
    return redirect(request,'index.html',context) 


def update(request,id):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        phone=request.POST.get('phone')

        emp=Employees(
            #if we dont use id than new record get updated so need to use id here
            id = id,
            name = name,
            email = email,
            address = address,
            phone = phone,

        )
        emp.save()
        return redirect('home')

    return redirect(request,'index.html')    


def delete(request,id):
    emp=Employees.objects.filter(id=id).delete()
    #emp.delete()
    context = {
        'emp':emp,
    }
    return redirect('home')    


def error(request):
    # Retrieve messages and clear them from the messages framework
    messages_to_display = list(messages.get_messages(request))
    storage = messages.get_messages(request)
    storage.used = True

    return render(request, 'error.html', {'messages_to_display': messages_to_display})

#logger

logger = logging.getLogger(__name__)  #instance

def index(request):

    logger.info("Accessing the index view")

    emp = Employees.objects.all()
    context = {'emp': emp}
    return render(request, 'index.html', context)
    return render(request, 'index.html', context)

