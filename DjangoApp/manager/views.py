import os

from django.conf import settings
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import FileResponse, HttpResponse, Http404,  StreamingHttpResponse, FileResponse

from .models import Staff, Meal, Banner, GalleryImage, Room, BaseInfo, Document


def homepage(request):
    staff = Staff.objects.filter(is_active=True)
    meals = Meal.objects.filter(is_active=True)
    banners = Banner.objects.filter(is_active=True)
    gallery_images = GalleryImage.objects.filter(is_active=True)
    rooms = Room.objects.all()
    baseInfo = BaseInfo.objects.all()[:1]
    return render(request, 'index.html', {'staff':staff, 'meals':meals, 'banners':banners, 'gallery_images':gallery_images, 'rooms':rooms, 'baseInfo':baseInfo})


def about(request):
    baseInfo = BaseInfo.objects.all()[:1]
    return render(request, 'about.html', {'baseInfo':baseInfo})


def contact(request):
    return render(request, 'contact.html', {})


def documents(request):
    documents = Document.objects.filter(is_active=True)
    return render(request, 'documents.html', {'documents':documents})

def download(request, path):
    # get the download path
    download_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(download_path):
        with open(download_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(download_path)
            return response
    raise Http404


def file_response_download(request, file_path):
    ext = os.path.basename(file_path).split('.')[-1].lower()
    # cannot be used to download py, db and sqlite3 files.
    if ext not in ['py', 'db',  'sqlite3']:
        response = FileResponse(open(file_path, 'rb'))
        response['content_type'] = "application/octet-stream"
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
        return response
    else:
        raise Http404


def document_detail(request, id):
    document = Document.object.get(id=id)
    return render(request, 'document_detail.html', {'document':document})
