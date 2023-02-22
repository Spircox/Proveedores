import os


def handle_uploaded_file(f, n):
    if os.path.isdir('static/upload/' + n):
        with open('static/upload/' + n + '/' + f.name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
    else:
        os.mkdir('static/upload/' + n, mode=0o755)
        with open('static/upload/' + n + '/' + f.name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)


def handle_uploaded_file2(f, n):
    if os.path.isdir('static/upload/' + n + '/2'):
        with open('static/upload/' + n + '/2' + '/' + f.name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
    else:
        os.mkdir('static/upload/' + n + '/2', mode=0o755)
        with open('static/upload/' + n + '/2' + '/' + f.name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)


def handle_uploaded_file3(f, n):
    if os.path.isdir('static/upload/' + n + '/3'):
        with open('static/upload/' + n + '/3' + '/' + f.name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
    else:
        os.mkdir('static/upload/' + n + '/3', mode=0o755)
        with open('static/upload/' + n + '/3' + '/' + f.name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)


def handle_uploaded_file4(f, n):
    if os.path.isdir('static/upload/' + n + '/4'):
        with open('static/upload/' + n + '/4' + '/' + f.name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
    else:
        os.mkdir('static/upload/' + n + '/4', mode=0o755)
        with open('static/upload/' + n + '/4' + '/' + f.name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
