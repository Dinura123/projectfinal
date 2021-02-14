from django import forms
from django.contrib.auth.models import User
from  .models import Car, User, Offer, Reservation
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)


    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
     )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save() 
            return user


class Addcarform(forms.ModelForm):
    class Meta:
        model = Car
        fields = (
            'brand',
            'model',
            'image',
            'price',
            'transmission',
            'mileage',
            'description',
        )
    def save(self, commit=True):
        addcar = super(Addcarform, self).save(commit=False)
        addcar.brand = self.cleaned_data['brand']
        addcar.model = self.cleaned_data['model']
        addcar.image = self.cleaned_data['image']
        addcar.price = self.cleaned_data['price']
        addcar.transmission = self.cleaned_data['transmission']
        addcar.mileage = self.cleaned_data['mileage']
        addcar.description = self.cleaned_data['description']

        if commit:
            addcar.save()
            return addcar

class Updatecarform(forms.ModelForm):
    class Meta:
        model = Car
        fields = (
            'brand',
            'model',
            'image',
            'price',
            'transmission',
            'mileage',
            'description', 
        )
    
    def save(self, commit=True):
        updatecar = super(Updatecarform, self).save(commit=False)
        updatecar.brand = self.cleaned_data['brand']
        updatecar.model = self.cleaned_data['model']
        updatecar.price = self.cleaned_data['price']
        updatecar.transmission = self.cleaned_data['transmission']
        updatecar.mileage = self.cleaned_data['mileage']
        updatecar.description = self.cleaned_data['description']

        if self.cleaned_data['image']:
            updatecar.image = self.cleaned_data['image']


        if commit:
            updatecar.save()
            return updatecar

class Offerform(forms.ModelForm):
    class Meta:
        model = Offer
        fields = (
            'model',
            'name',
            'email',
            'contact_number',
            'amount',
            'message',
            'car'
        )
    def save(self, commit=True):
        offer = super(Offerform, self).save(commit=False)
        offer.model = self.cleaned_data['model']
        offer.name = self.cleaned_data['name']
        offer.email = self.cleaned_data['email']
        offer.contact_number = self.cleaned_data['contact_number']
        offer.amount = self.cleaned_data['amount']
        offer.message = self.cleaned_data['message']
        offer.car = self.cleaned_data['car']

        if commit:
            offer.save()
            return offer

class Requestofferform(forms.ModelForm):
    class Meta:
        model = Offer
        fields = (
            'model',
            'name',
            'email',
            'contact_number',
            'amount',
            'message',
            'car'
        )
    def save(self, commit=True):
        requestoffer = super(Requestofferform, self).save(commit=False)
        requestoffer.model = self.cleaned_data['model']
        requestoffer.name = self.cleaned_data['name']
        requestoffer.email = self.cleaned_data['email']
        requestoffer.contact_number = self.cleaned_data['contact_number']
        requestoffer.amount = self.cleaned_data['amount']
        requestoffer.message = self.cleaned_data['message']
        requestoffer.car = self.cleaned_data['car']

        if commit:
            requestoffer.save()
            return requestoffer

class Reservationform(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = (
            'full_name',
            'email',
            'message',
            'contact_number',
        )
    def save(self, commit=True):
        reservation = super(Reservationform, self).save(commit=False)
        reservation.full_name = self.cleaned_data['full_name']
        reservation.email = self.cleaned_data['email']
        reservation.message = self.cleaned_data['message']
        reservation.contact_number = self.cleaned_data['contact_number']

        if commit:
            reservation.save()
            return reservation
