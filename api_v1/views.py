import ast
import json

import requests
from django.shortcuts import render
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView


class SubscriberChargingRecordsView(APIView):
    authentication_classes = (permissions.IsAuthenticated, )

    def post(self, request, format=None):
        try:
            user = request.user
            json_data = json.loads(request.body)
            from_date = json_data['from_date']
            to_date = json_data['to_date']
            number = user.phone
        except:
            return Response({'code': 406,
                             'body': 'INVALID_ARGUMENTS'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        try:
            headers = {
                'Content-Type': 'application/json', }
            data = {
                "username": "app",
                "password": "2423@#qefwe!!",
                "number": number,
                "from_date": from_date,
                "to_date": to_date,
            }
            data = json.dumps(data)
            r = requests.post("http://192.168.163.41:8000/app_v1/SubscriberChargingRecords/", data=data, headers=headers)
            return Response(json.loads(r.text), status=r.status_code)
        except requests.exceptions.RequestException as e:
            return Response({'error': 'Connection error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SubscriberPackageRecordsView(APIView):
    authentication_classes = (permissions.IsAuthenticated, )

    def post(self, request, format=None):
        try:
            user = request.user
            json_data = json.loads(request.body)
            from_date = json_data['from_date']
            to_date = json_data['to_date']
            number = user.phone
        except:
            return Response({'code': 406,
                             'body': 'INVALID_ARGUMENTS'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        try:
            headers = {
                'Content-Type': 'application/json', }
            data = {
                "username": "app",
                "password": "2423@#qefwe!!",
                "number": number,
                "from_date": from_date,
                "to_date": to_date,
            }
            data = json.dumps(data)
            r = requests.post("http://192.168.163.41:8000/app_v1/SubscriberPackageRecords/", data=data, headers=headers)
            return Response(json.loads(r.text), status=r.status_code)
        except requests.exceptions.RequestException as e:
            return Response({'error': 'Connection error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PackageDisplayView(APIView):
    authentication_classes = (permissions.IsAuthenticated, )

    def get(self, request, format=None):
        try:
            user = request.user
            number = user.phone
        except:
            return Response({'code': 406,
                             'body': 'INVALID_ARGUMENTS'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        try:
            headers = {
                'Content-Type': 'application/json',}
            data = {
                "username": "app",
                "password": "2423@#qefwe!!",
                "number": number,
                "from_date": "2019-03-15 18:04:00",
                "to_date": "2019-07-04 18:04:00",
            }
            data = json.dumps(data)
            r = requests.post("http://192.168.163.41:8000/app_v1/PackageDisplay/", data=data, headers=headers)
            return Response(json.loads(r.text), status=r.status_code)
        except requests.exceptions.RequestException as e:
            return Response({'error': 'Connection error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@permission_classes((permissions.AllowAny,))
class PackagesListView(APIView):

    def get(self, request, format=None):
        try:
            r = requests.get("http://192.168.163.41:8000/app_v1/PackagesList/")
            return Response(json.loads(r.text), status=r.status_code)
        except requests.exceptions.RequestException as e:
            return Response({'error': 'Connection error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CallSaleView(APIView):

    def get(self, request, format=None):
        try:
            user = request.user
            json_data = json.loads(request.body)
            number = int(json_data['number'])
        except:
            return Response({'code': 406,
                             'body': 'INVALID_ARGUMENTS'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        try:
            headers = {
                'Content-Type': 'application/json', }
            data = {
                "username": "app",
                "password": "2423@#qefwe!!",
                "number": number,
            }
            data = json.dumps(data)
            r = requests.post("http://192.168.163.41:8000/webservice/CallSale/", data=data, headers=headers)
            return Response(json.loads(r.text), status=r.status_code)
        except requests.exceptions.RequestException as e:
            return Response({'error': 'Connection error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PinLessChargingNumberView(APIView):

    def post(self, request, format=None):
        try:
            user = request.user
            json_data = json.loads(request.body)
            number = int(json_data['number'])
            dialer = user.phone
            amount = int(json_data['amount'])
        except:
            return Response({'code': 1,
                             'body': 'INVALID_ARGUMENTS'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        try:
            headers = {
                'Content-Type': 'application/json', }
            data = {
                "username": "app",
                "password": "2423@#qefwe!!",
                "number": number,
                "dialer": dialer,
                "amount": amount,
            }
            data = json.dumps(data)
            r = requests.post("http://192.168.163.41:8000/webservice/PinLessChargingNumber/", data=data, headers=headers)
            return Response(json.loads(r.text), status=r.status_code)
        except requests.exceptions.RequestException as e:
            return Response({'error': 'Connection error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PackageCallSaleView(APIView):

    def post(self, request, format=None):
        try:
            user = request.user
            json_data = json.loads(request.body)
            number = int(json_data['number'])
            package_id = int(json_data['package_id'])
        except:
            return Response({'code': 1,
                             'body': 'INVALID_ARGUMENTS'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        try:
            headers = {
                'Content-Type': 'application/json', }
            data = {
                "username": "app",
                "password": "2423@#qefwe!!",
                "number": number,
                "package_id": package_id,
            }
            data = json.dumps(data)
            r = requests.post("http://192.168.163.41:8000/webservice/PackageCallSale/", data=data, headers=headers)
            return Response(json.loads(r.text), status=r.status_code)
        except requests.exceptions.RequestException as e:
            return Response({'error': 'Connection error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PackageActivationView(APIView):

    def post(self, request, format=None):
        try:
            user = request.user
            json_data = json.loads(request.body)
            package_id = int(json_data['package_id'])
            number = int(json_data['number'])
        except:
            return Response({'code': 1,
                             'body': 'INVALID_ARGUMENTS'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        try:
            headers = {
                'Content-Type': 'application/json',}
            data = {
                "username": "app",
                "password": "2423@#qefwe!!",
                "number": number,
                "package_id": package_id,
            }
            data = json.dumps(data)
            r = requests.post("http://192.168.163.41:8000/webservice/PackageActivation/", data=data, headers=headers)
            return Response(json.loads(r.text), status=r.status_code)
        except requests.exceptions.RequestException as e:
            return Response({'error': 'Connection error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
