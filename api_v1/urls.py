from django.urls import path

from api_v1.views import PackageDisplayView, SubscriberChargingRecordsView, SubscriberPackageRecordsView, \
    PackagesListView, CallSaleView, PinLessChargingNumberView, PackageCallSaleView, PackageActivationView

urlpatterns = [
    path('PackageDisplay/', PackageDisplayView.as_view(), name='packagedisplay'),
    path('SubscriberChargingRecords/', SubscriberChargingRecordsView.as_view(), name='subscriberchargingrecords'),
    path('SubscriberPackageRecords/', SubscriberPackageRecordsView.as_view(), name='subscriberpackagerecords'),
    path('PackagesList/', PackagesListView.as_view(), name='packageslist'),
    path('callsale/', CallSaleView.as_view(), name='callsale'),
    path('pinlesscharging/', PinLessChargingNumberView.as_view(), name='pinlessscharging'),
    path('packagecallsale/', PackageCallSaleView.as_view(), name='packagecallsale'),
    path('packageactivation/', PackageActivationView.as_view(), name='packageactivation'),

]
