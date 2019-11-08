from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import paypalrestsdk
import logging

logging.basicConfig(level=logging.INFO)

paypalrestsdk.configure({
    'mode': 'sandbox',  # sandbox or live
    'client_id': 'ATNUMSsvOTPyIimF8XHVEwaBL_daevlVgolz0N65LCJ-a2JLYJYJIkLnL4FJzvD4f1sdo7KUC4YdORgB',
    'client_secret': 'ELrikiW_rOFFJ24DbXqIuAoBmhGc7qMH1Hva4R189jR7J_lB4topbllUtxvsE8FHLRNWyiFDvdhCwjZQ',
})


@api_view(['POST'])
def create_payment(request):
    """
    Create a payment object
    """
    print('rkmkc')
    print(request.data)
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        # Payer who funds the payment
        "payer": {
            "payment_method": "paypal"
        },
        # Set redirect urls
        "redirect_urls": {
            "return_url": "http://localhost:3000/process",
            "cancel_url": "http://localhost:3000/cancel"
        },
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": "item1",
                    "sku": "item1",
                    "price": "15.00",
                    "currency": "USD",
                    "quantity": 1
                }]
            },
            "amount": {
                "total": "15.00",
                "currency": "USD"
            },
            "description": "This is the payment transaction description"
        }]
    })

    # payment.create() returns a boolean True for success, False for err
    if payment.create():
        print("____PAYMENT_____", payment)
        # you have to return the paymentID to frontend and call resolve with it
        return Response({'paymentID': payment['id']}, status=status.HTTP_200_OK)
    else:
        print("Error while creating a payment: ", payment.error)
        return Response({"error_message": payment.error.get('message', '')},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def execute_payment(request):
    """
    Execute the payment to charge the customer
    """
    print('skmkc')
    print(request.data)
    # find the Payment by ID
    payment = paypalrestsdk.Payment.find(request.data.get('paymentID', ''))
    # Execute the payment using payer_id generated automatically by paypal
    if payment.execute({"payer_id": request.data.get('payerID', '')}):
        return Response({"message": "Your payment has been made successfully."},
                        status=status.HTTP_200_OK)
    else:
        print("_____ERROR___", payment.error)
        return Response({"message": "An Error has occured", "error": payment.error},
                        status=status.HTTP_400_BAD_REQUEST
                        )
