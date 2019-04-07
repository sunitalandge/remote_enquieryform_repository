from django.shortcuts import render
from .models import EnquiryData
#from django.http.response import HttpResponse

def EnquieryView(request):
    if request.method=="POST":
        fname=request.POST.get('fname','')
        lname=request.POST.get('lname','')
        email=request.POST.get('email','')
        mobile=request.POST.get('mobile','')
        username=request.POST.get('uname','')
        password=request.POST.get('pwd','')

        data = EnquiryData(
            first_name=fname,
            last_name=lname,
            email=email,
            mobile=mobile,
            username=username,
            password=password

        )
        data.save()
        return render(request,'enquiery.html')

    else:
        return render(request,'enquiery.html')


