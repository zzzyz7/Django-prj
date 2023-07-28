from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateUploadForm
# from .forms import UserForm
from . import forms
from . import models
from .models import Upload
from pet.models import Pet
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from contact.forms import ContactForm
from contact.models import Contact
from django.contrib.auth import authenticate
from django.contrib.auth import login as user_login
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
# Create your views here.
# def home(request):
# 	count = User.objects.count()
# 	return render(request, 'home.html',{
# 		'count': count
# 	})

def home(request):
	pet = Pet.objects.all()
	males = Pet.objects.filter(sex="Male")
	females = Pet.objects.filter(sex="Female")
	return render(request, 'home.html',{'pet': pet, "males":males, "females":females})

@csrf_protect
def register(request):
    if request.method == 'POST':
            
        user = User.objects.create_user(
            username=request.POST.get('username'),
            password=request.POST.get('password'),
            email=request.POST.get('email'),
            first_name=request.POST.get('firstname'),
            last_name=request.POST.get('lastname'),
            )
        user.save()
        return redirect('login')
    
    return render(request, "registration/signup.html", {})
    # if request.session.get('is_login', None):
    #     return redirect('/index/')

    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password1 = request.POST.get('password1')
    #     password2 = request.POST.get('password2')
    #     email = request.POST.get('email')
    #     if password1 != password2:
    #         message = 'Different Password'
    #         return render(request, 'registration/signup.html', {})
    #     else:
    #         same_name_user = User.objects.filter(username=username)
    #         if same_name_user:
    #             message = 'User Exist!'
    #             return render(request, 'registration/signup.html', {})
    #         same_email_user = User.objects.filter(email=email)
    #         if same_email_user:
    #             message = 'Email been used'
    #             return render(request, 'registration/signup.html', {})

    #         user = User.objects.create_user(username, email, password1)
    #         user.save()
    #             # new_user = models.User()
    #             # new_user.name = username
    #             # new_user.password = password1
    #             # new_user.email = email
    #             # new_user.sex = sex
    #             # new_user.save()

    #         return redirect('/login/')
    # else:
    #     return render(request, 'registration/signup.html', locals())
    # register_form = forms.RegisterForm()
    # return render(request, 'registration/signup.html', locals())
@login_required
def home_favourite_pet(request, petID):
	pet = get_object_or_404(Pet, id=petID)

	if pet.favourite.filter(id=request.user.id).exists():
		pet.favourite.remove(request.user)
	else:
		pet.favourite.add(request.user)
	return redirect('home')

#https://www.youtube.com/watch?v=1XiJvIuvqhs&list=PLKILtxhEt4-RT-GkrDkJDLuRPQfSK-6Yi&index=51
def favourites(request):
	favourite_pets = request.user.favourite.all()
	context = {
		'favourite_pets': favourite_pets
	}
	return render(request, 'favourite_pets.html', context)

def remove_favourite(request, petID):
	pet = get_object_or_404(Pet, id=petID)

	if pet.favourite.filter(id=request.user.id).exists():
		pet.favourite.remove(request.user)
	else:
		pet.favourite.add(request.user)
	return redirect('favourites')

@login_required
def secret_page(request):
    if request.method == 'POST':
        user = request.user
        if len(request.POST['username'])>0:
            user.username = request.POST['username']
        if len(request.POST['email'])>0:
            user.email = request.POST['email']
        if len(request.POST['firstname'])>0:
            user.first_name = request.POST['firstname']
        if len(request.POST['lastname'])>0:
            user.last_name = request.POST['lastname']

        user.save()
        return redirect('secret')


    return render(request, "secret_page.html", {})

class SecretPage(LoginRequiredMixin, TemplateView):
	template_name = 'secret_page.html'

def upload(request):
    if request.method == 'POST':
        pet = Pet(
            name = request.POST.get('name'),
            breed =request.POST.get('breed'),
            age = request.POST.get('age'),
            image =request.POST.get('image'),
            description = request.POST.get('description'),
            friendly = request.POST.get('friendly'),
        )
        if pet.age.isdigit():
            if pet.friendly.isdigit():
                pet.save()
                return redirect('home')
        else:
            message = 'please input right information!'
  
    return render(request, 'upload.html', {})
    
    # return render(request, "registration/signup.html", {})
    # if request.method == 'POST':
    #     form = CreateUploadForm(data=request.POST, files=request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponse('<h1> Uploaded')
    # else:
    #     form = CreateUploadForm()
    # context = {
    #     'form' : form
    # }
    # return render(request, 'upload.html', context)

def search(request):
    pets = Pet.objects.all()
    search_query = request.GET.get('q')

    if search_query:
        pets = pets.filter(
            Q(name__icontains=search_query) |
            Q(breed__icontains=search_query) |
            Q(sex__iexact=search_query)
        )
    return render(request, 'search.html', {'pets': pets, 'search_query': search_query})

def about(request):
	return render(request, 'about.html',{})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            user_login(request, user)
            return redirect('/')
        else:
            message = 'User Not Exist or Password Wrong'
            # return render(request, 'registration/login.html', locals())
        # user_login(request, user)
            # return redirect('/')

    return render(request, 'registration/login.html', locals())


def detail(request, pet_id):
	pet = get_object_or_404(Pet, pk=pet_id)
	pets= Pet.objects.all()
	return render(request, 'detail.html', {'pet': pet, 'pets': pets})


def donate(request):
	return render(request, 'donate.html',{})


# def contact(request):
#     if request.method == 'GET':
#         form = ContactForm()
#     else:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             from_email = form.cleaned_data['from_email']
#             message = form.cleaned_data['message']
#             try:
#                 send_mail(name, message, from_email, ['admin@example.com'])
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return redirect('success')
#     return render(request, "contact.html", {'form': form})
def contact(request):
    if request.method == 'POST':
            
        new_contact = Contact(
            name=request.POST.get('name'),
            from_email=request.POST.get('from_email'),
            message=request.POST.get('message'),
            
            )
        new_contact.save()
        return redirect('home')
        # send_mail(name, message, from_email, ['admin@example.com'])
        

    return render(request, "contact.html", {})


def success(request):
    return render(request,'success.html', {})

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password_reset.html", context={"password_reset_form":password_reset_form})


# def profile_edit(request):
#     if request.method == 'POST':
#         user = authenticate(username=username, password=password)
#         exist = User.objects.filter(username=username).exists()
#         if exist:
#             user.username=request.POST.get('name'),
#             user.email=request.POST.get('email'),
#             user.first_name=request.POST.get('firstname'),
#             user.last_name=request.POST.get('lastname'),

#             user.save()
#             return HttpResponseRedirect('secret')


#     return render(request, "secret_page.html", {})