from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView, CreateView, UpdateView
from django.contrib.auth import logout,authenticate
from .forms import RegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
# from .models import Profile
from django.contrib.messages.views import SuccessMessageMixin


# def base(request):
#     return render(request,'base.html')

class baseView(TemplateView):
    template_name = 'base.html'

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/login/')

# def logout_request(request):
#     logout(request)
#     messages.info(request, "Logged out successfully!")
#     return redirect("base")

# ####         login default page change         #################
# class LoginView(View):
#     def get(self, request, *args, **kwargs):
#         user = authenticate(username=username, password=password)
#         login(request,user)
#         template_name = 'registration/loginn.html'
#         success_url = reverse_lazy('/index/')
# class LoginView(View):
#     def function():
#         if request.method == "POST":
#             username = request.POST['username']
#             password = request.POST['password']
#             seo_specialist = authenticate(username=username, password=password)
#             if seo_specialist is not None:
#                 template_name = 'registration/loginn.html'
#                 return HttpResponse("Signed in")
#             else:
#                 return HttpResponse("Not signed in")
#         return HttpResponse("Signed in")
################



class RegisterView(SuccessMessageMixin, CreateView):
    template_name = 'registration/register.html'
    # template_name = 'registration/loginn.html'
    form_class = RegisterForm
    success_message = "Account Created Successfully"
    success_url = reverse_lazy('login')


# class ProfileView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
#     form_class = RegisterForm
#     template_name = 'registration/profile.html'
#     queryset = User.objects.all()
#     success_url = reverse_lazy('my_posts')
#     success_message = "Profile Updated Successfully"


# class ImageUpdateView(LoginRequiredMixin, TemplateView):
#     template_name = 'registration/profile_picture.html'

#     def post(self, request, *args, **kwargs):
#         img = request.FILES.get('image')
#         user = get_object_or_404(User, username=request.user.username)
#         user.profile.image = img
#         user.save()
#         return redirect('profile', request.user.id)
# from .models import Student
def student_show(request):
	# student = Student.objects.order_by('roll_no')
	return render(request, 'index.html')
