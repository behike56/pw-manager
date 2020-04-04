# -*- coding: utf-8 -*-
"""\
PwGenerator main logic

Author:
    Hideo Tsujisaki
"""

import sys
import os
from PySide2.QtCore import QUrl
from PySide2 import QtCore, QtWidgets, QtQml

import pw-randomizer as pwr


class PwGenerator(QtCore.QObject):
    def __init__(self, parent=None):
        super(PwGenerator, self).__init__(parent)
        self.moji_num = 0
        self.condition_oomoji = False
        self.condition_kigou = False
        self.condition_suuji = False
        self.moji_hajimari = 0


if __name__ == '__main__':
    os.environ["QT_QUICK_CONTROLS_STYLE"] = "Material.Indigo"
    app = QtWidgets.QApplication(sys.argv)
    pw_generator = PwGenerator()

    engine = QtQml.QQmlApplicationEngine()
    ctx = engine.rootContext()
    ctx.setContextProperty("Connect", pw_generator)
    engine.load(QUrl("pw-manager.qml"))

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())
