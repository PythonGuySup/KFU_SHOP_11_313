from django.shortcuts import render

# Create your views here.
def index(request):
    if request.POST:
        print(request.POST.dict().values())
        return render(request, "index.html")
    else:
        return render(request, "index.html")


def shop(request):
    return render(request, "shop.html")

def blog(request):
    return render(request, "blog.html")