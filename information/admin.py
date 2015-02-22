from django.contrib import admin
from .models import Speciality, CourseNumber, Subject, PracticalWorkFile, PracticalWork,Lecture, LecturePart, Theory, Presentation, Video, CheckTest 

class SpecialityOption(admin.ModelAdmin):
	fieldset = (
		('', {
			'fields': ('full_name', 'name',),
		}),
		('Flags', {
			'classes': ('grp-collapse grp-closed',),
			'fields': ('flag_front', 'flag_sticky', 'flag_allow_comments', 'flag_comments_closed',),
		}),
		('Tags', {
			'classes': ('grp-collapse grp-open',),
            'fields' : ('tags',),
			}),
	)


class StackedItemInLine(admin.StackedInline):
	classes = ('grp-collapse grp-open',)


class TabularItemInLine(admin.TabularInline):
	classes = ('grp-collapse grp-open',)


class PracticaInLine(admin.StackedInline):
	model = PracticalWorkFile
	extra = 0

class PracticaAdmin(admin.ModelAdmin):
	fields = ['kind', 'number', 'title', 'subject']
	inlines = [PracticaInLine]

class TheoryInline(admin.StackedInline):
	model = Theory
	extra = 1

class VideoInline(admin.StackedInline):
	model = Video
	extra = 1

class PresentationInline(admin.StackedInline):
	model = Presentation
	extra = 1

class LectureAdmin(admin.ModelAdmin):
	fields = ['name', 'number', 'subject']
	inlines = [TheoryInline, VideoInline, PresentationInline]

admin.site.register(Lecture,LectureAdmin)
admin.site.register(PracticalWork, PracticaAdmin)
admin.site.register(Subject)
admin.site.register(Speciality, SpecialityOption)