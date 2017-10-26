# -*- coding: utf-8 -*-
__author__ = 'czq'
__date = '2017/10/14 13:51'
import xadmin
from .models import Course, Lesson, Video, CourseResource, BannerCourse


# 这样做实现了在编辑课程的时候可以顺便编辑章节，但是不能再往下嵌套一层，即不能再编辑视频
# class LessonInline(object):
#     model = Lesson
#     extra = 0


# class CourseResourceInline(object):
#     model = CourseResource
#     extra = 0


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'add_time']
    search_fields = ['name', 'desc', 'detail', 'degree']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'add_time']
    # 设置后台查看时的排序
    ordering = ['-click_nums']
    # 设置某些字段在后台查看时为只读
    # readonly_fields = ['click_nums']
    # 设置某些字段在后台是隐藏的，这个属性和readonly_fields会冲突，所以不能同时设置一个字段
    # exclude = ['fav_nums']
    # inlines = [LessonInline, CourseResourceInline]
    # 设置的字段可以在列表页直接修改
    # list_editable = ['degree', 'desc']
    # 设置定时刷新列表页，这样设置为可选的每3秒或每5秒
    # refresh_times = [3, 5]
    # 指明某个字段使用什么样式
    style_fields = {"detail": "ueditor"}

    # 过滤数据
    # def queryset(self):
    #     qs = super(CourseAdmin, self).queryset()
    #     qs = qs.filter(is_banner=False)
    #     return qs

    # 在保存课程的时候统计课程机构的课程数，不需要手动修改
    # def save_models(self):
        # obj = self.new_obj
        # obj.save()
        # if obj.course_org is not None:
            # course_org = obj.course_org
            # course_org.course_nums = Course.objects.filter(course_org=course_org)
            # course_org.save()


# class BannerCourseAdmin(object):
    # list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'add_time']
    # search_fields = ['name', 'desc', 'detail', 'degree']
    # list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'add_time']
    # 设置后台查看时的排序
    # ordering = ['-click_nums']
    # 设置某些字段在后台查看时为只读
    # readonly_fields = ['click_nums']
    # 设置某些字段在后台是隐藏的，这个属性和readonly_fields会冲突，所以不能同时设置一个字段
    # exclude = ['fav_nums']
    # inlines = [LessonInline, CourseResourceInline]

    # 过滤数据
    # def queryset(self):
        # qs = super(BannerCourseAdmin, self).queryset()
        # qs = qs.filter(is_banner=True)
        # return qs


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson__name', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


xadmin.site.register(Course, CourseAdmin)
# xadmin.site.register(BannerCourse, BannerCourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)