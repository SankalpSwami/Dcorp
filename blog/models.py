from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse


class Topics(models.Model):
	grade = models.TextField()
	title = models.CharField(max_length=100)
	content = models.TextField()
	date = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse('topics-detail', kwargs={'pk': self.pk})		

class Remarks(models.Model):
	grade = models.TextField()
	rollno = models.IntegerField()
	title = models.CharField(max_length=100)
	content = models.TextField()
	date = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('remarks-detail', kwargs={'pk': self.pk})

class Homework(models.Model):
	grade = models.TextField()
	title = models.CharField(max_length=100)
	content = models.TextField()
	date = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title 	

	def get_absolute_url(self):
		return reverse('homeworks-detail', kwargs={'pk': self.pk})

class Submission(models.Model):
	grade = models.TextField()
	title = models.CharField(max_length=100)
	content = models.TextField()
	date = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('submissions-detail', kwargs={'pk': self.pk})

class Project(models.Model):
	grade = models.TextField()
	title = models.CharField(max_length=100)
	content = models.TextField()
	date = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('projects-detail', kwargs={'pk': self.pk})
  		
class Reminder(models.Model):
	grade = models.TextField()
	title = models.CharField(max_length=100)
	content = models.TextField()
	date = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title	

	def get_absolute_url(self):
		return reverse('reminders-detail', kwargs={'pk': self.pk})

class TimeTable(models.Model):
	grade = models.TextField()
	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to='images')
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.title			

	def get_absolute_url(self):
		return reverse('blog-timetable', kwargs={'pk': self.pk})

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='post_pics')
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Tweet(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tweet-detail', kwargs={'pk': self.pk})        


