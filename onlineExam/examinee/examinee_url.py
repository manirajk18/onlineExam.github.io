from django.urls import path
from examinee.views import *

urlpatterns=[
    path('new-examinee',newExaminee),
    path('examinee-signup/',examineeRegistration),
    path('examinee-login/',examineeLogin),
    path('examinee-LoginValidate',examineeLoginValidate),
    path('logout/',examineeLogout),
    path('exam/',examineeExam),
    path('result/',examineeResult),
]