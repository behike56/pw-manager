# -*- coding: utf-8 -*-
"""\
PwGenerator Controller

Author:
    Hideo Tsujisaki

"""

__version__ = "0.1"
__author__ = "Hideo Tsujisaki"

import sys
from PySide2.QtCore import QUrl
from PySide2 import QtCore, QtWidgets, QtQml

from PwRandomizer import PwBuildCenter as pwr


class PwGenerator(QtCore.QObject):

    # def __init__(self, parent=None):
    #     super(PwGenerator, self).__init__(parent)
    def __init__(self):
        super().__init__()
        self.char_lim = 0
        self.condition = ""
        self.start_con = 0
        self.style = None

    @QtCore.Slot(int,
                 int,
                 int,
                 int,
                 int,
                 int,
                 int,
                 int,
                 int,
                 int,
                 int,
                 int,
                 result=str)
    def stateHandler(self, radEight, radSixte, radTwetFor, chbxUpper, chbxKigo,
                     chbxNumb, radMojiSta, radKigoSta, radNumbSta, radTypeNone,
                     radTypeHype, radTypeDott):
        # 文字数の設定
        if radEight == 1:
            self.char_lim = 8
        if radSixte == 1:
            self.char_lim = 16
        if radTwetFor == 1:
            self.char_lim = 24

        # 含める文字種の設定
        if chbxUpper == 2:
            self.condition += "A"
        if chbxKigo == 2:
            self.condition += "B"
        if chbxNumb == 2:
            self.condition += "C"

        # 始まりの文字指定の設定
        if radMojiSta == 1:
            self.start_con = "moji"
        if radKigoSta == 1:
            self.start_con = "kigo"
        if radNumbSta == 1:
            self.start_con = "numb"

        # パスワード形式の設定
        if radTypeNone == 1:
            pass
        if radTypeHype == 1:
            self.style = "hype"
        if radTypeDott == 1:
            self.style = "dott"

        result = pwr(self.char_lim, self.condition, self.start_con, self.style)
        return result


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    myconnect = PwGenerator()

    engine = QtQml.QQmlApplicationEngine()
    bind = engine.rootContext()
    bind.setContextProperty("PwGenerator", myconnect)

    engine.load(QUrl("pw-manager.qml"))

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())
