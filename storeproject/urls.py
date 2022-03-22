from django.contrib import admin
from django.urls import path, include
from members import views as user_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('register/', user_view.register_user, name="user-register"),
    path('login/', user_view.login_user, name="user-login"),
    path('logout', user_view.logout_user, name="user-logout"),
    path('profile/', user_view.profile, name="user-profile"),
    path('profile/update/', user_view.profile_update, name="user-profile_update"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
