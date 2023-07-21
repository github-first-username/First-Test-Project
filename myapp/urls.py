from django.urls import path
from myapp.views import all_product, completed_product, waiting_product


urlpatterns = [
    path('all-product/', all_product),
    path('completed_product/', completed_product),
    path('waiting_product/', waiting_product),

]