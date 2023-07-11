from django.urls import re_path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'api-traceability'

urlpatterns = [

     re_path('traceability_list/', 
          views.traceabilityList.as_view(), 
          name='traceabilityList'),

     re_path('traceability_post/', 
          views.traceabilityPost.as_view(), 
          name='traceabilityPost'),
          
     re_path('ScannerDataSerilisersAPIView',
          views.ScannerDataSerilisersAPIView.as_view(),
          name='ScannerDataSerilisersAPIView'),

     re_path('ScannerDataSerilisersDetail/<int:id>/',
          views.ScannerDataSerilisersDetail.as_view(),
          name='ScannerDataSerilisersDetail'),
    
]

