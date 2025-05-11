# Ex.05 Design a Website for Server Side Processing
## Date:11-05-25

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
math.html

<html>
<head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>Lamp Filament Power Calculator</title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <style type="text/css">
        body {
            background-color: #0d8d88f2;
        }
        .edge {
            width: 100%;
            padding-top: 180px;
            text-align: center;
        }
        .box {
            display: inline-block;
            border: thick dashed #cd4f8e;
            width: 500px;
            min-height: 300px;
            font-size: 20px;
            background-color: rgb(67, 122, 204);
        }
        .formelt {
            color: black;
            text-align: center;
            margin-top: 8px;
            margin-bottom: 6px;
        }
        h1 {
            color: black;
            padding-top: 20px;
        }
    </style>
</head>
<body>
    <div class="edge">
        <div class="box">
            <h1>Lamp Filament Power Calculator</h1>
            <h3>Akash Prakash (212224240008)</h3>
            <form method="POST">
                {% csrf_token %}
                <div class="formelt">
                    Intensity (I): <input type="text" name="intensity" value="{{ I }}"> A<br/>
                </div>
                <div class="formelt">
                    Resistance (R): <input type="text" name="resistance" value="{{ R }}"> Ω<br/>
                </div>
                <div class="formelt">
                    <input type="submit" value="Calculate"><br/>
                </div>
                <div class="formelt">
                    Power (P): <input type="text" name="power" value="{{ P }}"> W<br/>
                </div>
            </form>
        </div>
    </div>
</body>
</html>

views.py

from django.shortcuts import render

def calculate_power(request):
    context = {
        'P': "0",
        'I': "0",
        'R': "0"
    }

    if request.method == 'POST':
        print("POST method is used")
        print('request.POST:', request.POST)

        I = request.POST.get('intensity', '0')
        R = request.POST.get('resistance', '0')

        print('Intensity (I) =', I)
        print('Resistance (R) =', R)

        try:
            intensity = float(I)
            resistance = float(R)
            power = intensity ** 2 * resistance
            context['P'] = round(power, 2)
        except ValueError:
            context['P'] = "Invalid input"

        context['I'] = I
        context['R'] = R
        print('Power (P) =', context['P'])

    return render(request, 'mathapp/math.html', context)
urls.py
from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculatepower/', views.calculate_power, name="calculate_power"),
    path('', views.calculate_power, name="calculate_power_home")
]


```


## SERVER SIDE PROCESSING:

![alt text](<Screenshot 2025-05-11 191726.png>)


## HOMEPAGE:

![alt text](<Screenshot 2025-05-11 191826.png>)

## RESULT:
The program for performing server side processing is completed successfully.
