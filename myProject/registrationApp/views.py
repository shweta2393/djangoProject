from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render

# relative import of forms
from .models import PeopleReg
from .forms import RegForm

def index(request):
    return HttpResponse("Please proceed to the registration page: localhost/reg/")

def create_view(request):
    data = serializers.serialize('json', PeopleReg.objects.all())
    # return HttpResponse(data, content_type='application/json')
    return JsonResponse(data, status=200)


def list_view(request):
    # Query the database to get PeopleReg objects
    queryset = PeopleReg.objects.all()
    # Serialize the queryset into JSON format
    data = serialize('json', queryset)
    # Return JSON response
    return JsonResponse(data, safe=False)


def update_view(request, id):
    context = {}
    obj = get_object_or_404(PeopleReg, id=id)
    form = RegForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        # Return success message as JSON response
        return JsonResponse({'message': 'Update successful'})
    # If form is invalid, return form errors as JSON response
    errors = form.errors.as_json()
    return JsonResponse({'errors': errors}, status=400)

def delete_view(request, id):
    # Fetch the object related to the passed id
    obj = get_object_or_404(PeopleReg, id=id)
    if request.method == "POST":
        # Delete object
        obj.delete()
        # Return success message as JSON response
        return JsonResponse({'message': 'Object deleted successfully'})
    # If request method is not POST, return error message as JSON response
    return JsonResponse({'error': 'Method not allowed'}, status=405)