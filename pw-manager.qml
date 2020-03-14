import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls 2.3
import QtQuick.Shapes 1.11
import QtQuick.Controls.Material 2.0

Window {
    visible: true
    width: 640
    height: 480
    title: qsTr("文字列ジェネレータ")
    color: "darkgrey"

        Button {
            id: button
            x: 113
            y: 35
            text: qsTr("生成")
        }
        Button {
            id: button1
            x: 450
            y: 35
            text: qsTr("クリア")
        }

    GroupBox {
        id: groupBox1
        x: 70
        y: 104
        width: 500
        height: 64
        title: qsTr("文字数指定")

        Row{
            width: 476
            height: 40
            anchors.centerIn: parent
            spacing: 70

            RadioButton {
                id: radioButton
                x: 9
                y: 3
                text: qsTr("8文字")
                checked: true
            }

            RadioButton {
                id: radioButton1
                x: 162
                y: 3
                text: qsTr("16文字")
            }

            RadioButton {
                id: radioButton2
                x: 334
                y: 3
                text: qsTr("24文字")
            }
        }
    }

    GroupBox {
        id: groupBox
        x: 70
        y: 186
        width: 500
        height: 100
        title: qsTr("条件指定")

        Row{
            width: 476
            height: 40
            anchors.verticalCenterOffset: -15
            anchors.horizontalCenterOffset: 0
            anchors.centerIn: parent
            spacing: 70

            CheckBox {
                id: checkBox
                x: 0
                y: 0
                text: qsTr("大文字")
            }
            CheckBox {
                id: checkBox1
                x: 369
                y: 0
                text: qsTr("記号")
            }
            CheckBox {
                id: checkBox3
                x: 189
                y: 0
                text: qsTr("数字")
            }
        }

        Row{
            width: 476
            height: 40
            anchors.verticalCenterOffset: 21
            anchors.horizontalCenterOffset: 0
            anchors.centerIn: parent
            spacing: 50

            RadioButton {
                id: radioButton3
                x: 189
                y: 0
                text: qsTr("文字始まり")
                checked: true
            }
            RadioButton {
                id: radioButton4
                x: 369
                y: 0
                text: qsTr("記号始まり")
            }
            RadioButton {
                id: radioButton5
                x: 0
                y: 0
                text: qsTr("数字始まり")
            }
        }
    }


    GroupBox {
        id: groupBox3
        x: 70
        y: 302
        width: 500
        height: 57
        title: qsTr("形式指定")

        Row{
            width: 476
            height: 40
            anchors.centerIn: parent
            spacing: 70

            RadioButton {
                id: radioButton6
                x: 0
                y: 5
                text: qsTr("なし")
                checked: true
            }
            RadioButton {
                id: radioButton7
                x: 192
                y: 5
                text: qsTr("ー形式")
            }
            RadioButton {
                id: radioButton8
                x: 373
                y: 5
                text: qsTr(".形式")
            }
        }
    }

    GroupBox {
        id: groupBox2
        x: 70
        y: 373
        width: 500
        height: 88
        title: qsTr("出力文字")

        Text {
            id: element
            x: 0
            y: 15
            width: 476
            height: 36
            text: qsTr("")
            font.pixelSize: 12
        }
    }

}
