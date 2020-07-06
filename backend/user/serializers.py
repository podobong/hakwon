from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers as srlzr
from rest_framework.authtoken.models import Token

from common.exceptions import PasswordCheckError, ModelDoesNotExistError
from common.validators import phone_validator
from user.models import Student, Parent, Teacher
from academy.models import Academy


def delete_auth_token(user):
    if Token.objects.filter(user=user):
        Token.objects.get(user=user).delete()


class UserCreateRetrieveSerializer(srlzr.ModelSerializer):
    password = srlzr.CharField(
            label='비밀번호',
            max_length=255,
            required=True,
            write_only=True,
            style={'input_type': 'password', 'placeholder': 'Password'}
            )
    password_check = srlzr.CharField(
            label='비밀번호 확인',
            max_length=255,
            required=True,
            write_only=True,
            style={'input_type': 'password', 'placeholder': 'Password'}
            )

    class Meta:
        model = get_user_model()
        fields = ('phone', 'password', 'password_check')

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class UserLoginSerializer(srlzr.Serializer):
    phone = srlzr.CharField(
            label='전화번호',
            help_text='(- 없이 입력)',
            max_length=30,
            required=True,
            )
    password = srlzr.CharField(
            label='비밀번호',
            max_length=255,
            required=True,
            write_only=True,
            style={'input_type': 'password', 'placeholder': 'Password'}
            )

    def validate(self, data):
        user = authenticate(**data)
        if not user:
            raise srlzr.ValidationError()
        return user

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class UserAuthSerializer(srlzr.ModelSerializer):
    auth_token = srlzr.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ('phone', 'auth_token')

    def get_auth_token(self, user):
        if Token.objects.filter(user=user):
            delete_auth_token(user)
        token = Token.objects.create(user=user)
        return token.key


class StudentCreateRetrieveSerializer(srlzr.ModelSerializer):
    user = UserCreateRetrieveSerializer()
    parent_phone = srlzr.CharField(
            label='학부모 전화번호',
            help_text='(- 없이 입력)',
            validators=[phone_validator],
            max_length=30,
            required=False,
            write_only=True,
            )

    class Meta:
        model = Student
        fields = ('user', 'name', 'image', 'parent_phone')

    def create(self, validated_data):
        if validated_data.get('user').get('password_check') != validated_data.get('user').get('password'):
            raise PasswordCheckError()
        user = get_user_model().objects.create_user(
                phone=validated_data.get('user').get('phone'),
                password=validated_data.get('user').get('password'),
                is_student=True,
                is_parent=False,
                is_teacher=False,
                )
        try:
            parent = get_user_model().objects.get(
                    phone=validated_data.get('parent_phone')
                    ).parent
        except get_user_model().DoesNotExist:
            parent = None
        student = Student(
                user=user,
                parent=parent,
                name=validated_data.get('name'),
                image=validated_data.get('image'),
                )
        student.save()
        return student

    def update(self, instance, validated_data):
        instance.user.phone = validated_data.get('user').get('phone', instance.user.phone)
        instance.user.password = validated_data.get('user').get('password', instance.user.password)
        instance.parent = validated_data.get('parent', instance.parent)
        instance.name = validated_data.get('name', instance.name)
        instance.image = validated_data.get('image', instance.image)
        return instance


class StudentUpdateSerializer(srlzr.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'image')

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.image = validated_data.get('image', instance.image)
        return instance


class ParentCreateRetrieveSerializer(srlzr.ModelSerializer):
    user = UserCreateRetrieveSerializer()
    students = StudentCreateRetrieveSerializer(many=True)

    class Meta:
        model = Parent
        fields = ('user', 'name', 'image', 'students')

    def create(self, validated_data):
        if validated_data.get('user').get('password_check') != validated_data.get('user').get('password'):
            raise PasswordCheckError()
        user = get_user_model().objects.create_user(
                phone=validated_data.get('user').get('phone'),
                password=validated_data.get('user').get('password'),
                is_student=False,
                is_parent=True,
                is_teacher=False,
                )
        parent = Parent(
                user=user,
                name=validated_data.get('name'),
                image=validated_data.get('image'),
                )
        parent.save()
        return parent


class ParentUpdateSerializer(srlzr.ModelSerializer):
    class Meta:
        model = Parent
        fields = ('name', 'image')

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.image = validated_data.get('image', instance.image)
        return instance


class TeacherCreateRetrieveSerializer(srlzr.ModelSerializer):
    user = UserCreateRetrieveSerializer()
    academy_phone = srlzr.CharField(
            label='학원 전화번호',
            help_text='(- 없이 입력)',
            validators=[phone_validator],
            max_length=30,
            write_only=True,
            )

    class Meta:
        model = Teacher
        fields = ('user', 'academy_phone', 'name', 'image')

    def create(self, validated_data):
        if validated_data.get('user').get('password_check') != validated_data.get('user').get('password'):
            raise PasswordCheckError()
        user = get_user_model().objects.create_user(
                phone=validated_data.get('user').get('phone'),
                password=validated_data.get('user').get('password'),
                is_student=False,
                is_parent=False,
                is_teacher=True,
                )
        try:
            academy = Academy.objects.get(phone=validated_data.get('academy_phone'))
        except Academy.DoesNotExist:
            raise ModelDoesNotExistError('Academy')
        teacher = Teacher(
                user=user,
                academy=academy,
                name=validated_data.get('name'),
                image=validated_data.get('image'),
                )
        teacher.save()
        return teacher

    def update(self, instance, validated_data):
        instance.user.phone = validated_data.get('user').get('phone', instance.user.phone)
        instance.user.password = validated_data.get('user').get('password', instance.user.password)
        instance.academy = validated_data.get('academy', instance.academy)
        instance.name = validated_data.get('name', instance.name)
        instance.image = validated_data.get('image', instance.image)
        return instance


class TeacherUpdateSerializer(srlzr.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('name', 'image')

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.image = validated_data.get('image', instance.image)
        return instance


class StudentInfoSerializer(srlzr.ModelSerializer):
    user = UserCreateRetrieveSerializer()
    parent = ParentCreateRetrieveSerializer()

    class Meta:
        model = Student
        fields = ('user', 'parent', 'name', 'image')


class ParentReviewSerializer(srlzr.ModelSerializer):
    class Meta:
        model = Parent
        fields = ('name', 'image')


class StudentReviewSerializer(srlzr.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'image')


class UserReviewSerializer(srlzr.ModelSerializer):
    parent = ParentReviewSerializer()
    student = StudentReviewSerializer()

    class Meta:
        model = get_user_model()
        fields = ('phone', 'parent', 'student')

