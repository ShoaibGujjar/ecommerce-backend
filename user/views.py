from rest_framework.permissions import BasePermission, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics, mixins,status
from rest_framework.response import Response
from django_mongodb.settings import EMAIL_HOST_USER
from .models import Product, OrderSummary, Status,OrderItem
from .serializers import OrderSummarySerializers, DetailProductSerializers
from rest_framework.decorators import api_view, permission_classes
from django.db.models.query_utils import Q
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
import os
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient

# from address we pass to our Mail object, edit with your name
FROM_EMAIL = 'shoaibgujjar948@gmail.com'

# update to your dynamic template id from the UI
TEMPLATE_ID = 'd-f4a282ddf74047bc93c7ab0784b561b3'

# list of emails and preheader names, update with yours
TO_EMAILS = [('sir.ihtesham@gmail.com', 'ihtesham')]
# TO_EMAILS = [('l191177@lhr.nu.edu.pk', 'ihtesham')]
@api_view(['GET','POST'])
def SendDynamic(request):
    # create Mail object and populate
    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=TO_EMAILS,
        # subject='A Test from SendGrid!',
        # html_content='<strong>Hello there from SendGrid your URL is: ' +
        # '<a href=''https://github.com/cyberjive''>right here!</a></strong>',
        )

    # pass custom values for our HTML placeholders
    message.dynamic_template_data = {
        "subject": 'SendGrid Development',
        "place": 'New York City',
        "event": 'Twilio Signal json data'
    }
    message.template_id = TEMPLATE_ID

    try:
        sg = SendGridAPIClient('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')
        response = sg.send(message)
    except Exception as e:
        print("Error: {0}".format(e))
    massage = {'mail send'}
    return Response(massage)


if __name__ == "__main__":
    SendDynamic()



class orderListCreateAPIView(generics.ListCreateAPIView):
    queryset = OrderSummary.objects.all()
    serializer_class = OrderSummarySerializers





@api_view(['POST'])
def Sendmail(request):
    msg = EmailMessage(
    from_email='shoaibgujjar948@gmail.com',
    to=TO_EMAILS,
    )
    msg.template_id = TEMPLATE_ID
    msg.dynamic_template_data = {
    "title": "foo"
    }
    msg.send(fail_silently=False)
    massage = {'mail send'}
    return Response(massage)


@api_view(['GET'])
def RelatedProductAPIView(request):
    """ fid the data accroging to queryset """
    data = request.data
    id = data['id']
    obj = get_object_or_404(Product, product_id=id)
    product = Product.objects.get(product_id=id)
    x = product.name.split(" ")
    print(x)
    for y in x:
        matches = Product.objects.filter(Q(name__icontains=y) |
                                         Q(description__icontains=y)).exclude(product_id=id)
        print(matches)
    data = DetailProductSerializers(matches, many=True).data
    return Response(data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addOrderItems(request):
    user = request.user
    data = request.data
    orderItems = data['cartItems']
    address=data['shipping']
    if orderItems and len(orderItems) == 0:
        return Response({'detail': 'No Order Items'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        # (1) create order
        order = OrderSummary.objects.create(
            name=data['shipping']['name'],
            email=data['shipping']['email'],
            phone=data['shipping']['phone'],
            postal_code=data['shipping']['postalCode'],
            address=data['shipping']['address'],
            totalAmount=data['cartTotalAmount'],
        )

        for i in orderItems:
            product = Product.objects.get(product_id=i['product_id'])
            item = OrderItem.objects.create(
                Product=product,
                order=order,
                name=product.name,
                qty=i['cartQuantity'],
                price=i['price'],
                image=i['image'][0]['image']     
            )

            product.countInStock -= item.qty
            product.save()
            # 
    serializer = OrderSummarySerializers(order, many=False)
    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=user.email,
        )


    # pass custom values for our HTML placeholders
    message.dynamic_template_data = {
        "subject": 'SendGrid Development',
        "place": 'New York City',
        "event": serializer.data
    }
    message.template_id = TEMPLATE_ID

    try:
        sg = SendGridAPIClient('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')
        response = sg.send(message)
    except Exception as e:
        print("Error: {0}".format(e))

    return Response(serializer.data)


@api_view(['POST'])
def ChangeOrderStatus(request):
    data = request.data
    id = data['id']
    status = data['status']
    # due to enum field we use else if conditions
    if status == 'PLASED':
        order = OrderSummary.objects.get(id=id)
        order.status = Status.PLASED
        order.save()
    elif status == 'CONFORMED':
        order = OrderSummary.objects.get(id=id)
        order.status = Status.CONFORMED
        order.save()
    elif status == 'DISPATCH':
        order = OrderSummary.objects.get(id=id)
        order.status = Status.DISPATCH
        order.save()
    return Response('status is changed')
