from django.shortcuts import render, redirect

def index(request):
    if 'key' in request.session:
        print('key exists!')
        request.session['key']+=1
    else:
        print("key 'key' does NOT exist")
        request.session['key'] = 0

    return render(request, "index.html")

def _del(request):
    del request.session['key']
    return redirect('/')
