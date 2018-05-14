from django.shortcuts import render
def home_page(request):

    if request.method == 'POST':
        c_name = request.POST.get('customer_name')
        b_name = request.POST.get("barber_name")
        our_time =request.POST.get("time")

        return render(request,'haircut/home_page.html',{'customer_name': c_name, 'barber_name':b_name, 'time': our_time})   
    # Create your views here.
    return render(request,'haircut/home_page.html') 