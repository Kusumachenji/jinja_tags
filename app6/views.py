from django.shortcuts import render 
def jinja_print(request):
    d={'name':'ayan','age':2}

    return render(request,'jinja_print.html',context=d)


# Create your views here.
