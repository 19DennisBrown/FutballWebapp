from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import teamSerializer
from .models import Team

# Create your views here.

 
@api_view(['GET', 'POST'])
def teams(request):
  if request.method == 'GET':
    teams = Team.objects.all()
    serialized = teamSerializer(teams, many=True)
    return Response(serialized.data, status=status.HTTP_200_OK)
  
  if request.method == 'POST':
    serialized = teamSerializer(data=request.data)
    if serialized.is_valid():
      serialized.save()
      return Response(status=status.HTTP_201_CREATED)
    return Response(serialized.data)

@api_view(['GET', 'PUT', 'DELETE'])
def team(request, id):
  try:
    team = Team.objects.get(id=id)
  except team.notFound:
    return Response(status=status.HTTP_204_NO_CONTENT)
    
  if request.method == 'GET':
    serialized = teamSerializer(team)
    return Response(serialized.data, status=status.HTTP_200_OK)
  
  if request.method == 'PUT':
    serialized = teamSerializer(data=request.data, instance=team)
    if serialized.is_valid():
      serialized.save()
      return Response(status=status.HTTP_201_CREATED)
    return Response(serialized.data)
  
  if request.method == 'DELETE':
    team.delete()
    return Response(status=status.HTTP_200_OK)