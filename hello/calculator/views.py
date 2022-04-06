from django.http import HttpResponse
from django.shortcuts import render

def intro(request):
    return render(request,'calchomepage.html')

def operation(request):
     val1=int(request.GET['num1'])
     val2=int(request.GET['num2'])
     operation=request.GET['operation']
     if operation in ['+','-','*','/']:
         if operation=='+':
             res=val1+val2
             return render(request,'calcresult.html',{'result':res,'operation':'addition'})
         if operation=='-':
             res=abs(val1-val2)
             return render(request,'calcresult.html',{'result':res,'operation':'subtraction'})
         if operation=='*':
             res=val1*val2
             return render(request,'calcresult.html',{'result':res,'operation':'multiplication'})
         if operation=='/':
             res=val1/val2
             return render(request,'calcresult.html',{'result':res,'operation':'division'})
     else:
         return HttpResponse('<h1>INVALID INPUT</h1>')