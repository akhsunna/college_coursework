from django.db import models
from django.contrib.auth.models import User

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
	author = models.ForeignKey(User, null=True, blank=True)

	class Meta:
		verbose_name = 'Предмет'
		verbose_name_plural = 'Предмети'

	def __str__(self):
		return self.name

class PracticalWork(models.Model):
	PR = 'PR'
	LR = 'LR'
	DOC_TYPE_CHOICES=(
		(PR, 'Практична'),
		(LR, 'Лабораторна'),
	)
	kind = models.CharField(choices=DOC_TYPE_CHOICES, max_length=255, verbose_name='Тип')
	number = models.IntegerField(verbose_name='Номер')
	title = models.CharField(max_length=255, verbose_name='Тема')
	subject = models.ForeignKey(Subject, verbose_name="Предмет")
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)	

	class Meta:
		verbose_name = 'Практично-лабораторна робота'
		verbose_name_plural = 'Практично-лабораторні роботи'

	def __str__(self):
		return '%s робота %i : на тему : %s' % (self.get_kind_display(), self.number, self.title)


class PracticalWorkFile(models.Model):
	practical_work = models.ForeignKey(PracticalWork, verbose_name='')
	document = models.FileField(upload_to='data/practical_works/', verbose_name='Файл')

	class Meta:
		verbose_name = 'Файл до роботи'
		verbose_name_plural = 'Файли до робіт'

	def __str__(self):
		return str(self.pk)

class Lecture(models.Model):
	number = models.IntegerField(verbose_name='Номер')
	name = models.CharField(max_length=255, verbose_name='Тема')
	subject = models.ForeignKey(Subject, verbose_name="Предмет")
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)
	

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Лекція'
		verbose_name_plural = 'Лекції'

class LecturePart(models.Model):
	class Meta:
		abstract = True	
	title = models.TextField(verbose_name='Тема')
	lecture = models.OneToOneField(Lecture, verbose_name="Лекція")	


class Theory(LecturePart):
	document = models.FileField(upload_to='data/theory/', verbose_name='Файл')

	class Meta:
		verbose_name = 'Теорія'
		verbose_name_plural = 'Теорії'

	def __str__(self):
		return self.title

class Presentation(LecturePart):	
	document = models.FileField(upload_to='data/presentation/', verbose_name='Файл')

	class Meta:
		verbose_name = 'Презентація'
		verbose_name_plural = 'Презентації'

	def __str__(self):
		return self.title

class Video(LecturePart):
	document = models.FileField(upload_to='data/video/', verbose_name='Файл')

	class Meta:
		verbose_name = 'Відеофайл'
		verbose_name_plural = 'Відеофайли'

	def __str__(self):
		return self.title

class CheckTest(models.Model):
	title = models.CharField(max_length=255, verbose_name='Тест')
	doc_name = models.CharField(max_length=255, blank=True, verbose_name='Файл')
	subject = models.ForeignKey(Subject, verbose_name='Предмет')
