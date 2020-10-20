from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect
from django.shortcuts import render
from app.forms import UploadFileForm, ConfirmationForm
from app.utils import temporary_files, validators


MSG_INVALID_METHOD = 'Only accept GET and POST requests'


def handle_uploaded_file(f):
    path = temporary_files.get_temp_file_path(ensure_dir=True)
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return temporary_files.path_to_name(path)


def import_table(request):
    if request.method == 'GET':
        form = UploadFileForm()
        return render(request, 'app/import_table_form.html', {'form': form})
    elif request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            name = handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/confirm_import_table/{}/'.format(name))
        else:
            return render(request, 'app/import_table_form.html', {'form': form})
    else:
        return HttpResponseNotAllowed(MSG_INVALID_METHOD)


def confirm_import_table(request, uploaded_file_name):
    is_valid = validators.validate_import_table(uploaded_file_name)

    if request.method == 'GET' or not is_valid:
        form = ConfirmationForm()
        return render(request, 'app/confirm_import_table_form.html', {
            'form': form,
            'action': '/confirm_import_table/{}/'.format(uploaded_file_name)
        })
    elif request.method == 'POST':
        return HttpResponse(validators.get_json_from_table(uploaded_file_name))
    else:
        return HttpResponseNotAllowed(MSG_INVALID_METHOD)
