from django.shortcuts import render, redirect
from account import info
from . import load
from submit.models import Submit

HELLO_WORLD_CODE = 'print("Hello World!")'


def index(request, problem):
    data = {
        'problem_id': problem,
        'problem_md': load.PROBLEM_MD[str(problem)],
    }
    user_id = info.get_user_id(request.session)
    if user_id is not None:
        recent_submit = Submit.objects.filter(problem_id=problem, user_id=user_id)
        if recent_submit.exists():
            submit = recent_submit.last()
            data['code'] = submit.code
        else:
            data['code'] = HELLO_WORLD_CODE
    else:
        data['code'] = HELLO_WORLD_CODE

    data.update(info.get_data(request.session))

    return render(request, 'problem.html', data)


def reload(request):
    load.load_problems()
    return redirect('/')
