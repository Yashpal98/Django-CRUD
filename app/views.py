from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from .models import Person
from .forms import PersonForm
from .filters import ListFilter

# Create your views here.

def home(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Submit Complete")
        else:
            return HttpResponse(status=400)
    else:
        form = PersonForm()

    return render(request, 'index.html', {'form':form})

def list(request):
    persons = Person.objects.all()
    filter = ListFilter(request.GET, queryset=persons)
    persons = filter.qs
    # print(filter.qs)
    
    return render(request, 'list.html', {'persons':persons, 'filter':filter})

def edit(request, id):
    person = Person.objects.get(id=id)
    # if request.method == 'POST':
    if request.method == "POST" and request.is_ajax():
        form = PersonForm(request.POST, instance=person)
        # print(form)
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()

            # print(request.POST)
            return JsonResponse({"name": name}, status=200)
            # return redirect("Edit", id=id)
        
        else:
            return HttpResponse(status=400)

    else:
        form = PersonForm(instance=person)
        return render(request, 'edit.html', {'person':person,'form':form})

def delete(request, id):
    person = Person.objects.get(id=id)
    person.delete()
    return redirect("List")