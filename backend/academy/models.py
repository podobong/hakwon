from django.db import models
from multiselectfield import MultiSelectField

from common.exceptions import UserTypeError
from common.validators import phone_validator, zip_validator
from academy.choices import SUBJECTS, TARGET_AGES, SCORES


class Academy(models.Model):
    class Meta:
        verbose_name = '학원'
        verbose_name_plural = '학원'

    phone = models.CharField(
            verbose_name='대표전화',
            help_text='(- 없이 입력)',
            max_length=30,
            validators=[phone_validator],
            unique=True,
            )

    name = models.CharField(
            verbose_name='학원명',
            max_length=255,
            )
    image = models.ImageField(
            verbose_name='프로필 사진',
            blank=True,
            )

    address_zip = models.CharField(
            verbose_name='우편번호',
            max_length=10,
            validators=[zip_validator],
            )
    address_state = models.CharField(
            verbose_name='광역시/도',
            max_length=30,
            )
    address_city = models.CharField(
            verbose_name='시/군/구',
            max_length=30,
            )
    address_district = models.CharField(
            verbose_name='읍/면/동',
            max_length=30,
            )
    address_street = models.CharField(
            verbose_name='도로명',
            max_length=30,
            )
    address_building = models.IntegerField(
            verbose_name='건물 번호',
            )
    address_detail = models.CharField(
            verbose_name='상세 주소',
            max_length=255,
            )

    subjects = MultiSelectField(
            verbose_name='과목',
            max_length=20,
            choices=SUBJECTS,
            )
    target_ages = MultiSelectField(
            verbose_name='대상층',
            max_length=20,
            choices=TARGET_AGES,
            )
    description = models.TextField(
            verbose_name='학원 소개',
            blank=True,
            )

    def __str__(self):
        return f'{self.name}: {self.phone}'


class StudentInAcademy(models.Model):
    class Meta:
        verbose_name = '학원당 학생 계정 정보'
        verbose_name_plural = '학원당 학생 계정 정보'
        unique_together = ('academy', 'student_number')

    student = models.ForeignKey(
            verbose_name='학생 계정 정보',
            related_name='students_in_academy',
            to='user.Student',
            on_delete=models.CASCADE,
            null=True,
            )
    academy = models.ForeignKey(
            verbose_name='학원',
            related_name='students_in_academy',
            to=Academy,
            on_delete=models.CASCADE,
            )
    student_number = models.CharField(
            verbose_name='학생 고유번호',
            max_length=30,
            )

    def __str__(self):
        return f'{self.academy.name}: {self.student.name}({self.student_number})'


class Review(models.Model):
    class Meta:
        verbose_name = '학원 리뷰'
        verbose_name_plural = '학원 리뷰'

    academy = models.ForeignKey(
            verbose_name='대상 학원',
            related_name='reviews',
            to=Academy,
            on_delete=models.CASCADE,
            )
    author = models.ForeignKey(
            verbose_name='작성자',
            related_name='reviews',
            to='user.User',
            on_delete=models.SET_NULL,
            null=True,
            )

    score = models.IntegerField(
            verbose_name='별점',
            choices=SCORES,
            )
    text = models.TextField(
            verbose_name='내용',
            )

    def __str__(self):
        return f'{self.academy.name} 리뷰: {self.text}'

