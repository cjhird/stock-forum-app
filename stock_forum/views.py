from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

from comments.serializers.populated import PopulatedCommentSerializer

# custom imports
from .models import Thread
from .serializers.common import ThreadSerializer
from .serializers.populated import PopulatedThreadSerializer

# import permissions 
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# -----------------

# Create your views here.
class ThreadListView(APIView):

  permission_classes = (IsAuthenticatedOrReadOnly, )

  # GET - Get all threads
  def get(self, _request):
    threads = Thread.objects.all()
    serialized_threads = ThreadSerializer(threads, many=True)
    return Response(serialized_threads.data, status=status.HTTP_200_OK)

  # POST - Add a thread
  def post(self, request):
    deserialized_thread = ThreadSerializer(data=request.data)
    print('deserialized request --->', request.data)
    try:
      deserialized_thread.is_valid()
      deserialized_thread.save()
      return Response(deserialized_thread.data, status.HTTP_201_CREATED)
    
    except Exception as e:
      print(e)
      return Response({ 'detail': str(e) }, status.HTTP_422_UNPROCESSABLE_ENTITY)


class ThreadDetailView(APIView):

  permission_classes = (IsAuthenticatedOrReadOnly, )

  # Find a specific thread
  def get_thread(self, pk):
    try:
      return Thread.objects.get(pk=pk)
    except Thread.DoesNotExist as e:
        print(e)
        raise NotFound({ 'detail': str(e) })

  # GET - Return a single specific thread
  def get(self, _request, pk):
    thread = self.get_thread(pk)
    serialized_thread = PopulatedThreadSerializer(thread)
    return Response(serialized_thread.data, status.HTTP_200_OK)

  # DELETE - Delete a single specific thread
  def delete(self, _request, pk):
    thread_to_delete = self.get_thread(pk)
    thread_to_delete.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

  # PUT - Update a single specific thread
  def put(self, request, pk):
    thread_to_update = self.get_thread(pk=pk)
    print(type(thread_to_update))
    deserialized_thread = ThreadSerializer(thread_to_update, request.data)
    try:
        deserialized_thread.is_valid()
        deserialized_thread.save()
        return Response(deserialized_thread.data, status.HTTP_202_ACCEPTED)
    except Exception as e:
        print(e)
        return Response({ 'detail': str(e) }, status.HTTP_422_UNPROCESSABLE_ENTITY)