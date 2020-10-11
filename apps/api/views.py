from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import views
from rest_framework.exceptions import (
    ValidationError, PermissionDenied
)
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from apps.api.models import Record, Artist, Collection
from apps.api.serializers import RecordSerializer, ArtistSerializer, CollectionSerializer

#
# class CategoryViewSet(viewsets.ModelViewSet):
#     # this means, the user must be logged into the system
#     # to create a category
#     permission_classes = (IsAuthenticated,)
#     # assign the serializer that is responsible for the data conversion
#     serializer_class = CategorySerializer
#
#     def get_queryset(self):
#         # SELECT * FROM
#         queryset = Category.objects.all().filter(owner=self.request.user)
#         return queryset
#
#     def create(self, request, *args, **kwargs):
#         print(self)
#         print(type(super()))
#         # check if the category already exists for the current logged in user
#         category = Category.objects.filter(
#             name=request.data.get('name'),
#             owner=request.user
#         )
#         if category:
#             msg = 'Category with that name already exists'
#             raise ValidationError(msg)
#         return super().create(request)
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#     def destroy(self, request, *args, **kwargs):
#         print(request)
#         print(args)
#         print(kwargs)
#         category = Category.objects.get(pk=self.kwargs["pk"])
#         if not request.user == category.owner:
#             raise PermissionDenied("You cannot delete this category")
#         return super().destroy(request, *args, **kwargs)
#
# class CategoryRecipes(generics.ListCreateAPIView):
#     permission_classes = (IsAuthenticated,)
#
#     def get_queryset(self):
#         if self.kwargs.get("category_pk"):
#             category = Category.objects.get(pk=self.kwargs["category_pk"])
#             queryset = Recipe.objects.filter(
#                 owner=self.request.user,
#                 category=category
#             )
#
#         serializer_class = RecipeSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
# class SingleCategoryRecipe(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = RecipeSerializer
#
#     def get_queryset(self):
#         if self.kwargs.get("category_pk") and self.kwargs.get("pk"):
#             category = Category.objects.get(pk=self.kwargs["category_pk"])
#             queryset = Recipe.objects.filter(
#                 pk=self.kwargs["pk"],
#                 owner=self.request.user,
#                 category=category
#             )
#             return queryset


class ArtistViewset(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = ArtistSerializer

    def get_queryset(self):
        queryset = Artist.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):

        if request.user.is_anonymous:
            raise PermissionDenied(
                "Only logged in users may create records."
            )
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        record = Artist.objects.get(pk=self.kwargs["pk"])
        if not request.user.is_staff:
            raise PermissionDenied(
                "You do not have permission to delete this record."
            )
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        record = Artist.objects.get(pk=self.kwargs["pk"])
        if not request.user.is_staff:
            raise PermissionDenied(
                "You do not have permission to edit this record."
            )
        return super().update(request, *args, **kwargs)

class RecordViewset(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = RecordSerializer

    def get_queryset(self):
        queryset = Record.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):

        if request.user.is_anonymous:
            raise PermissionDenied(
                "Only logged in users may create records."
            )
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        record = Record.objects.get(pk=self.kwargs["pk"])
        if not request.user.is_staff:
            raise PermissionDenied(
                "You do not have permission to delete this record."
            )
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        record = Record.objects.get(pk=self.kwargs["pk"])
        if not request.user.is_staff:
            raise PermissionDenied(
                "You do not have permission to edit this record."
            )
        return super().update(request, *args, **kwargs)

class CollectionViewset(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = CollectionSerializer

    def get_queryset(self):
        queryset = Collection.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):

        if request.user.is_anonymous:
            raise PermissionDenied(
                "Only logged in users may create records."
            )
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        record = Collection.objects.get(pk=self.kwargs["pk"])
        if not request.user.is_staff:
            raise PermissionDenied(
                "You do not have permission to delete this record."
            )
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        record = Collection.objects.get(pk=self.kwargs["pk"])
        if not request.user.is_staff:
            raise PermissionDenied(
                "You do not have permission to edit this record."
            )
        return super().update(request, *args, **kwargs)


class BlankView(generics.GenericAPIView):

    def __init__(self, request, *args, **kwargs):
        print(args)
        print(dict(request))
        newnew = dict(kwargs)
        for kwarg in newnew.items():
            print(kwarg)

    @action(detail=True, methods=['get'])
    def get(self, *args, **kwargs):
        print(args)
        print(kwargs)
        response = Response('[{"one":"it"}]')
        print(response)
        return response
    
class CollectionDetail(views.APIView):

    permission_classes = (AllowAny, IsAuthenticated)
    serializer_class = CollectionSerializer

    def get_object(self, pk):
        print(self.kwargs)
        collection = Collection.objects.get(pk=pk)
        return collection

    def create(self, request, *args, **kwargs):
        collection = Collection.objects.get(pk=self.kwargs['pk'])
        print(collection)

    def get(self, request, pk, *args, **kwargs):
        collection = self.get_object(pk)
        serializer = CollectionSerializer(collection)
        print(collection)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        collection = self.get_object(pk)
        print(request.data)
        # collection.records = request.data.records
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



