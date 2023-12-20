from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView # 追加


'''トップページ'''
class TempView(generic.TemplateView):
    template_name = 'account/top.html'


'''追加'''
class Logout(LogoutView):
    template_name = 'account/logout_done.html'