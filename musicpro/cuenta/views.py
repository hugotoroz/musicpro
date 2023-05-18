from django.shortcuts import redirect, render
from django.contrib.auth import logout
from order.views import user_orders
from django.contrib.auth.decorators import login_required

def logout_view(request):
    logout(request)
    return redirect('../../cuenta/login')

@login_required
def dashboard(request):
    order = user_orders(request)
    return render(request,'cuenta/dashboard.html', {'order': order})