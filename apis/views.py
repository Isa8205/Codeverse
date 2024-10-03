from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from authentication.models import Users
from django.http import JsonResponse

@api_view(['GET'])
def users(request):
    users = Users.objects.all()
    user_data = []

    for user in users:
        user_data.append({
            'name': user.full_name,
            'email': user.email,
            'profile': user.profile
        })

    return JsonResponse(user_data, safe=False)