from django.http import HttpResponse
from django.shortcuts import render

# relative import of forms
from .models import PeopleReg
from .forms import RegForm

def index(request):
    return HttpResponse("Please proceed to the registration page: localhost/reg/")

def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}
    # add the dictionary during initialization
    form = RegForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_view.html", context)


def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}
    # add the dictionary during initialization
    context["dataset"] = PeopleReg.objects.all()
    return render(request, "list_view.html", context)


def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}
    # fetch the object related to passed id
    obj = get_object_or_404(PeopleReg, id=id)
    # pass the object as instance in form
    form = RegForm(request.POST or None, instance=obj)
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)
    # add form dictionary to context
    context["form"] = form
    return render(request, "update_view.html", context)


def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}
    # fetch the object related to passed id
    obj = get_object_or_404(PeopleReg, id=id)
    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")
    return render(request, "delete_view.html", context)