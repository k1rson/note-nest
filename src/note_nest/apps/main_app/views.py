from django.shortcuts import render

from django.views import View

class HomePageView(View):
    def get(self, request):
        return render(request, 'main_app/index_main.html')