from django.db.models import Q
from django.contrib.auth import login, logout
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from common.exceptions import ModelDoesNotExistError
from common.permissions import IsSelfOrAdmin
from user.models import Parent, Student, Teacher
from user import serializers as srlzr
from user import docs


class StudentCreate(generics.CreateAPIView):
    serializer_class = srlzr.StudentCreateRetrieveSerializer
    permission_classes = (AllowAny,)

    @swagger_auto_schema(**docs.student_create_post)
    def post(self, request):
        '''
        # Create a User-Student Model Pair
        '''
        return super().post(request)


class ParentCreate(generics.CreateAPIView):
    serializer_class = srlzr.ParentCreateRetrieveSerializer
    permission_classes = (AllowAny,)

    @swagger_auto_schema(**docs.parent_create_post)
    def post(self, request):
        '''
        # Create a User-Parent Model Pair
        '''
        return super().post(request)


class TeacherCreate(generics.CreateAPIView):
    serializer_class = srlzr.TeacherCreateRetrieveSerializer
    permission_classes = (AllowAny,)

    @swagger_auto_schema(**docs.teacher_create_post)
    def post(self, request):
        '''
        # Create a User-Teacher Model Pair
        '''
        return super().post(request)


class StudentDetail(APIView):
    serializer_class = srlzr.StudentUpdateSerializer
    permission_classe = (IsSelfOrAdmin,)

    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise ModelDoesNotExistError('Student')

    @swagger_auto_schema(**docs.student_detail_get)
    def get(self, request, pk):
        '''
        # Retrieve a Specific User-Student Model Pair
        '''
        try:
            student = self.get_object(pk)
        except ModelDoesNotExistError as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        serializer = srlzr.StudentCreateRetrieveSerializer(parent)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(**docs.student_detail_put)
    def put(self, request, pk):
        '''
        # Update a Specific User-Student Model Pair
        '''
        try:
            student = self.get_object(pk)
        except ModelDoesNotExistError as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        serializer = srlzr.StudentUpdateSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(**docs.student_detail_delete)
    def delete(self, request, pk):
        '''
        # Destroy a Specific User-Student Model Pair
        '''
        try:
            student = self.get_object(pk)
        except ModelDoesNotExistError as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        student.delete()
        return Response({'success': 'Successfully deleted an object'}, status=status.HTTP_204_NO_CONTENT)


class ParentDetail(APIView):
    serializer_class = srlzr.ParentUpdateSerializer
    permission_classes = (IsSelfOrAdmin,)

    def get_object(self, pk):
        try:
            return Parent.objects.get(pk=pk)
        except Parent.DoesNotExist:
            raise ModelDoesNotExistError('Parent')

    @swagger_auto_schema(**docs.parent_detail_get)
    def get(self, request, pk):
        '''
        # Retrieve a Specific User-Parent Model Pair
        '''
        try:
            parent = self.get_object(pk)
        except ModelDoesNotExistError as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        serializer = srlzr.ParentCreateRetrieveSerializer(parent)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(**docs.parent_detail_put)
    def put(self, request, pk):
        '''
        # Update a Specific User-Parent Model Pair
        '''
        try:
            parent = self.get_object(pk)
        except ModelDoesNotExistError as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        serializer = srlzr.ParentUpdateSerializer(parent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(**docs.parent_detail_delete)
    def delete(self, request, pk):
        '''
        # Destroy a Specific User-Parent Model Pair
        '''
        try:
            parent = self.get_object(pk)
        except ModelDoesNotExistError as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        parent.delete()
        return Response({'success': 'Successfully deleted an object'}, status=status.HTTP_204_NO_CONTENT)


class TeacherDetail(APIView):
    pass


class UserLogin(APIView):
    serializer_class = srlzr.UserLoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = srlzr.UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            auth_serializer = srlzr.UserAuthSerializer(user)
            login(request, user)
            return Response(auth_serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogout(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        srlzr.delete_auth_token(request.user)
        logout(request)
        return Response({'success': 'Successfully logged out.'}, status=status.HTTP_200_OK)

