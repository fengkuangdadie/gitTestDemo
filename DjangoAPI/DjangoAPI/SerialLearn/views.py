from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import JSONParser

from SerialLearn.models import Book, Game
from SerialLearn.serializers import BookSerializer, GameSerializer


class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.all()

    serializer_class = BookSerializer


def get_book(request):

    if request.method == "GET":

        books = Book.objects.all()

        serializer = BookSerializer(instance=books, many=True)

        book_data = serializer.data

        print(book_data)

        print(type(book_data))

        data = {
            "msg": "ok",
            "status": 200,
            "data": book_data
        }

        return JsonResponse(data=data)
    elif request.method == "POST":

        content = JSONParser().parse(request)

        serializer = BookSerializer(data=content)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(data={"msg": "create_ok"})

        return JsonResponse(data={"msg": "create fail"})


def games(request):

    if request.method == "GET":

        game_list = Game.objects.all()

        serializer = GameSerializer(instance=game_list, many=True)

        data = {
            "msg": "ok",
            "status": 200,
            "data": serializer.data
        }

        return JsonResponse(data)

    elif request.method == "POST":

        game_info = JSONParser().parse(request)

        serializer = GameSerializer(data=game_info)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({"msg": "create ok"})
        return JsonResponse({"msg": "create fail"})

