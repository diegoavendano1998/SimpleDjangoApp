from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import stripe

# Create your views here.

secret = settings.STRIPE_SECRET_KEY
stripe.api_key = secret
@login_required
def checkout(request):
    publishKey = settings.STRIPE_PUBLISHABLE_KEY
    customer_id = (request.user.userstripe.stripe_id)
    if request.method == 'POST':
        # No trae el token con este flujo en versiones > 2.0
        token = request.POST['stripeToken']
        try:
            # Obtener la tejeta del cliente
            customer = stripe.Customer.retrieve(customer_id)
            customer.sources.create(source=token)
            # Data de la transaccion
            charge = stripe.Charge.create(
                amount      = 100,
                currency    = "usd",
                customer    = customer,
                description = "Some description"
            )
        except stripe.error.CardError as e:
            print ("Something happend")
    context = {'publichKey':publishKey}
    template = 'checkout.html'
    return render(request, template, context)
