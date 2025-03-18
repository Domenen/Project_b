import datetime
from django import template

register = template.Library()

@register.filter(name="splitl")
def splitl_func(value: str):
    return value.replace("_", " ")

def splitlvl_func(value: str, rplv: str):
    return value.replace(rplv, " ")

register.filter("split_vl", splitlvl_func)

@register.simple_tag(name="current_time")
def current_time(format_string):
    return "Текущее время" + str(datetime.datetime.now().strftime(format_string))

def now_time():
    return datetime.datetime.now()

register.simple_tag(now_time, name="now")