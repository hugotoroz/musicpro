from django.shortcuts import redirect, render
from django.contrib.auth import logout
from .forms import SignUpForm
from order.views import user_orders
from django.contrib.auth.decorators import login_required

def logout_view(request):
    logout(request)
    return redirect('../../cuenta/login')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
   
            form.save()
            return redirect('../../cuenta/login')

    else:
        form = SignUpForm()

    return render(request, 'cuenta/signup.html',{
        'form': form,
    })

@login_required
def dashboard(request):
    order = user_orders(request)
    return render(request,'cuenta/dashboard.html', {'order': order})

