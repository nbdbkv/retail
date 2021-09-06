from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from stores.models import Store
from stores.serializers import (
    StoreListSerializer, StoreDetailSerializer, ProductBuySerializer,
    ProductAddSerializer,
)


class StoreListView(ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreListSerializer


class StoreDetailView(RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreDetailSerializer


@api_view(['POST'])
def buy(request, **kwargs):
    """Buy a product and decrease from products in store."""
    context = {'store_pk': kwargs['pk']}
    serializer = ProductBuySerializer(
        data=request.data, many=True, context=context
    )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add(request, **kwargs):
    """Add a product to products in store."""
    context = {'store_pk': kwargs['pk']}
    serializer = ProductAddSerializer(
        data=request.data, many=True, context=context
    )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
