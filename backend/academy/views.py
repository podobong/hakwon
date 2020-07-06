from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

from common.exceptions import ModelDoesNotExistError
from common.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly, IsAcademyStaff, IsNotAcademyStaffOrReadOnly
from academy.models import Academy
from academy import serializers as srlzr


class AcademyList(generics.ListCreateAPIView):
    queryset = Academy.objects.all()
    serializer_class = srlzr.AcademySerializer
    permission_classes = (IsAdminOrReadOnly,)


class AcademyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Academy.objects.all()
    serializer_class = srlzr.AcademySerializer
    permission_classes = (IsOwnerOrReadOnly,)


class AcademyStudents(APIView):
    serializer_class = srlzr.StudentInAcademySerializer
    permission_classes = (IsAcademyStaff,)

    def get_object(self, pk):
        try:
            academy = Academy.objects.get(pk=pk)
            self.check_object_permissions(self.request, academy)
            return academy
        except Academy.DoesNotExist:
            raise ModelDoesNotExistError('Academy')

    def get(self, request, pk):
        try:
            academy = self.get_object(pk)
        except ModelDoesNotExistError as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        serializer = srlzr.AcademyStudentsSerializer(academy)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        try:
            academy = self.get_object(pk)
        except ModelDoesNotExistError as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        serializer = srlzr.StudentInAcademySerializer(
                data=request.data,
                context={'academy': academy},
                )
        if serializer.is_valid():
            try:
                serializer.save()
            except ModelDoesNotExistError as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AcademyReview(APIView):
    serializer_class = srlzr.ReviewSerializer
    permission_classes = (IsNotAcademyStaffOrReadOnly,)

    def get_object(self, pk):
        try:
            return Academy.objects.get(pk=pk)
        except Academy.DoesNotExist:
            raise ModelDoesNotExistError('Academy')

    def get(self, request, pk):
        try:
            academy = self.get_object(pk)
        except ModelDoesNotExistError as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        serializer = srlzr.AcademyReviewsSerializer(academy)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        try:
            academy = self.get_object(pk)
        except ModelDoesNotExistError as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        serializer = srlzr.ReviewSerializer(
                data=request.data,
                context={'request': request, 'academy': academy},
                )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

