# coding=utf-8
from django.contrib.auth.decorators import login_required


# 我使用的django 1.11 的版本 ,已经内置了限制对登录用户的访问类 from django.contrib.auth.mixins import LoginRequiredMixin
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        # 调用父类的as_view
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)
