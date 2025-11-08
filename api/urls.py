from django.urls import path

from api.views import FinalAnswerViewSet

urlpatterns = [
    path('get_second_part/', FinalAnswerViewSet.as_view({'post': "get_second_part"}), name="get_second_part"),
    path('get_final_answer/', FinalAnswerViewSet.as_view({'get': "get_final_answer"}), name="get_second_part")
]