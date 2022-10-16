from django.conf.urls import url

from payments import views

urlpatterns = [
    url('test-payment/', views.test_payment),
    url('save-stripe-info/', views.save_stripe_info),
    url('confirm-payment-intent/', views.confirm_payment_intent),

]
