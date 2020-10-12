class SuperLineageObj:
    def __init__(self, lineage_obj, update_time):
        self._lineage_obj = lineage_obj
        self._update_time = update_time
        self._added_info = None

    @property
    def lineage_obj(self):
        return self._lineage_obj

    @property
    def added_info(self):
        return self._added_info

    @added_info.setter
    def added_info(self, added_info):
        self._added_info = added_info

    @property
    def update_time(self):
        return self._update_time


import time

obj = SuperLineageObj("abc", time.time())
obj.added_info = {"tag": 1}
print(obj.added_info)


class A:
    """1"""
    def __init__(self, a: dict):
        self._obj = a

