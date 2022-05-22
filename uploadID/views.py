from django.shortcuts import render
from .models import Id_item
from  .forms import UploadForm
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    items = Id_item.objects.all()
    context = {'items': items}
    return render(request, 'homepage.html', context)

def upload_lost_id (request):
    form =UploadForm()
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            Lost_id = Id_item(
                ID_num = form.cleaned_data['ID_num'],
                Location_found = form.cleaned_data['Location_found'],
                Pick_up_location = form.cleaned_data['Pick_up_location'],
                Image = form.cleaned_data['Image']
            )
            Lost_id.save()
            return HttpResponse('Form has been submitted')
        else:
            return HttpResponse('Invalid form')
    context = {'form': form}
    return render(request, 'upload_lost_id.html', context)

def id_detail(request, pk):
    lost_id = Id_item.objects.get(pk=pk)
    context = {'lost_id': lost_id}
    return render(request, 'id_detail.html', context)