from app import models
from django import template
import datetime
register = template.Library()


@register.simple_tag
def get_snc():
    """
    云标签
    :return:
    """
    data = [{"label": i.name, "url": '/sort/'+str(i.id), "target": '_top'} for i in models.Classification.objects.all()]
    if not data:
        data = [{"label": "暂时无分类", "url": '#', "target": '_top'}, {"label": "请添加", "url": '#', "target": '_top'}]
    return data


@register.assignment_tag
def get_user_post():
    """
    统计用户
    :return:
    """
    post_number = models.Sitck.objects.count()
    user_number = models.User.objects.filter(is_active=0).count()
    return {'user_number': user_number, 'post_number': post_number}


@register.filter
def time_sub(time):
    """
    处理时间
    :param time:
    :return:
    """
    try:
        startTime= datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
        endTime= datetime.datetime.strptime(time.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
    except Exception as e:
        return 0
    data = startTime - endTime

    return "{}{}{}".format(str_int(data.days) + '天' if data.days else '',
                           str_int(data.seconds/3600) + '小时' if data.seconds/3600 else '',
                           str_int(data.seconds%3600/60) + "分钟前")


def str_int(num):
    """
    :param num:
    :return:
    """
    return str(int(num))
