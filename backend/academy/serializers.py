from django.db.models import Q
from rest_framework import serializers as srlzr

from common.exceptions import UserTypeError, ModelDoesNotExistError
from common.validators import phone_validator
from user.models import Student
from user.serializers import UserReviewSerializer, StudentInfoSerializer
from academy.models import Academy, StudentInAcademy, Review


class ReviewSerializer(srlzr.ModelSerializer):
    author = UserReviewSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('author', 'score', 'text')

    def create(self, validated_data):
        review = Review(
                academy=self.context.get('academy'),
                author=self.context.get('request').user,
                score=validated_data.get('score'),
                text=validated_data.get('text'),
                )
        review.save()
        return review


class AcademySerializer(srlzr.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Academy
        fields = (
                'phone', 'name', 'image',
                'address_zip', 'address_state', 'address_city', 'address_district',
                'address_street', 'address_building', 'address_detail',
                'subjects', 'target_ages', 'description', 'reviews',
                )


class StudentInAcademySerializer(srlzr.ModelSerializer):
    student = StudentInfoSerializer(read_only=True)
    student_phone = srlzr.CharField(
            label='학생 전화번호',
            help_text='(- 없이 입력)',
            validators=[phone_validator],
            max_length=30,
            required=True,
            write_only=True,
            )
    student_number = srlzr.CharField(
            label='학생 고유번호',
            max_length=30,
            required=True,
            )

    class Meta:
        model = StudentInAcademy
        fields = ('student', 'student_phone', 'student_number')

    def create(self, validated_data):
        try:
            student = Student.objects.get(Q(user__phone=validated_data.get('student_phone')))
        except Student.DoesNotExist:
            raise ModelDoesNotExistError('Student')
        sia = StudentInAcademy(
                student=student,
                academy=self.context.get('academy'),
                student_number=validated_data.get('student_number'),
                )
        sia.save()
        return sia

    def update(self, validated_data):
        pass


class AcademyStudentsSerializer(srlzr.ModelSerializer):
    students_in_academy = StudentInAcademySerializer(many=True)

    class Meta:
        model = Academy
        fields = ('phone', 'name', 'image', 'students_in_academy',)


class AcademyReviewsSerializer(srlzr.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Academy
        fields = ('phone', 'name', 'image', 'reviews')

