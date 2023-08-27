from __future__ import absolute_import
from datetime import datetime  # Beacause celery. See: https://
import importlib
import sys
import os


def str_to_list(str_list=''):
    var_list = []
    if str_list:
        if ',' in str_list:
            values_list = str_list.split(',')
            var_list = [x.strip() for x in values_list]
        else:
            var_list.append(str_list)

    return var_list


def str_to_class(classname):
    list_dir = [x for x in os.listdir(sys.path[0]+"/apps")]
    for _path in list_dir:
        if "__" not in _path:
            path = f"apps.{_path}.models"
            i = importlib.import_module(path)
        if getattr(i, classname, None):
            return getattr(i, classname)


def str_to_date(dt):

    result = datetime.now()
    try:
        try:
            result = datetime.strptime(dt, "%Y-%m-%d")
        except Exception:
            result = datetime.strptime(dt, "%d-%m-%Y")
    except Exception:
        try:
            result = datetime.strptime(dt, "%Y/%m/%d")
        except Exception:
            result = datetime.strptime(dt, "%d/%m/%Y")

    return result
