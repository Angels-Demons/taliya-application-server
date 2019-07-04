import random

from accounts.models import User, create_profile, UserManager
from api import sms_send, sms
from django.shortcuts import render
from accounts import models
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.Serializers import ProfileSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)


def authenticate(request):
    token = request.META['HTTP_AUTHORIZATION']
    token = str(token).split(' ')[1]
    phone = request.POST['phone']
    owner_of_phone = User.objects.filter(phone=phone).first()
    owner_of_token = Token.objects.filter(key=token).first()
    if not (owner_of_phone or owner_of_token):
        data = {'error': 'error: token or phone not found'}
        return Response(data, status=HTTP_404_NOT_FOUND)
    if owner_of_token.user == owner_of_phone:
        return owner_of_phone
    else:
        data = {'error': 'error: invalid credentials'}
        return Response(data, status=HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def profile(request):
    resp_profile = {'phone': '9367498998',
                    'token': '12345678901234567890',
                    'credit': 1000}
    return Response(resp_profile)


@csrf_exempt
@api_view(["POST"])
def my_profile_api(request):
    user = authenticate(request)
    if not isinstance(user, User):
        print(user.__class__)
        print(user)
        return user
    return Response(ProfileSerializer(user.profile).data)


@permission_classes((AllowAny,))
class RegisterView(APIView):
    # permission_classes = (AllowAny,)
    def post(self, request):
        # serializer.save()
        manager = models.UserManager()
        password = random.randint(1000, 9999)
        print(password)
        phone = request.POST['phone']
        user = User.objects.filter(phone=phone).first()
        if user:
            # print('user exists')
            user.set_password(password)
            user.save()
        else:
            # print('new user')
            user = manager.create_user(phone, password)
            # modify
            # you can set the tariff_id here
            profile = create_profile(user)
        # sms_send.send_sms(phone, password)
        sms.verify(phone, password)

        return Response({'success': 'success'},
                        status=HTTP_200_OK)

    #     serializer = UserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         # serializer.save()
    #         manager = models.UserManager()
    #         password = random.randint(1000, 9999)
    #         print(password)
    #         phone = serializer.validated_data['phone']


class LoginView(APIView):
    pass


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    phone = request.data.get("phone")
    password = request.data.get("password")
    if phone is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=phone, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    user.set_unusable_password()
    user.save()
    return Response({'token': token.key},
                    status=HTTP_200_OK)


# @csrf_exempt
# @api_view(["POST"])
# @permission_classes((AllowAny,))
def sign(request):
    user_manager = UserManager()
    user_manager.create_staffuser(request.GET['phone'], request.GET['password'])
    return Response({'success': 'success'},
                    status=HTTP_200_OK)
