from rest_framework import authentication, generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from django.http import Http404
from django.shortcuts import get_object_or_404

from .permissions import IsStaffEditorPermission
from .models import Product
from .serializers import ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [IsStaffEditorPermission]

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)

product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_detail_view = ProductDetailAPIView.as_view()


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

product_update_view = ProductUpdateAPIView.as_view()

class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destory(self, instance):
        super().perform_destory(instance)
            
product_destroy_view = ProductDestroyAPIView.as_view()


# @api_view(['GET', 'POST'])
# def product_alt_view(request, *args, **kwargs):
#    method = request.method

#    if method == 'GET':
#         pass
#    if method == 'POST':
#         serializers = ProductSerializer(data=request.data)
#         if serializers.is_valid(raise_exception=True):
#             print(serializers.data)
#             # data = serializers.data
#             return Response(serializers.data)
#         return Response({"invalid": "not good data"}, status=400)
