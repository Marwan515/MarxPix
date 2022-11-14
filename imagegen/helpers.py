import requests
import json
from .models import Rovers, Apod, Cameras
from datetime import date, timedelta
import os

NASA_KEY = os.environ["NASA_API_KEY"]

def check_rovers():
    rover_data = Rovers.objects.all()
    if len(rover_data) > 0:
        for r in rover_data:
            if r.rover_status == "active" and r.max_date <= str(date.today() - timedelta(days=1)):
                named = r.rover_name
                try:
                    url = f"https://api.nasa.gov/mars-photos/api/v1/manifests/{named}/?api_key={NASA_KEY}"
                    response = requests.get(url)
                except requests.RequestException:
                    None
                p = response.json()
                j = p["photo_manifest"]
                Rovers.objects.filter(id=r.id).update(max_sol = str(j["max_sol"]), max_date = str(j["max_date"]), total_photos = j["total_photos"])
            else:
                return
    else:
        return

def seed_rover_data():
    rover_n = ['curiosity', 'spirit', 'opportunity', 'perseverance']
    rver_data = Rovers.objects.all()
    if len(rver_data) == 0:
        for name in rover_n:
            try:
                url = f"https://api.nasa.gov/mars-photos/api/v1/manifests/{name}/?api_key={NASA_KEY}"
                response = requests.get(url)
            except requests.RequestException:
                return None
            try:
                p = response.json()
                j = p["photo_manifest"]
            except KeyError:
                return None
            rver = Rovers(rover_name = str(j["name"]), rover_landing_date = str(j["landing_date"]), rover_launching_date = str(j["launch_date"]), rover_status = str(j["status"]), max_sol = str(j["max_sol"]), max_date = str(j["max_date"]), total_photos = j["total_photos"], first_photos = j["photos"][0]["earth_date"])
            rver.save()
    else:
        return    

def apod_data():
    ad = Apod.objects.filter(apod_date = str(date.today()))
    if not ad:
        url = f"https://api.nasa.gov/planetary/apod/?api_key={NASA_KEY}"
        try:
            res = requests.get(url)
        except requests.RequestException:
            return None
        # parse Data
        try:
            j = res.json()
            k = Apod.objects.filter(title=j["title"])
            if not k:
                apd = Apod(title = str(j["title"]), explaination = str(j["explanation"]), hdurl = str(j["hdurl"]), media_type = str(j["media_type"]), urli = str(j["url"]), apod_date = str(j["date"]))
                apd.save()
            else:
                return None
        except KeyError:
            print("parse Error")
    else:
        return


def daily_date_check():
    check_rovers()
    apod_data()
    seed_rover_data()
    cameras_seed()

def cameras_seed():
    ojb = Cameras.objects.filter(cam = "fhaz")
    if not ojb:
        psn = Rovers.objects.get(rover_name = 'Perseverance')
        o = Rovers.objects.get(rover_name = 'Opportunity')
        s = Rovers.objects.get(rover_name = 'Spirit')
        c = Rovers.objects.get(rover_name = 'Curiosity')
        perseverance_c = [["edl_rucam", "Rover Up-Look Camera"], ["edl_rdcam", "Rover Down-Look Camera"], ["edl_ddcam", "Descent Stage Down-Look Camera"], ["edl_pucam1", "Parachute Up-Look Camera A"], ["edl_pucam2", "Parachute Up-Look Camera B"], ["navcam_left", "Navigation Camera - Left"], ["navcam_right", "Navigation Camera - Right"], ["mcz_right", "Mast Camera Zoom - Right"], ["mcz_left", "Mast Camera Zoom - Left"], ["front_hazcam_left_a", "Front Hazard Avoidance Camera - Left"], ["front_hazcam_right_a", "Front Hazard Avoidance Camera - Right"], ["rear_hazcam_left", "Rear Hazard Avoidance Camera - Left"], ["rear_hazcam_right", "Rear Hazard Avoidance Camera - Right"], ["skycam", "Meda Skycam"], ["sherloc_watson", "Sherloc Watson Camera"]]
        cams = [["fhaz", "Front Hazard Avoidance Camera"], ["rhaz", "Rear Hazard Avoidance Camera"], ["navcam", "Navigation Camera"], ["pancam", "Panoramic Camera"], ["minites", "Miniature Thermal Emission Spectrometer (Mini-TES)"]]
        curiosity_c = [cams[0], cams[1], cams[2], ["mast", "Mast Camera"], ["chemcam", "Chemistry and Camera Complex"], ["mahli", "Mars Hand Lens Imager"], ["mardi", "Mars Descent Imager"]]
        for p in perseverance_c:
            rec = Cameras(cam = p[0], cam_full = p[1], rover_id = psn)
            rec.save()
        for p in cams:
            rec = Cameras(cam = p[0], cam_full = p[1], rover_id = o)
            rec2 = Cameras(cam = p[0], cam_full = p[1], rover_id = s)
            rec.save()
            rec2.save()
        for p in curiosity_c:
            rec = Cameras(cam = p[0], cam_full = p[1], rover_id = c)
            rec.save()
    return


def generate_image_ap(rov, gen, cams=""):
    p = "photos"
    img_url = f"https://mars-photos.herokuapp.com/api/v1/rovers/{rov}/{p}?page=1&{gen}&{cams}"
    if gen == "latest_photos":
        img_url = f"https://mars-photos.herokuapp.com/api/v1/rovers/{rov}/{gen}?page=1&{cams}"
    try:
        response = requests.get(img_url)
    except requests.RequestException:
        return None
    if gen == "latest_photos":
        pht = response.json()
        photos = pht["latest_photos"]
    else:
        pht = response.json()
        photos = pht["photos"]
    if len(photos) < 1:
        return False
    return photos
