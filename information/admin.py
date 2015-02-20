from django.contrib import admin
from .models import Speciality, CourseNumber, Subject

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


admin.site.register(Subject)
admin.site.register(Speciality, SpecialityOption)