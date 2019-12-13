from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('account/', include('django.contrib.auth.urls')),
    path('account/register/', views.signup, name='signup'),
    path('new-recipe/',views.add_recipe, name='new-recipe'),
    path('all-recipes/',views.recipes,name='food'),
    path('single_recipe/<recipe_id>', views.single_recipe, name='single-recipe'),
    path('profile/<username>/edit/', views.edit_profile, name='edit-profile'),
    path('profile/<username>', views.profile, name='profile'),
    path('favourite_recipe/<id>', views.favourite_recipe,name='favourite_recipe'),
    path('favourites/',views.recipe_favourite_list, name='recipe_favourite_list'),
    # path('ajax/newsletter/', views.newsletter, name ='newsletter')
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
