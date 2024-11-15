from django.urls import path
from django.urls import path,include
from teachers import views
from django.contrib import admin

from teachers.models import NewEntry

app_name = 'teachers'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('insert/',views.insert,name='insert'),
    path('insert_data/',views.insert_data,name='insert_data'),
    path('view_products/',views.view_product,name='view_product'),
    path('details/<id>/',views.get_product,name='details'),
    path('update/<id>/',views.update_product,name='update_product'),
    path('delete/<id>/',views.delete_product,name='delete_product'),

    path('StudFom/', views.Studinsert, name='Studinsert'),
    path('NewStudInsert/', views.NewStudInsert, name='NewStudInsert'),
    path('viewstudents/',views.viewstudents,name='view_students'),
    # path('stud_details/',views.Stud_Details,name='stud_details'),


]

