from django.shortcuts import render

def churncalculator(request):
    Customers_Lost = float(request.POST.get('CustLost', '0'))
    Initial_Customer = float(request.POST.get('InitCust', '0'))

    Churn_Rate = ( Customers_Lost / Initial_Customer) * 100 if request.method == 'POST' else 0

    print("Customer Lost =", Customers_Lost)
    print("Initial Customer =", Initial_Customer)
    print("Churn Rate =", Churn_Rate)

    return render(
        request,
        'myapp/hi.html',
        {
            'Customers_Lost': Customers_Lost, 
            'Initial_Customer': Initial_Customer, 
            'Churn_Rate': Churn_Rate
        }
    )

