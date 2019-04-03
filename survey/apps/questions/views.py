from django.shortcuts import render, HttpResponse, redirect
  
def index(request):
    if not "count" in request.session:
        request.session["count"] = 0    
    return render(request, "questions/index.html")
def surveys(request):
    request.session["name"] = request.POST["name"]
    request.session["Dojo_location"] = request.POST["Dojo_location"]
    request.session["Fav_lang"] = request.POST["Fav_lang"]
    request.session["message"] = request.POST["message"]
    request.session["count"] += 1
    return redirect('surveys/process')
def process(request):
    return render(request, "questions/result.html")
def result(request):
    request.session["count"] = 0
    return redirect('/')


