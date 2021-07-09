import json

from django.http import JsonResponse
from .models import Entities, Engagements
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def entities_view(request):
    model = Entities
    params = json.loads(request.body)
    name = params.get("user_name")
    if name is None:
        return JsonResponse({"msg": "no request payload"})
    if request.method == "GET":
        objects = model.objects.all()
        return JsonResponse(serializers.serialize(objects))
    if request.method == "POST":
        if name is not None:
            new_object = Entities(name=name)
            new_object.save()
            return JsonResponse({"msg": "user created"})
    if request.method == "PUT":
        new_name = params.get("new_user_name")
        if new_name is not None:
            obj = model.objects.get(name=name)
            if obj is not None:
                obj.name = new_name
                obj.save()
            return JsonResponse({"msg": "user not registered"})
        return JsonResponse({"msg": "request payload incorrect"})
    if request.method == "DELETE":
        obj = model.objects.get(name=name)
        if obj is not None:
            obj.delete()
        return JsonResponse({"msg": "name not found"})


@csrf_exempt
def engagements_view(request):
    model = Engagements
    params = json.loads(request.body)
    user_name, activity = params.get("user_name"), params.get("activity")
    if user_name is None or activity is None:
        return JsonResponse({"msg": "no request payload"})
    user = Entities.objects.get(name=user_name)
    if user is None:
        return JsonResponse({"msg": "user not registered"})
    if request.method == "GET":
        objects = model.objects.all()
        return JsonResponse(serializers.serialize(objects))
    if request.method == "POST":
        # try:
        engagements_obj = Engagements(user_name=user, name=activity)
        engagements_obj.save()
        return JsonResponse({"msg": "user's activity created"})
        # except:
        #     return JsonResponse({"msg": "error while processing request"})
    if request.method == "PUT":
        # try:
        engagements_obj = Engagements(user_name=user)
        engagements_obj.name = activity
        return JsonResponse({"msg": "user's activity changed"})
        # except:
        #     return JsonResponse({"msg": "error while processing request"})
    if request.method == "DELETE":
        # try:
        engagements_obj = Engagements(user_name=user)
        engagements_obj.delete()
        return JsonResponse({"msg": "user's activity removed"})
        # except:
        #     return JsonResponse({"msg": "error while processing request"})


@csrf_exempt
def user_register(request):
    params = json.loads(request.body)
    user_name = params.get("user_name")
    if user_name is None:
        return JsonResponse({"msg": "no request payload"})
    if request.method == "POST":
        # try:
        new_object = Entities(name=user_name)
        new_object.save()
        return JsonResponse({"msg": "user registered. please login"})
        # except:
        #     return JsonResponse({"msg": "error while processing request"})


@csrf_exempt
def user_login(request):
    params = json.loads(request.body)
    user_name, activity = params.get("user_name"), params.get("activity")
    if user_name is None or activity is None:
        return JsonResponse({"msg": "request payload incorrect"})
    user = Entities.objects.get(name=user_name)
    if user is None:
        return JsonResponse({"msg": "user not registered, please register user"})
    if request.method == "POST":
        # try:
        all_objects = Engagements.objects.all()
        if len(all_objects) == 0:
            return JsonResponse({"msg": "add engagement entry for user"})
        else:
            engagement_entry = Engagements.objects.get(user_name=user)
        if engagement_entry is not None:
            if engagement_entry.current_status:
                return JsonResponse({"msg": "user is already logged in"})
            engagement_entry.current_status = True
            engagement_entry.save()
            return JsonResponse({"msg": "user logged in"})
        return JsonResponse({"msg": "add engagement entry for user"})
        # except:
        #     return JsonResponse({"msg": "error while processing request"})


@csrf_exempt
def user_logout(request):
    params = json.loads(request.body)
    user_name, activity = params.get("user_name"), params.get("activity")
    if user_name is None or activity is None:
        return JsonResponse({"msg": "request payload incorrect"})
    user = Entities.objects.get(name=user_name)
    if user is None:
        return JsonResponse({"msg": "user not registered, please register user"})
    if request.method == "POST":
        last_entry = Engagements.objects.get(user_name=user, name=activity)
        if last_entry.current_status:
            object.current_status = False
            object.save()
            return JsonResponse({"msg": "user logged out"})
        return JsonResponse({"msg": "user is already logged out"})
