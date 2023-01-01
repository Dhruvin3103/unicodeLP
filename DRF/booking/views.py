from django.http import Http404
from django.shortcuts import render

from rest_framework import mixins, generics, authentication, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import userpermission
from .models import *
from .serializers import *



class bookingmixin(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = booking.objects.all()
    serializer_class = bookingserialzer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [userpermission]
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


booking_m = bookingmixin.as_view()

class update_booking(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [userpermission]

    def get_object(self, pk):
        try:
            return booking.objects.get(pk=pk)
        except booking.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = bookingserialzer(snippet, data=request.data)
        data = request.data
        t = data['b_no_of_tickets']
        id = data['movie_no']
        m = movie.objects.filter(id=id).values()
        d = booking.objects.filter(movie_no=id)
        d1 = booking.objects.filter(id=pk).values()
        p = m[0]['movie_ticket_price'] * t
        data['booking_price'] = p
        c = 0
        for i in d.values(): c = c + i['b_no_of_tickets']
        print(m[0]['no_of_seats'])
        print(c)
        print(d1[0]['b_no_of_tickets'])

        if ((m[0]['no_of_seats'] - (c-d1[0]['b_no_of_tickets'])) >= data['b_no_of_tickets']):
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        else:
            return Response({
                'status':400,
                'message':'an error occured'
            })

update_b = update_booking.as_view()

class create_booking(APIView):
    queryset = booking.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [userpermission]

    def get(self,request):

        print(request.user)

        data = booking.objects.all()
        d = [i for i in booking.objects.all().values()]
        serializer = bookingserialzer(data,many=True)
        return Response({
            'status':200,
            'data': serializer.data
        })
    def post(self,request):
        print(request.user)
        try:
            data = request.data
            t=data['b_no_of_tickets']
            id=data['movie_no']
            m= movie.objects.filter(id=id).values()
            d = booking.objects.filter(movie_no=id)
            p=m[0]['movie_ticket_price']*t
            data['booking_price']=p
            c = 0
            for i in d.values(): c = c+i['b_no_of_tickets']
            if((m[0]['no_of_seats']-c)>=data['b_no_of_tickets']):
                serializer = bookingserialzer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(
                        {
                            'status':200,
                            'message':'booking completed you can proceed for payment',
                            'data':serializer.data,
                        }
                    )
                else:
                    return Response({
                        'status':400,
                        'message':'error occured',
                        'data':serializer.errors,
                    })
            else:
                return Response({
                    'status':400,
                    'message':'Housefull sry :(',
                })
        except Exception as e:
            print(e)

create_b = create_booking.as_view()
