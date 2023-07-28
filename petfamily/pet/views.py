from django.shortcuts import render
from .models import Pet
from .serializers import PetSerializer
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# from rest_framework import viewsets
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticatedOrReadOnly


# class PetViewSet(viewsets.ModelViewSet):
#     authentication_classes = (BasicAuthentication,)
#     permission_classes = (IsAuthenticatedOrReadOnly, )
#     queryset = Pet.objects.all()
#     serializer_class = PetSerializer

# @login_required
# def home_favourite_pet(request, petID):
# 	pet = get_object_or_404(Pet, id=petID)

# 	if pet.favourite.filter(id=request.user.id).exists():
# 		pet.favourite.remove(request.user)
# 	else:
# 		pet.favourite.add(request.user)
# 	return redirect('home')

# #https://www.youtube.com/watch?v=1XiJvIuvqhs&list=PLKILtxhEt4-RT-GkrDkJDLuRPQfSK-6Yi&index=51
# def favourites(request):
# 	favourite_pets = request.user.favourite.all()
# 	context = {
# 		'favourite_pets': favourite_pets
# 	}
# 	return render(request, 'favourite_pets.html', context)

# def remove_favourite(request, petID):
# 	pet = get_object_or_404(Pet, id=petID)

# 	if pet.favourite.filter(id=request.user.id).exists():
# 		pet.favourite.remove(request.user)
# 	else:
# 		pet.favourite.add(request.user)
# 	return redirect('favourites')