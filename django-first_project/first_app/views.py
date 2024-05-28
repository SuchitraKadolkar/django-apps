from django.shortcuts import render
#from django.http import HttpResponse
#from first_app.models import User
from first_app.signup import NewUserForm

# Create your views here.
def index(request):
    return render(request, 'first_app/index.html')

def user(request):
    # users_list = User.objects.order_by('first_name')
    # users_dict = {"get_user": users_list}
    # return render(request, 'first_app/user.html', context=users_dict)
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Form is invalid")
    return render(request, 'first_app/user.html', {'form': form})