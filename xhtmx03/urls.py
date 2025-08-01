from django.contrib import admin
from django.urls import include, path
from configurations.views import CustomLoginView, page_inconnue, tableau_de_bord
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('tableau/', tableau_de_bord, name='tableau'),
    path('', include('configurations.urls', namespace='configurations')),
]

handler404 = "configurations.views.page_inconnue"
