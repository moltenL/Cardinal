from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .generate_test_data import DataGenerator
from django.http import HttpResponse

CARDINAL_EMOJI = "🐦"


def api_docs(_):
    page = """<div>
    <h1>Cardinal 🐦</h1>
    <h4>API</h4>

    <ul>
        <li>/api/hello</li>
        <li>/api/all</li>
        <li>/api/generate/&lt;str:data_structure_type&gt;</li>
        <li>/api/generate/&lt;str:data_structure_type&gt;/?count=int</li>
    </ul>
    </div>"""
    return HttpResponse(page)

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

        filename = kwargs["data_structure_type"] + ".yml"
        generate_test_data = DataGenerator(filename)

        # If the "count" is specified, give that number to the data generator
        # Example "api/generate/calc_tba_team_schema/?format=json&count=10"
        if "count" in request.query_params:
            count = int(request.query_params["count"])
        else:
            count = 1

        return Response(generate_test_data.get_data(count), status=status.HTTP_200_OK)
