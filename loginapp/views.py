from django.shortcuts import render

def getLoginpage(request):
    return  render(request,'login.html')
def checkLogin(request):
    user=request.POST['un']
    password=request.POST['pw']
    if user=='vivek' and password=='jango':
        return render(request,'success.html',{'username':user})
    else:
        return render(request,'unsuccess.html',{'username':user})
# Create your views here.
