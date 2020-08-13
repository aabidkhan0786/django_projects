from django.shortcuts import render,HttpResponseRedirect
from ToDo_App.models import Task

# Create your views here.
def home(request):
    context={"success": False}
    if request.method=="POST":
        title=request.POST["title"]
        desc=request.POST["desc"]
        ins = Task(title=title,desc=desc)
        ins.save()
        context={"success": True}


    return render(request,"home.html",context)

def task(request):
    alltasks = Task.objects.all()
    context = {"tasks":alltasks}
    return render(request,"task.html",context) 


def delete(request,id):
    context={"delete": False}
    if request.method == "POST":
        d = Task.objects.get(pk=id)
        d.delete()
        context={"delete": True}
        return render(request,"home.html",context)
