import os


def handle_uploaded_file(f, n):
    if os.path.isdir('files/static/upload/' + n):
        with open('files/static/upload/' + n + '/' + f.name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
    else:
        os.mkdir('files/static/upload/' + n, mode=0o755)
        with open('files/static/upload/' + n + '/' + f.name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)


def handle_uploaded_file_rut(f, n):
    if os.path.isdir('files/static/upload/' + n + '/rut'):
        with open('files/static/upload/' + n + '/rut' + '/' + f.name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
    else:
        os.mkdir('files/static/upload/' + n + '/rut', mode=0o755)
        with open('files/static/upload/' + n + '/rut' + '/' + f.name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
