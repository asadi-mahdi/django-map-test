from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.exceptions import ParseError
from rest_framework.response import Response

from .models import Member


def members(request):
    return HttpResponse("Hello world!")


@api_view(['GET'])
def rest_response(request):
    response = {'name': 'mahdi'}
    return Response(response)


@api_view(['POST'])
def create(request):
    try:
        member = Member(firstname=request.data.get("firstname"), lastname=request.data.get("lastname"))
        member.save()
        return Response(member.id)
    except Exception as e:
        raise ParseError(detail=e)


@api_view(['GET'])
def find_member(request, id):
    try:
        return Response(Member.objects.filter(id=id).values()[0])
    except Exception as e:
        raise ParseError(detail=e)


@api_view(['GET'])
def find_all(request):
    result = []
    for member in Member.objects.all():
        result.append({"id": member.id,
                       "firstname": member.firstname,
                       "lastname": member.lastname,
                       "joinedDate": member.joined_date,
                       "phone": member.phone})
    return Response(result)


@api_view(['PUT'])
def update(request):
    try:
        member = Member.objects.get(id=request.data.get("id"))
        member.firstname = request.data.get("firstname")
        member.lastname = request.data.get("lastname")
        member.save()
        return Response(member.id)
    except Exception as e:
        raise ParseError(detail=e)


@api_view(['DELETE'])
def delete(request, id):
    try:
        member = Member.objects.get(id=id)
        member.delete()
        return Response("successful")
    except Exception as e:
        raise ParseError(detail=e)
