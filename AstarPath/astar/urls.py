from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='home'),
  path('add/', views.add, name='add'),
  path('addher/', views.addher, name='addher'),
  path('fsp/', views.fsp, name='fsp'),
  path('fsp/fspastar/', views.fspastar, name='fspastar'),
  path('add/addrecord/', views.addrecord, name='addrecord'),
  path('addher/addrecordher/', views.addrecordher, name='addrecordher'),
  path('delete/<int:id>', views.delete, name='delete'),
  path('deleteher/<int:id>', views.deleteher, name='deleteher'),
  path('update/<int:id>', views.update, name='update'),
  path('updateher/<int:id>', views.updateher, name='updateher'),
  path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
  path('updateher/updaterecordher/<int:id>', views.updaterecordher, name='updaterecordher'),
  
]
