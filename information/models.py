from django.db import models

# Create your models here.
class CourseNumber(models.Model):
	FIRST_COURSE = 1
	SECOND_COURSE = 2
	THIRD_COURSE = 3
	FOURTH_COURSE = 4
	COURSE_CHOICES = (
		(FIRST_COURSE, '1 курс'),
		(SECOND_COURSE, '2 курс'),
		(THIRD_COURSE, '3 курс'),
		(FOURTH_COURSE, '4 курс'),
	)
	number = models.IntegerField(choices=COURSE_CHOICES)
	def __str__(self):
		return self.get_number_display()	


class Speciality(models.Model):
	name = models.CharField(max_length=255, verbose_name='Скорочена назва')
	full_name = models.CharField(max_length=255, verbose_name='Повна назва')
	def __str__(self):
		return self.full_name

	class Meta:
		verbose_name = 'Спеціальність'
		verbose_name_plural = 'Спеціальності'

class Subject(models.Model):
	name = models.CharField(max_length=255, verbose_name='Назва')
	specialty = models.ForeignKey(Speciality, verbose_name="Спеціальність", related_name='subjects')
	year = models.ForeignKey(CourseNumber, verbose_name="Курс")
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)

	class Meta:
		verbose_name = 'Предмет'
		verbose_name_plural = 'Предмети'

	def __str__(self):
		return self.name

#PEP8
#для классов - CamelCase
#для переменных, методов, функция - method_name 

class PracticalWork(models.Model):
	PR = 1
	LR = 2
	DOC_TYPE_CHOICES=(
		(PR, 'Практична'),
		(LR, 'Лабораторна'),
	)
	kind = models.IntegerField(choices=DOC_TYPE_CHOICES, verbose_name='Тип')
	number = models.IntegerField(verbose_name='Номер')
	title = models.CharField(max_length=255, verbose_name='Тема')
	subject = models.ForeignKey(Subject, verbose_name="Предмет")
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)	

	def __str__(self):
		return self.name	


class PracticalWorkFile(models.Model):
	practical_work = models.ForeignKey(PracticalWork, verbose_name='Тема')
	document = models.FileField(upload_to='ads/', verbose_name='Файл')


class Lecture(models.Model):
	number = models.IntegerField(verbose_name='Номер')
	name = models.CharField(max_length=255, verbose_name='Тема')
	subject = models.ForeignKey(Subject, verbose_name="Предмет")
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)
	

	def __str__(self):
		return self.name

class LecturePart(models.Model):
	class Meta:
		abstract = True	
	document = models.FileField(upload_to='insdfs/', verbose_name='Файл')
	lecture = models.OneToOneField(Lecture, verbose_name="Лекція")	


class Theory(LecturePart):
	title = models.TextField(verbose_name='Тема')

class Presentation(LecturePart):
	title = models.TextField(verbose_name='Тема')

class Video(LecturePart):
	title = models.TextField(verbose_name='Тема')


class CheckTest(models.Model):
	title = models.CharField(max_length=255, verbose_name='Тест')
	doc_name = models.CharField(max_length=30, blank=True, verbose_name='Файл')
	subject = models.ForeignKey(Subject, verbose_name='Предмет')
