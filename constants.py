# -*- coding: utf-8 -*-
"""\
定数モジュール
"""

__version__ = "0.1"
__author__ = "Hideo Tsujisaki"


class _Constants(object):
    class ConstError(TypeError):
        pass

    def __repr__(self):
        return "定数型の定義。"

    def __setattr__(self, const_name, value):
        if const_name in self.__dict__:
            raise self.ConstError("定数には再代入できません。 (%s)" % const_name)
        self.__dict__[const_name] = value

    def __del__(self):
        self.__dict__.clear()
