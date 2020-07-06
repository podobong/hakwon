from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from common.exceptions import EmptyValueError, UserTypeError
from common.validators import phone_validator
from academy.models import Academy


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, **info):
        # Required Fields
        fields = ('phone', 'password')
        for field in fields:
            if not info.get(field):
                raise EmptyValueError(field)
        # User Type Check
        if info['is_student'] and info['is_parent'] \
                or info['is_parent'] and info['is_teacher'] \
                or info['is_teacher'] and info['is_student']:
            raise UserTypeError('Each user can have only one user type.')
        # Save
        password = info['password']
        del info['password']
        user = self.model(**info)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password):
        user = self.create_user(
                phone=phone,
                password=password,
                is_student=False,
                is_parent=False,
                is_teacher=False,
                )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = '계정'
        verbose_name_plural = '계정'

    objects = UserManager()
    USERNAME_FIELD = 'phone'

    is_student = models.BooleanField(
            verbose_name='학생 계정',
            default=True,
            )
    is_parent = models.BooleanField(
            verbose_name='학부모 계정',
            default=False,
            )
    is_teacher = models.BooleanField(
            verbose_name='선생님 계정',
            default=False,
            )

    phone = models.CharField(
            verbose_name='전화번호',
            help_text='(- 없이 입력)',
            validators=[phone_validator],
            max_length=30,
            unique=True,
            )

    is_active = models.BooleanField(
            verbose_name='활성 계정',
            default=True,
            )
    is_admin = models.BooleanField(
            verbose_name='관리자 계정',
            default=False,
            )
    is_superuser = models.BooleanField(
            verbose_name='슈퍼유저 계정',
            default=False,
            )
    is_staff = models.BooleanField(
            verbose_name='스태프 계정',
            default=False,
            )
    date_joined = models.DateTimeField(
            verbose_name='가입일시',
            auto_now_add=True,
            )

    def __str__(self):
        return f'{self.phone}'


class Parent(models.Model):
    class Meta:
        verbose_name = '학부모 계정 정보'
        verbose_name_plural = '학부모 계정 정보'

    user = models.OneToOneField(
            verbose_name='계정',
            related_name='parent',
            to=User,
            on_delete=models.CASCADE,
            )

    name = models.CharField(
            verbose_name='이름',
            max_length=30,
            )
    image = models.ImageField(
            verbose_name='프로필 사진',
            blank=True,
            )

    def __str__(self):
        return f'{self.name}: {self.user.phone}'


class Student(models.Model):
    class Meta:
        verbose_name = '학생 계정 정보'
        verbose_name_plural = '학생 계정 정보'

    user = models.OneToOneField(
            verbose_name='계정',
            related_name='student',
            to=User,
            on_delete=models.CASCADE,
            )
    parent = models.ForeignKey(
            verbose_name='학부모',
            related_name='students',
            to=Parent,
            on_delete=models.SET_NULL,
            null=True,
            )

    name = models.CharField(
            verbose_name='이름',
            max_length=30,
            )
    image = models.ImageField(
            verbose_name='프로필 사진',
            blank=True,
            )

    def __str__(self):
        return f'{self.name}: {self.user.phone}'


class Teacher(models.Model):
    class Meta:
        verbose_name = '선생님 계정 정보'
        verbose_name_plural = '선생님 계정 정보'

    user = models.OneToOneField(
            verbose_name='계정',
            related_name='teacher',
            to=User,
            on_delete=models.CASCADE,
            )
    academy = models.ForeignKey(
            verbose_name='소속 학원',
            related_name='teachers',
            to=Academy,
            on_delete=models.SET_NULL,
            null=True,
            )
    is_owner = models.BooleanField(
            verbose_name='학원 관리자 계정',
            default=False,
            )

    name = models.CharField(
            verbose_name='이름',
            max_length=30,
            )
    image = models.ImageField(
            verbose_name='프로필 사진',
            blank=True,
            )

    def __str__(self):
        return f'{self.name}: {self.user.phone}'

