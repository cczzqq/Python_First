# -*- coding: utf-8 -*-
__author__ = 'czq'
__date = '2017/10/14 14:24'
import xadmin
from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'city', 'add_time']
    search_fields = ['name', 'desc', 'city']
    list_filter = ['name', 'desc', 'city__name', 'add_time']
    # 当有一个外键指向这个类的时候，在后台显示不是下拉框，而是以ajax的形式的搜索框
    # relfield_style = 'fk-ajax'


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position']
    list_filter = ['org__name', 'name', 'work_years', 'work_company', 'work_position', 'add_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)