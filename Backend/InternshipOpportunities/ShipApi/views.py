from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import InternShip
from .serializers import InternShipSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


@api_view(["GET", "POST"])
def internship_list(request):
    if request.method == "GET":
        internships = InternShip.objects.all()
        serializer = InternShipSerializer(internships, many=True)
        return Response(serializer.data)

    elif request.method == "POST":

        serializer = InternShipSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def internship_detail(request, pk):
    try:
        intern = InternShip.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = InternShipSerializer(intern)
        return JsonResponse(serializer.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = InternShipSerializer(intern, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        intern.delete()
        return HttpResponse(status=204)