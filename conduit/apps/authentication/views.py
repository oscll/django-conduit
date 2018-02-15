from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import authentication, exceptions
from rest_framework import serializers
from .renderers import UserJSONRenderer
from .serializers import (
    LoginSerializer, RegistrationSerializer, UserSerializer
)
from .models import User
from django.core.mail import send_mail, BadHeaderError


class RegistrationAPIView(APIView):
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})

        # The create serializer, validate serializer, save serializer pattern
        # below is common and you will see it a lot throughout this course and
        # your own work later on. Get familiar with it.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        #User is created but active is false
        new_user = User.objects.get(email=user.get('email'))
        new_user.token_password = new_user._generate_password_token()
        new_user.save()
        #Generate a toke password and save 
        print('----------')
        try:
            subject = 'Activacion Email'
            message = 'Para activar la cuenta haga click en el siguiente link : http://localhost:4200/#/activation/'+new_user.token_password+'/'+new_user.email
            email = new_user.email
            send_mail(subject, message, 'oscllweb@gmail.com', [email])
        except BadHeaderError:
            return Response({
                    'status': 'false',
                    'message': 'BadHeaderError for your message'
                }, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        #Send Email

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})

        # Notice here that we do not call `serializer.save()` like we did for
        # the registration endpoint. This is because we don't actually have
        # anything to save. Instead, the `validate` method on our serializer
        # handles everything we need.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        # There is nothing to validate or save here. Instead, we just want the
        # serializer to handle turning our `User` object into something that
        # can be JSONified and sent to the client.
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        user_data = request.data.get('user', {})

        serializer_data = {
            'username': user_data.get('username', request.user.username),
            'email': user_data.get('email', request.user.email),

            'profile': {
                'bio': user_data.get('bio', request.user.profile.bio),
                'image': user_data.get('image', request.user.profile.image)
            }
        }

        # Here is that serialize, validate, save pattern we talked about
        # before.
        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

class PasswordAPIView(APIView):

    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        data = request.data.get('data',None)
        email = data.get('email')
        
        try:
            user = User.objects.get(email= email)
            user.token_password = user._generate_password_token()
            user.save()
            subject = "Recover Password"
            message = 'Para cambiar la password haga click en el siguiente link : http://localhost:4200/#/changepassword/'+user.token_password+'/'+user.email
            try:
                send_mail(subject, message, 'oscllweb@gmail.com', [email])
            except BadHeaderError:
                return Response({
                        'status': 'false',
                        'message': 'BadHeaderError for your message'
                    }, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        except:
            raise serializers.ValidationError(
                'An email address is not registered.'
            )

        return Response({'status': 'true'}, status=status.HTTP_200_OK)

class ChangePasswordAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        print(request.data)
        token = request.data.get('data',None).get('token')
        password = request.data.get('data',None).get('password')
        email = request.data.get('data',None).get('email')
        if token == 'false' : 
            token = 'true'

        try:
            user = User.objects.get(email=email)
            if user.token_password == token:
                user.set_password(password)
            else:
                raise serializers.ValidationError(
                    'Por favor intentelo mas tarde.'
                )    
            user.token_password = 'false'
            user.save()
        except:
            raise serializers.ValidationError(
                'Por favor intentelo mas tarde.'
            )


        return Response({'status': 'true'}, status=status.HTTP_200_OK)

class ActiveUserEmailAPIView(APIView):

    def post(self, request, format=None):
        print(request.data)
        token = request.data.get('data',None).get('token')
        email = request.data.get('data',None).get('email')
        if token == 'false' : 
            token = 'true'
        try:
            user = User.objects.get(email=email)
            if user.token_password == token:
                user.is_active = True
            else:
                raise serializers.ValidationError(
                    'El token no es valido por favor intentelo mas tarde.'
                )    
            user.token_password = 'false'
            user.save()
        except:
            raise serializers.ValidationError(
                'Por favor intentelo mas tarde.'
            )
        return Response({'status': 'true'}, status=status.HTTP_200_OK)


