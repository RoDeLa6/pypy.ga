from django.shortcuts import render
from account import info
from problem import load


def index(request):
    if len(load.PROBLEMS_LIST) == 0:
        load.load_problems()
    data = {'list': load.PROBLEMS_LIST}
    data.update(info.get_data(request.session))
    return render(request, 'index.html', data)