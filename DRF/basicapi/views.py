from rest_framework.authtoken.models import Token

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
# rest_framework import
from rest_framework.views import APIView
from rest_framework import authentication,generics,mixins,permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .permissions import isstaffpermission
from .models import *
from .serializers import *
from .emails import *
import json, requests
# token auth
from rest_framework.authentication import TokenAuthentication

User = get_user_model()
# genericsview start

# create data

class movielistapicreateview(generics.ListCreateAPIView):
    queryset = movie.objects.all()
    serializer_class = movieserializer
    authentication_classes = [
        authentication.TokenAuthentication
    ]
    # permission_classes = [isstaffpermission]

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        serializer.save()
moviecreateview = movielistapicreateview.as_view()

class signup(APIView):
    def post(self,request):
        try:
            data = request.data
            serializer = signupserialzer(data=data)
            if serializer.is_valid():
                serializer.save()
                send_otp_via_email(serializer.data['email'])
                return Response({
                    'status':200,
                    'message':'User registrated successfully',
                    'data':serializer.data,
                })
            return Response({
                'status': 400,
                'message': 'An error Occured',
                'data': serializer.errors,
            })
        except Exception as e:
            print(e)
signupapi = signup.as_view()

class verifyotp(APIView):
    def post(self,request):
        try:
            data = request.data
            serializer = verifyserialzer(data=data)
            if serializer.is_valid():
                email = serializer.data['email']
                otp = serializer.data['otp']
                user = User.objects.filter(email=email)
                if not user.exists():
                    return Response({
                        'status': 400,
                        'message': 'something went wrong',
                        'data': 'invalid email',
                    })

                if user[0].otp != otp:
                    return Response({
                        'status': 400,
                        'message': 'something went wrong',
                        'data': 'invalid otp',
                    })
                user = user.first()
                user.is_verified = True
                user.save()
                return Response({
                    'status': 200,
                    'message': 'User verified successfully',
                    'data': {},
                })
        except Exception as e:
            print(e)
verify = verifyotp.as_view()
# class signup(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = signupserialzer
#
#     def perform_create(self, serializer):
#         # serializer.save(user=self.request.user)
#         print(serializer.validated_data)
#         user = serializer.save()
# signupapi = signup.as_view()

# retrieve data
class movieapiview(generics.RetrieveAPIView):
    queryset = movie.objects.all()
    serializer_class = movieserializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # lookup_field = 'pk'
movieview = movieapiview.as_view()

# update data
class movieapiupdateview(generics.UpdateAPIView):
    queryset = movie.objects.all()
    serializer_class = movieserializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content=instance.title

movieupdateview = movieapiupdateview.as_view()

# delete view
class movieapideleteview(generics.DestroyAPIView,generics.RetrieveAPIView):
    queryset = movie.objects.all()
    serializer_class = movieserializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

moviedeleteview = movieapideleteview.as_view()

# mixins

class moviemixinview(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):
    queryset = movie.objects.all()
    serializer_class = movieserializer
    lookup_field = 'pk'
    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request)

    def post(self, request, *args, **kwargs):
        return self.create(request)
moviemixinview = moviemixinview.as_view()
    # def post(self):
# class movielistapiview(generics.ListAPIView):
#
#     queryset = movie.objects.all()
#     serializer_class = movieserializer
#     # lookup_field = 'pk'
# movielistview = movielistapiview.as_view()

# genericsview end

# functionbasedview
# @api_view(["GET","POST"])
# def moviealtview(request,pk=None, *args, **kwargs):
#     print(request.data)
#     method = request.method
#     if method == "GET":
#         if pk is not None:
#             obj = get_object_or_404(movie, pk=pk)
#             data = movieserializer(obj, many=False).data
#             return Response(data)
#
#         queryset = movie.objects.all()
#         data = movieserializer(queryset, many=True).data
#         return Response(data)
#     if method == "POST":
#         serial = movieserializer(data=request.data)
#         if serial.is_valid(raise_exception=True):
#             serial.save()
#             print(serial.data)
#         # instance = movie.objects.all().order_by("?").first()
#         # data={}
#         # if instance:
#         #     data = movieserializer(instance).data
#             return Response(serial.data)

# functionbasedview end
@api_view(["POST"])
def apihome(request, *args, **kwargs):
    print(request.data)
    serial = movieserializer(data=request.data)
    if serial.is_valid(raise_exception=True):
        serial.save()
        print(serial.data)
    # instance = movie.objects.all().order_by("?").first()
    # data={}
    # if instance:
    #     data = movieserializer(instance).data
        return Response(serial.data)


# Create your views here.
@csrf_exempt
def alist(request):
    if request.method == "GET":
        art = article.objects.all()
        serial = articleserializer(art, many=True)
        return JsonResponse(serial.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serial = articleserializer(data=data)

        if serial.is_valid():
            serial.save()
            return JsonResponse(serial.data, status=201)
        return JsonResponse(serial.errors, status=400)


@csrf_exempt
def adetail(request, pk):
    try:
        art = article.objects.get(pk=pk)

    except article.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serial = articleserializer(art)
        return JsonResponse(serial.data, safe=False)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serial = articleserializer(art, data=data)
        if serial.is_valid():
            serial.save()
            return JsonResponse(serial.data)
        return JsonResponse(serial.errors, status=400)

    elif request.method == "DELETE":
        art.delete()
        return HttpResponse(status=204)



def home(request):
    return render(request,'Home.html',{})


