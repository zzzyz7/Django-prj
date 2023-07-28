from django import template
from pet.models import Pet

register = template.Library()

@register.simple_tag
def hasUserFavouritePet(favouriteList, userID):
    return favouriteList.filter(id=userID).exists()