# -*- coding: utf-8 -*-
__author__ = 'czq'
__date = '2017/10/14 13:29'

import xadmin
from xadmin import views

from .models import EmailVerifyRecord, Banner


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = u"后台管理系统"
    site_footer = u"慕学在线网"
    menu_style = "accordion" #左侧导航栏显示样式


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']
    # 设置后台图标
    model_icon = "fa fa-envelope"


class BannerAdmin(object):
    list_display = ['title', 'url', 'index', 'add_time']
    search_fields = ['title', 'url', 'index']
    list_filter = ['title', 'url', 'index', 'add_time']


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)