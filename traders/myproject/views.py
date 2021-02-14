from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from .forms import (
    RegistrationForm,
    Addcarform,
    Updatecarform,
    Offerform,
    Requestofferform,
    Reservationform,
)
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, authenticate, login
from myproject.models import Car, User, Offer, Reservation 
from django.contrib import messages




def index(request):
    return render(request,'myproject/index.html')

def about(request):
    return render(request,'myproject/about.html')

def Vehicle(request):
    if request.method == 'POST':
        offer_form = Offerform(request.POST)
        if offer_form.is_valid():
            offer_form.save()
            return redirect('Vehicle')

        else:
            args = {'offer_form': offer_form}
            return render(request,'myproject/Vehicle.html', args)

    else:
        offer_form = Offerform()

        args = {'offer_form': offer_form, 'nbar': 'Vehicle'}
    return render(request,'myproject/Vehicle.html', args)


def contact(request):
    if request.method == 'POST':
        reservation_form = Reservationform(request.POST)
        if reservation_form.is_valid():
            reservation_form.save()
            return redirect('contact')

        else:
            args = {'reservation_form': reservation_form}
            return render(request,'myproject/contact.html', args)

    else:
        reservation_form = Reservationform()

        args = {'reservation_form': reservation_form, 'nbar': 'contact'}
    return render(request,'myproject/contact.html', args)

    

def signin(request):
    return render(request,'myproject/sign-in.html')

def signup(request):
        if request.method == 'POST':
            form = RegistrationForm(request.POST)

            if form.is_valid():
                form.save()
                
                return redirect('sign-in')

            else:
                form = RegistrationForm()
                args = {'form': form} 
                return render(request, 'myproject/sign-up.html', args)
        
        else:
            form = RegistrationForm()
            args = {'form': form} 
            return render(request,'myproject/sign-up.html', args)


@user_passes_test(lambda u: u.is_superuser)
def dashboard(request):
    if request.method == 'GET':
        reservation = Reservation.objects.all()

        args = {'reservation': reservation, 'nbar': 'dashboard'}
    return render(request,'myproject/dashboard.html', args)


@user_passes_test(lambda u: u.is_superuser)
def addcar(request):
    if request.method == 'GET':
        addcar = Car.objects.all()
        args = {'addcar': addcar}
        return render(request, 'myproject/addcar.html', args)

@user_passes_test(lambda u: u.is_superuser)
def edit_car(request, id):

    args = {}
    car = Car.objects.get(id=id)
    form = Updatecarform(request.POST, instance=recipient)

    if request.method == 'POST':
        form = Updatecarform(request.POST, instance=recipient)
        if form.is_valid():
            form.save()
            return redirect('../../')

        else:
        
            args = {'form': form}
            return render(request, 'myproject/edit_car.html', args)

    else:
        form = Updatecarform(instance=recipient)
        args = {'form': form}
        return render(request, 'myproject/edit_car.html', args)

@user_passes_test(lambda u: u.is_superuser)
def delete_car(request, id):
    car = Car.objects.get(id=id)
    if request.method == 'POST':
        car.delete()
        return redirect('addcar')

    args = {'car': car}
    return render(request, 'myproject/delete_car.html', args)


@user_passes_test(lambda u: u.is_superuser)
def offer(request):
    if request.method == 'GET':
        offer = Offer.objects.all()
        args = {'offer': offer}
        return render(request, 'myproject/offer.html', args)

@user_passes_test(lambda u: u.is_superuser)
def delete_offer(request, id):
    offer = Offer.objects.get(id=id)
    if request.method == 'POST':
        offer.delete()
        return redirect('../../')

    args = {'offer': offer}
    return render(request, 'myproject/delete_offer.html', args)

@user_passes_test(lambda u: u.is_superuser)
def add_car(request):
    if request.method == 'POST':
        addcar_form = Addcarform(request.POST, request.FILES)
        if addcar_form.is_valid():
            addcar_form.save()
            return redirect ('../')

        else:
            args = {'addcar_form': addcar_form}
            return render(request, 'myproject/add_car.html', args)

    else:
        addcar_form = addcar_form()
        args = {'addcar_form': addcar_form}
        return render(request, 'myproject/add_car.html', args)

@user_passes_test(lambda u: u.is_superuser)
def reservation(request):
    if request.method == 'GET':
        reservation = Reservation.objects.all()
        args = {'reservation': reservation}
        return render(request, 'myproject/reservation.html', args)

@user_passes_test(lambda u: u.is_superuser)
def view_reservation(request, id):
    reservation =  Reservation.objects.get(id=id)
    args = {'reservation': reservation} 
    return render(request, 'myproject/view_reservation.html', args)

@user_passes_test(lambda u: u.is_superuser)
def user(request):

    user = User.objects.all().exclude(is_superuser=True)
    args = {'user': user}
    return render(request, 'myproject/user.html', args)

@user_passes_test(lambda u: u.is_superuser)
def delete_user(request):

    user = User.objects.all().exclude(is_superuser=True)
    if request.method == 'POST':
        user.delete()
        return redirect('../../')
    args = {'user': user}
    return render(request, 'myproject/delete_user.html', args)