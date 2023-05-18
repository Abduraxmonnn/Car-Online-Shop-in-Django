# Rest-Framework
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

# Project
from apps.transmission.models import Transmission
from apps.transmission.serializers import TransmissionBaseSerializer


class TransmissionCreateAPIView(generics.CreateAPIView):
    queryset = Transmission.objects.all()
    serializer_class = TransmissionBaseSerializer
    permission_classes = [IsAdminUser]
    http_method_names = ['post']


class TransmissionUpdateAPIView(generics.UpdateAPIView):
    queryset = Transmission.objects.all()
    serializer_class = TransmissionBaseSerializer
    permission_classes = [IsAdminUser]
    http_method_names = ['put']

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Transmission updated successfully"
            })

        else:
            return Response({
                "message": "Failed",
                "details": serializer.errors
            })


class TransmissionDestroyAPIView(generics.DestroyAPIView):
    queryset = Transmission.objects.all()
    serializer_class = TransmissionBaseSerializer
    permission_classes = [IsAdminUser]
    http_method_names = ['delete']

    def delete(self, request, pk=None, *args, **kwargs):
        get_transmission = Transmission.objects.get(pk=pk)
        get_transmission.delete()
        return Response({
            "Transmission deleted"
        }, status=status.HTTP_204_NO_CONTENT)


class TransmissionListAPIVIew(generics.ListAPIView):
    queryset = Transmission.objects.all()
    serializer_class = TransmissionBaseSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get']
    lookup_field = ['type']


class TransmissionRetrieveAPIVIew(generics.RetrieveAPIView):
    queryset = Transmission.objects.all()
    serializer_class = TransmissionBaseSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get']
