from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE
from django.core.files.storage import FileSystemStorage
def button(request):
    return render(request, 'index.html')




def external1(request1):
    return render(request1,'about.html')
def external2(request1):
	name = request1.POST.get("first_name")
	email = request1.POST.get("email")
	phone  = request1.POST.get("phone")
	message = request1.POST.get("message")
	if name:
		out = run([sys.executable,'C:\\python\\button\\mail.py',name,email,message,phone],shell=False,stdout=PIPE)
		
		return render(request1,'contactus.html')
		
			

	else:
	
		return render(request1,'contactus.html')


def external(request):
    inp = request.POST.get("param")
    inp1 = request.POST.get("crop")
    out=run([sys.executable,'C:\\python\\button\\test.py',inp,inp1],shell=False,stdout=PIPE)

    return render(request,'output.html',{'data1':out.stdout})
