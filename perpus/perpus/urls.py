from django.contrib import admin
from django.urls import path, include
from perpustakaan.views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from perpustakaan.viewset_api import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('kelompok', KelompokViewset)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('penerbit/', penerbit, name='penerbit'),
    path('buku/', buku, name='buku'),
    path('buku/tambah/', tambah_buku, name='tambah_buku'),
    path('buku/ubah/<int:id_buku>', ubah_buku, name='ubah_buku'),
    path('buku/hapus/<int:id_buku>', hapus_buku, name="hapus_buku"),
    path('buku/export/xls/', export_xls, name='export_xls'),
    path('auth/masuk/', LoginView.as_view(), name='masuk'),
    path('auth/keluar/', LogoutView.as_view(next_page='masuk'), name='keluar'),
    path('user/', users, name='users'),
    path('user/add/', signup, name='signup'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)