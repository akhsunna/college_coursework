from django.shortcuts import render
from information.models import Speciality, CourseNumber, Subject, Lecture, PracticalWork

def speciality_list(request):
	specialities = Speciality.objects.all()
	return render(request,'speciality.html',{'specialities':specialities})

def course_list(request, speciality_id):
	courses = CourseNumber.objects.all()
	speciality = Speciality.objects.get(id=speciality_id)
	return render(request,'courses.html',{'courses':courses,'speciality_id':speciality_id,'speciality':speciality})

def subject_list(request, speciality_id, course_id):
	subjects = Subject.objects.filter(specialty=speciality_id,year=course_id)
	return render(request,'subjects.html',{'subjects':subjects,'course_id':course_id,'speciality_id':speciality_id})

def subject_show(request, speciality_id, course_id, subject_id):
	subject = Subject.objects.get(id=subject_id)
	lectures = Lecture.objects.filter(subject=subject_id)
	prs = PracticalWork.objects.filter(subject=subject_id,kind=1)
	lrs = PracticalWork.objects.filter(subject=subject_id,kind=2)
	return render(request,'subject.html',{'subject':subject,'lectures':lectures,'prs':prs,'lrs':lrs})

