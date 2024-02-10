from django.shortcuts import render, redirect
from .models import UserRegistrar, SocietyModel
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == 'POST':
        email = request.POST["email"]
        firstName = request.POST["firstName"]
        lastName = request.POST["lastName"]
        phoneNumber = request.POST["phoneNumber"]
        level = request.POST["level"]
        societies = request.POST.getlist("societies")
        IEEE_number = request.POST["IEEE_number"]
        
        ### PERFORM SOME LOGIC ###
        ## START CODE ##
        society_instance = SocietyModel.objects.filter(pk__in=societies)

        
        if UserRegistrar.objects.filter(email__iexact=email).exists():
            messages.error(request, 'A User with this Email exists')
            return redirect('register')
        else:
            user = UserRegistrar.objects.create(email=email, firstName=firstName, lastName=lastName, phoneNumber=phoneNumber, level=level)
            if IEEE_number:
                user.IEEE_number = IEEE_number
            user.societies.set(society_instance)
            user.save()
            messages.success(request, 'Thank you for Registering with us!!!')
            return redirect("register")
        
        ## END CODE ##
        
    return render(request, "registration.html")