from django.shortcuts import render
from information.models import Speciality, CourseNumber, Subject, Lecture, PracticalWork, Video, Theory, CheckTest, PracticalWorkFile, Presentation
import sys
import os


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

def subject_show(request, subject_id):
	subject = Subject.objects.get(id=subject_id)
	lectures = Lecture.objects.filter(subject=subject_id)
	prs = PracticalWork.objects.filter(subject=subject_id,kind=1)
	lrs = PracticalWork.objects.filter(subject=subject_id,kind=2)
	tests = CheckTest.objects.filter(subject=subject_id)
	return render(request,'subject.html',{'subject':subject,'lectures':lectures,'prs':prs,'lrs':lrs,'tests':tests})

def video_show(request,subject_id,video_id):
	video = Video.objects.get(id=video_id)
	subject = Subject.objects.get(id=subject_id)
	slide = 1
	return render(request,'videoplay.html',{'video':video,'subject':subject,'slide':slide})

def theory_show(request,subject_id,theory_id):
	theory = Theory.objects.get(id=theory_id)
	subject = Subject.objects.get(id=subject_id)
	return render(request,'pdf.html',{'theory':theory,'subject':subject})

def pr_show(request,subject_id,pr_id):
	work = PracticalWork.objects.get(id=pr_id)
	subject = Subject.objects.get(id=subject_id)
	docs = PracticalWorkFile.objects.filter(practical_work=pr_id)
	return render(request,'practicalwork.html',{'work':work,'docs':docs,'subject':subject})

def test_show(request,subject_id,test_id):
	test = CheckTest.objects.get(id=test_id)
	return render(request,'test.html',{'test':test})

def presentation_show(request,subject_id,prs_id):
	folder = str(prs_id)
	os.makedirs(folder, exist_ok=True)
	files = os.listdir("mediafiles/data/pres/"+folder)
	subject = Subject.objects.get(id=subject_id)
	return render(request,'presentation.html',{'subject':subject,'files':files,'folder':folder})