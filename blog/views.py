from django.shortcuts import render
from .models import Topics, Remarks, Homework, Submission, Project, Reminder, TimeTable, Post, Tweet
from django.views.generic import DetailView, CreateView
from django.contrib.auth.models import User
from users.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
	context = {
		'posts': Post.objects.all()
	}
	if(request.user.profile.role==1): 
		return render(request, 'blog/home.html', context)
	elif(request.user.profile.role==2):
		return render(request, 'blog/home1.html', context)
	else:
		return render(request, 'blog/base2.html', context)


def topic(request):
	context = {
		'topics': Topics.objects.filter(grade=request.user.profile.grade)
	}
	return render(request, 'blog/topics.html', context)

class TopicsDetailView(DetailView):
	model = Topics

def remarks(request):
	context = {
		'remarks': Remarks.objects.filter(grade=request.user.profile.grade, rollno=request.user.profile.rollno)
	}
	return render(request, 'blog/remarks.html', context)

class RemarksDetailView(DetailView):
	model = Remarks	

def homeworks(request):
	context = {
		'homeworks': Homework.objects.filter(grade=request.user.profile.grade)
	}	
	return render(request, 'blog/homeworks.html', context)

class HomeworkDetailView(DetailView):
	model = Homework

def submissions(request):
	context = {
		'submissions': Submission.objects.filter(grade=request.user.profile.grade)
	}	
	return render(request, 'blog/submissions.html', context)

class SubmissionDetailView(DetailView):
	model = Submission			

def projects(request):
	context = {
		'projects': Project.objects.filter(grade=request.user.profile.grade)
	}	
	return render(request, 'blog/projects.html', context)

class ProjectDetailView(DetailView):
	model = Project	

def reminders(request):
	context = {
		'reminders': Reminder.objects.filter(grade=request.user.profile.grade)
	}	
	return render(request, 'blog/reminders.html', context)

class ReminderDetailView(DetailView):
	model = Reminder	

def myclass(request):
	context = {
		'profiles': Profile.objects.filter(grade=request.user.profile.grade)
	}
	return render(request, 'blog/myclass.html', context)

def teachers(request):
	context = {
		'profiles': Profile.objects.filter(role=2)
	}	
	return render(request, 'blog/teachers.html', context)

class UsersDetailView(DetailView):
	model = User	

def timetable(request):
	context = {
		'timetable': TimeTable.objects.all()
	}	
	if(request.user.profile.role==1):
		return render(request, 'blog/timetable.html', context)
	else:
		return render(request, 'blog/timetable1.html', context)	
def works(request):
	return render(request, 'blog/works.html')	

class TopicCreateView(LoginRequiredMixin, CreateView):
    model = Topics
    fields = ['grade','title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RemarkCreateView(LoginRequiredMixin, CreateView):
    model = Remarks
    fields = ['grade','title', 'rollno', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class HomeworkCreateView(LoginRequiredMixin, CreateView):
    model = Homework
    fields = ['grade','title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class SubmissionCreateView(LoginRequiredMixin, CreateView):
    model = Submission
    fields = ['grade','title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ReminderCreateView(LoginRequiredMixin, CreateView):
    model = Reminder
    fields = ['grade','title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['grade','title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TimeTableCreateView(LoginRequiredMixin, CreateView):
    model = TimeTable
    fields = ['grade','title', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)   

def mytopics(request):
	context = {
		'topics': Topics.objects.filter(author=request.user)
	}                                                     
	return render(request, 'blog/my_topics.html', context)

def myremarks(request):
	context = {
		'remarks': Remarks.objects.filter(author=request.user)
	}                                                     
	return render(request, 'blog/my_remarks.html', context)

def myhomeworks(request):
	context = {
		'homeworks': Homework.objects.filter(author=request.user)
	}                                                     
	return render(request, 'blog/my_homeworks.html', context)

def myreminders(request):
	context = {
		'reminders': Reminder.objects.filter(author=request.user)
	}                                                     
	return render(request, 'blog/my_reminders.html', context)

def mysubmissions(request):
	context = {
		'submissions': Submission.objects.filter(author=request.user)
	}                                                     
	return render(request, 'blog/my_submissions.html', context)

def myprojects(request):
	context = {
		'projects': Project.objects.filter(author=request.user)
	}                                                     
	return render(request, 'blog/my_projects.html', context)					

class PostDetailView(DetailView):
	model = Post

class TweetDetailView(DetailView):
	model = Tweet	

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content','image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TweetCreateView(LoginRequiredMixin, CreateView):
    model = Tweet
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)        	