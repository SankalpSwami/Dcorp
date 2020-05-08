from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
	if (request.user.profile.role==2):
		return render(request, 'users/profile.html')
	else:
		return render(request, 'users/profile1.html')