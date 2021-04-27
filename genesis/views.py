from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.
class GenesisListView(ListView):
    model = Post
    template_name = 'home.html'


class GenesisDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class GenesisCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']


class GenesisUpdateView(UpdateView):
    fields = ['title', 'content']

    def test_func(self):
        obj = self.get_object()

        return obj.author == self.request.user


class GenesisDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    form_class = UserRegistrationForm


class PasswordsChangeView(SuccessMessageMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('logout')
    success_message = "Your Password was successfully changed!!!"



def login_request(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, "Invalid username or password.")
        context = {}
        return render(request, "registration/login.html", context)


def logout_request(request):
    logout(request)
    messages.success(request, 'You were successfully Logged Out')
    return redirect('login')


