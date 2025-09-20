from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from product.models import Product, Category,Review,ProductImage
from product.serializer import ProductSerializer, CategorySerializer,ReviewSerializers,ProductImageSerializer 
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from product.filters import ProductFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from product.paginations import DeafultPaginations
from api.permissions import IsAdminOrReadOnly,FullDjangoModelPermission
from rest_framework.permissions import DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from product.permissions import IsReviewAuthorOrReadOnly
from drf_yasg.utils import swagger_auto_schema


class ProductImageViewSet(ModelViewSet):

    serializer_class = ProductImageSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return ProductImage.objects.filter(product_id = self.kwargs.get('product_pk'))
    
    def perform_create(self, serializer):
        serializer.save(product_id=self.kwargs.get('product_pk'))



class ProductViewSet(ModelViewSet):

    """
    API endpoint for managing products in the e-commerce store
        - Allows authenticated admin to create , update and delete product
        - Allows user to browse and filter product
        - Support searching by name, Description
    

    """
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter,OrderingFilter]
    # filterset_fields = ['category_id','price']
    filterset_class = ProductFilter
    pagination_class = DeafultPaginations
    search_fields = ['name', 'description']
    ordering_fields = ['price','updated_at']
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return Product.objects.prefetch_related('images').all()

    def list(self, request, *args, **kwargs):
        """Retrive all the product """
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
            operation_summary="Create A Product By Admin",
            operation_description="This allow an admin to create a product",
            request_body= ProductSerializer,
            responses={
                201: ProductSerializer,
                400 : "Bad Request"
            }
    )
    def create(self, request, *args, **kwargs):
        """Only Authenticated admin can create product"""
        return super().create(request, *args, **kwargs)
    
    # permission_classes =[DjangoModelPermissionsOrAnonReadOnly]
    # permission_classes = [DjangoModelPermissions]
    # permission_classes = [FullDjangoModelPermission]
    # permission_classes = [IsAdminUser]

    # def get_permissions(self):
    #     if self.request.method=='GET':
    #         return [AllowAny()]
    #     return [IsAdminUser()]


   
    
class CategoryViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]

    queryset = Category.objects.annotate(product_count=Count('products')).all()
    serializer_class = CategorySerializer
    

class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializers
    permission_classes = [IsReviewAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    
    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs.get('product_pk'))
    def get_serializer_context(self):
        return {'product_id' : self.kwargs.get('product_pk')}


""" 
    Destory Method Override
    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        if product.stock > 10 :
            return Response({'message': "Product with stock more than 10 could not be delted"})
        self.perform_destroy(product)
        return Response(status=status.HTTP_204_NO_CONTENT)
"""