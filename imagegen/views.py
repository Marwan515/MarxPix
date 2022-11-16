from django.shortcuts import render, redirect
from django.contrib import messages
from .helpers import daily_date_check, generate_image_ap
from .models import Apod, Rovers, Cameras
from datetime import date

# Create your views here.

def index(request):
    if request.method == "POST":
        request.session["rover"] = request.POST.get("rover_id")
        return redirect("generate_images")
    daily_date_check()
    pics = Apod.objects.filter(apod_date = str(date.today()))
    rvers = Rovers.objects.all()
    return render(request, 'index.html', {"pics": pics[0], "rvers": rvers})
    
def generate_images(request):
    rv = Rovers.objects.get(id = request.session["rover"])
    cams = Cameras.objects.filter(rover_id = rv.id)
    if request.method == "POST":
        rov = request.POST.get("rov")
        camra = request.POST.get("cmra")
        gen = request.POST["gen-by"]
        c = request.POST.get("cmra")
        if len(camra) < 1:
            camra = ""
        else:
            camra = f"camera={c}"
        if gen == "1":
            dt = request.POST.get("earth_date")
            pics = generate_image_ap(rov, f"earth_date={dt}", camra)
        elif gen == "2":
            dt = request.POST.get("sold")
            print(dt)
            if int(dt) > int(rv.max_sol):
                messages.warning(request, "Sol Is More Than The Max Sol")
                return redirect("generate_images")
            pics = generate_image_ap(rov, f"sol={dt}", camra)
        else:
            pics = generate_image_ap(rov, "latest_photos", camra)
        if pics == False:
            messages.info(request, "Did Not Find Images ON This Day")
            return redirect("generate_images")
        return render(request, "generated_imgs.html", {"pics": pics, "r": rv})
    return render(request, 'generate_images.html', {"r": rv, "cams": cams})

def about(request):
    return render(request, 'about.html')