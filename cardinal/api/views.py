from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

CARDINAL_EMOJI = "🐦"

class InitialApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """Return a cardinal"""
        return Response(CARDINAL_EMOJI, status=status.HTTP_200_OK)


class DataRequestApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):

        # TODO: pull from database
        data = "foobar"

        return Response(data, status=status.HTTP_200_OK)


class TestDataGeneratorApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response("jake", status=status.HTTP_200_OK)
