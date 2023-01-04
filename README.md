# Menu Management Api Application
## A Django rest framework application used to showcase an api performing full crud operations

Please Visit my repository on https://github.com/Ndhlovu1/django-crud-api-system

### To properly implement the Api's
##### Go into the AppFolders/models.py file and add the table attributes that'll be present as forms in the Api calls
```Python3
class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

```

##### Create the serializers.py file to implement the serializers as connecters into the database

```
from rest_framework import serializers
from .models import MenuItem

class menuItSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)



class MenuItemSerializer(serializers.ModelSerializer):
    #The Meta class is only needed if the serializers.ModelSerializer is imported 
    class Meta:
        model = MenuItem
        fields = ['id','title','price','inventory']

```

#### A Get Call
![Screenshot from 2022-12-28 11-08-39](https://user-images.githubusercontent.com/46927702/209790347-a59ef498-9b67-4c18-afd5-a7079ef6b155.png)


#### An Inset/Put Call
![Screenshot from 2022-12-28 11-09-18](https://user-images.githubusercontent.com/46927702/209790355-0025b610-2db4-4716-a311-f422a07d4404.png)


#### The Project/urls.py file is going to inherit the App/urls.py hence add the code below into a newly created urls.py file in the app folder


```Python3
from django.urls import path
from . import views

urlpatterns = [
    path('menu-items', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    
]


```

![Screenshot from 2022-12-28 11-30-04](https://user-images.githubusercontent.com/46927702/209790529-ad628055-8206-46f8-9257-7858cbd85bba.png)


#### The App level urls.py file
![Screenshot from 2022-12-28 11-30-13](https://user-images.githubusercontent.com/46927702/209790533-08d1b433-fc81-421c-82e5-c0eb1fdd4fd9.png)

```shell
> pipenv install djangorestframework
```

#### You should also see the djangorestframework file added into your Pipfile that keeps your dependencies

```file
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
django = "*"
djangorestframework = "*"

[dev-packages]

[requires]
python_version = "3.8"

```


```Python3
# Go into the settings.py file and change the line below
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
] # The default INSTALLED_APPS LOOKS LIKE THIS LIST

```

```Python3

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'menuApiApp',
] 
# Dont remove that last coma, 
# The names of your apps must also be added into this list element

```

#### Add the 'rest_framework' into the installed apps
![Screenshot from 2022-12-28 11-32-43](https://user-images.githubusercontent.com/46927702/209790781-7ffd91d8-e0a4-46d5-9f92-79fd74d690de.png)
