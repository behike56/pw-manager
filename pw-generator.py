# -*- coding: utf-8 -*-
"""\
pw-manager ロジック部分

Author:
    Hideo Tsujisaki
"""

import sys
import os
from PySide2.QtCore import QUrl
from PySide2 import QtCore, QtWidgets, QtQml


class PwGenerator(QtCore.QObject):
    def __init__(self, parent=None):
        super(PwGenerator, self).__init__(parent)


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
