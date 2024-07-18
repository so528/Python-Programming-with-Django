def my_view(request):
    if request.method == 'GET':
        return HttpResponse('result')
