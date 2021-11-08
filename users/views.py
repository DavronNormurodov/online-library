from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
# Create your views here.

# def home(request):
#     return render(request, 'users/home.html')

# def signup(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(
#                 request, f"Welcom {username}, your account is created")
#             return redirect('/')
#         else:
#             messages.success(
#                 request, "unvalid input")
#             return redirect('signup')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'users/signup.html', {'form': form})

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'