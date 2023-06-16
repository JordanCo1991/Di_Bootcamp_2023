from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ReportSerializer
from .models import Report

from rest_framework import generics
from rest_framework import  mixins

# Create your views here.


class ReportView(APIView):

    def get(self, request, *args, **kwargs): 
        if 'pk' in kwargs:
            report = Report.objects.get(id=kwargs['pk'])
            serializer = ReportSerializer(post)
            return Response(serializer.data)
        else:
            queryset = Report.objects.all()
            serializer = ReportSerializer(queryset, many = True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ReportSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk, *args, **kwargs):
        report = Report.objects.get(id=pk)
        report.delete()
        return Reponse()

    
# put=update
    def put(self, request, pk, *args, **kwargs):
        report = Report.objects.get(id=pk)
        serializer = ReportSerializer(report, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



class ReportListView(mixins.ListModelMixin,
mixins.CreateModelMixin,
 generics.GenericAPIView):

    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class ReportDetailView(generics.RetrieveAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class ReportDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsForecaster)