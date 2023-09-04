from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
import pandas as pd
import pickle as pkl
from polls.models import Crop
# from .models import History
from django.contrib import messages
from django.contrib.auth import logout
from django.http import JsonResponse


# def login(request):
#     return HttpResponse("hello i am working")
@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


def Signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:

            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login1')

    return render(request, 'signup1.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!")

    return render (request,'login1.html')

def LogoutPage(request):
    logout(request)
    return redirect('login1')

def predict(request):
    return render(request, 'predict.html')


def result(request):
    datapath = str(settings.BASE_DIR) + "/ML_Project/"
    output = None

    if request.method == "POST":
        predli = [float(request.POST['N']), float(request.POST['P']), float(request.POST['k']),
                  float(request.POST['temperature']), float(request.POST['humidity']),
                  float(request.POST['ph']), float(request.POST['rainfall'])]
        notes = str(request.POST['notes'])

        # Print the received data
        print("N:", predli[0])
        print("P:", predli[1])
        print("K:", predli[2])
        print("Temperature:", predli[3])
        print("Humidity:", predli[4])
        print("pH:", predli[5])
        print("Rainfall:", predli[6])
        print("notes:", notes)
        # print("result:", output)
        #
        # try:
        #     crop = Crop(
        #         N=predli[0],
        #         P=predli[1],
        #         k=predli[2],
        #         temperature=predli[3],
        #         humidity=predli[4],
        #         ph=predli[5],
        #         rainfall=predli[6],
        #         notes=notes,
        #         prediction_result = output
        #     )
        #     crop.save()
        # except Exception as e:
        #     print("An error occurred while saving:", e)

    crop = pd.read_csv(datapath + 'crop_recommendation_test.csv')
    with open(datapath + 'Crop_recommendation_RF.pkl', 'rb') as f:
        model = pkl.load(f)

    crop_test = crop.iloc[:, 1:-1]
    y = crop.iloc[:, -1]
    model.score(crop_test, y)
    pred = model.predict(crop_test)

    label_name = pd.read_csv(datapath + 'label_name_number.csv').iloc[:, 1:]

    res = model.predict([predli])
    predicted_crop_number = int(res)

    if predicted_crop_number in label_name['Crop_number'].values:
        index_number = label_name[label_name['Crop_number'] == predicted_crop_number].index[0]
        crop_name = label_name.loc[index_number, 'crop_name']
        output = crop_name.title()

    try:
        crop = Crop(
            N=predli[0],
            P=predli[1],
            k=predli[2],
            temperature=predli[3],
            humidity=predli[4],
            ph=predli[5],
            rainfall=predli[6],
            notes=notes,
            prediction_result=output
        )
        crop.save()
    except Exception as e:
        print("An error occurred while saving:", e)
    return render(request, 'result.html', {"result": output})

def history(request):

    my_crops = Crop.objects.all()
    context = {'crops': my_crops}

    return render(request, 'history.html', context=context)
