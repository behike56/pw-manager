import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls 2.3

Window {
    visible: true
    width: 640
    height: 480
    title: qsTr("ぱすわーどジェネレータ")
    color: "darkgrey"

    Button {
        id: button
        x: 70
        y: 9
        text: qsTr("生成")
        onClicked: function(){
            passDisplay.text = PwGenerator.stateHandler(
                radEight.checked, radSixte.checked, radTwetFor.checked,
                chbxUpper.checkState, chbxKigo.checkState, chbxNumb.checkState,
                radMojiSta.checked, radKigoSta.checked, radNumbSta.checked,
                radTypeNone.checked, radTypeHype.checked, radTypeDott.checked)
        }
    }
    GroupBox {
        id: groupBox1
        x: 70
        y: 60
        width: 500
        height: 70
        title: qsTr("文字数指定")

        Row{
            width: 476
            height: 60
            anchors.centerIn: parent
            spacing: 55

            RadioDelegate {
                id: radEight
                x: 9
                y: 3
                text: qsTr("8文字")
                checked: true
            }

            RadioDelegate {
                id: radSixte
                x: 162
                y: 3
                text: qsTr("16文字")
            }

            RadioDelegate {
                id: radTwetFor
                x: 334
                y: 3
                text: qsTr("24文字")
            }
        }
    }

    GroupBox {
        id: groupBox
        x: 70
        y: 140
        width: 500
        height: 125
        title: qsTr("条件指定")

        Row{
            width: 476
            height: 60
            anchors.verticalCenterOffset: -15
            anchors.horizontalCenterOffset: 0
            anchors.centerIn: parent
            spacing: 70

            CheckBox {
                id: chbxUpper
                x: 0
                y: 0
                text: qsTr("大文字")
            }
            CheckBox {
                id: chbxKigo
                x: 369
                y: 0
                text: qsTr("記号")
            }
            CheckBox {
                id: chbxNumb
                x: 189
                y: 0
                text: qsTr("数字")
            }
        }

        Row{
            width: 476
            height: 60
            anchors.verticalCenterOffset: 21
            anchors.horizontalCenterOffset: 0
            anchors.centerIn: parent
            spacing: 35

            RadioDelegate {
                id: radMojiSta
                x: 189
                y: 0
                text: qsTr("文字始まり")
                checked: true
            }
            RadioDelegate {
                id: radKigoSta
                x: 369
                y: 0
                text: qsTr("記号始まり")
            }
            RadioDelegate {
                id: radNumbSta
                x: 0
                y: 0
                text: qsTr("数字始まり")
            }
        }
    }

    GroupBox {
        id: groupBox3
        x: 70
        y: 271
        width: 500
        height: 70
        title: qsTr("形式指定")

        Row{
            width: 476
            height: 60
            anchors.verticalCenterOffset: 3
            anchors.horizontalCenterOffset: 0
            anchors.centerIn: parent
            spacing: 70

            RadioDelegate {
                id: radTypeNone
                x: 0
                y: 5
                text: qsTr("なし")
                checked: true
            }
            RadioDelegate {
                id: radTypeHype
                x: 192
                y: 5
                text: qsTr("ー形式")
            }
            RadioDelegate {
                id: radTypeDott
                x: 373
                y: 5
                text: qsTr(".形式")
            }
        }
    }

    GroupBox {
        id: groupBox2
        x: 70
        y: 354
        width: 500
        height: 90
        title: qsTr("生成パスワード")
        TextEdit {
            id: passDisplay
            x: 100
            y: 5
            width: 480
            height: 40
            text: qsTr("")
            font.pixelSize: 20
        }
    }
}
