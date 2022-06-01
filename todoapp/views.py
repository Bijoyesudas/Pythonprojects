from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy

from todoapp.forms import TodoForm
from todoapp.models import task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class taskdeleteview(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')

class taskupdatview(UpdateView):
    model = task
    template_name = 'edit.html'
    context_object_name = 'task'
    fields = ['name','priority','date']

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class taskdetailview(DetailView):
    model = task
    template_name = 'detail.html'
    context_object_name = 'task'

class tasklistview(ListView):
    model = task
    template_name = 'home.html'
    context_object_name = 'Task'

def index(request):
    Task1 = task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        Task=task(name=name,priority=priority,date=date)
        Task.save()

    return render(request,'home.html',{'Task':Task1})

def delete(request,id):
    if request.method=='POST':
        Task=task.objects.get(id=id)
        Task.delete()
        return redirect('/')
    return render(request,'delete.html',)

def update(request,id):
    Task=task.objects.get(id=id)
    f=TodoForm(request.POST or None,instance=Task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'update.html',{'f':f,'Task':Task})
