from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail, BadHeaderError
from rest_framework import permissions, status, views, viewsets
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.response import Response


class ContactView(views.APIView): 
    def post(self, request, format=None):
        body = request.data
        data = body.get('data',None)
        subject = data.get('subject',None)
        name = data.get('name',None)
        message = data.get('message',None)
        email = data.get('email',None)
        try:
            send_mail(subject, message, 'oscllweb@gmail.com', [email])
        except BadHeaderError:
            return Response({
                    'status': 'false',
                    'message': 'BadHeaderError for your message'
                }, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        return Response({
                    'status': 'true',
                    'message': 'Success! Thank you for your message'
                }, status=status.HTTP_200_OK)
