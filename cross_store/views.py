from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == "POST":
        data = request.POST
        print("Пост-обработан", data["remember"])
        return render(request, "index.html")
    else:
        return render(request, "index.html")


def shop(request):
    return render(request, "shop.html")

def blog(request):
    return render(request, "blog.html")