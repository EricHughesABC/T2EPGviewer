# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'epg_fit_parameters_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import lmfit as lm

from PyQt5 import QtCore, QtGui, QtWidgets

class EpgT2paramsDialog(object):

    def __init__(self, lmparams):

        self.lmparams = lmparams

        self.params = self.lmparams['epgt2fitparams']



    def setupEpgT2paramsDialog(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(386, 284)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(60, 250, 321, 23))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 10, 361, 231))

        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.setObjectName("gridLayout")
        self.fatT1value = QtWidgets.QLineEdit(self.widget)
        self.fatT1value.setValidator(QtGui.QDoubleValidator())
        self.fatT1value.setObjectName("fatT1value")
        self.gridLayout.addWidget(self.fatT1value, 7, 1, 1, 1)

        self.muscleFractionMax = QtWidgets.QLineEdit(self.widget)
        self.muscleFractionMax.setValidator(QtGui.QDoubleValidator())
        self.muscleFractionMax.setObjectName("muscleFractionMax")
        self.gridLayout.addWidget(self.muscleFractionMax, 3, 3, 1, 1)

        self.optimizeMuscleFraction = QtWidgets.QCheckBox(self.widget)
        self.optimizeMuscleFraction.setText("")
        self.optimizeMuscleFraction.setChecked(True)
        self.optimizeMuscleFraction.setObjectName("optimizeMuscleFraction")
        self.gridLayout.addWidget(self.optimizeMuscleFraction, 3, 4, 1, 1)

        self.fatFractionMin = QtWidgets.QLineEdit(self.widget)
        self.fatFractionMin.setValidator(QtGui.QDoubleValidator())
        self.fatFractionMin.setObjectName("fatFractionMin")
        self.gridLayout.addWidget(self.fatFractionMin, 4, 2, 1, 1)

        self.fatFractionMax = QtWidgets.QLineEdit(self.widget)
        self.fatFractionMax.setValidator(QtGui.QDoubleValidator())
        self.fatFractionMax.setObjectName("fatFractionMax")
        self.gridLayout.addWidget(self.fatFractionMax, 4, 3, 1, 1)

        self.b1scaleMax = QtWidgets.QLineEdit(self.widget)
        self.b1scaleMax.setValidator(QtGui.QDoubleValidator())
        self.b1scaleMax.setObjectName("b1scaleMax")
        self.gridLayout.addWidget(self.b1scaleMax, 5, 3, 1, 1)

        self.muscleFractionMin = QtWidgets.QLineEdit(self.widget)
        self.muscleFractionMin.setValidator(QtGui.QDoubleValidator())
        self.muscleFractionMin.setObjectName("muscleFractionMin")
        self.gridLayout.addWidget(self.muscleFractionMin, 3, 2, 1, 1)

        self.b1scaleValue = QtWidgets.QLineEdit(self.widget)
        self.b1scaleValue.setValidator(QtGui.QDoubleValidator())
        self.b1scaleValue.setObjectName("b1scaleValue")
        self.gridLayout.addWidget(self.b1scaleValue, 5, 1, 1, 1)

        self.b1scaleMin = QtWidgets.QLineEdit(self.widget)
        self.b1scaleMin.setValidator(QtGui.QDoubleValidator())
        self.b1scaleMin.setObjectName("b1scaleMin")
        self.gridLayout.addWidget(self.b1scaleMin, 5, 2, 1, 1)

        self.fatFractionLabel = QtWidgets.QLabel(self.widget)
        self.fatFractionLabel.setObjectName("fatFractionLabel")
        self.gridLayout.addWidget(self.fatFractionLabel, 4, 0, 1, 1)

        self.fatFractionValue = QtWidgets.QLineEdit(self.widget)
        self.fatFractionValue.setValidator(QtGui.QDoubleValidator())
        self.fatFractionValue.setObjectName("fatFractionValue")
        self.gridLayout.addWidget(self.fatFractionValue, 4, 1, 1, 1)

        self.muscleT1label = QtWidgets.QLabel(self.widget)
        self.muscleT1label.setObjectName("muscleT1label")
        self.gridLayout.addWidget(self.muscleT1label, 6, 0, 1, 1)

        self.fatT2min = QtWidgets.QLineEdit(self.widget)
        self.fatT2min.setValidator(QtGui.QDoubleValidator())
        self.fatT2min.setObjectName("fatT2min")
        self.gridLayout.addWidget(self.fatT2min, 2, 2, 1, 1)

        self.maxHeadingLabel = QtWidgets.QLabel(self.widget)
        self.maxHeadingLabel.setObjectName("maxHeadingLabel")
        self.gridLayout.addWidget(self.maxHeadingLabel, 0, 3, 1, 1)

        self.minHeadingLabel = QtWidgets.QLabel(self.widget)
        self.minHeadingLabel.setObjectName("minHeadingLabel")
        self.gridLayout.addWidget(self.minHeadingLabel, 0, 2, 1, 1)

        self.valueHeadingLabel = QtWidgets.QLabel(self.widget)
        self.valueHeadingLabel.setObjectName("valueHeadingLabel")
        self.gridLayout.addWidget(self.valueHeadingLabel, 0, 1, 1, 1)

        self.fatT2value = QtWidgets.QLineEdit(self.widget)
        self.fatT2value.setValidator(QtGui.QDoubleValidator())
        self.fatT2value.setObjectName("fatT2value")
        self.gridLayout.addWidget(self.fatT2value, 2, 1, 1, 1)

        self.optimizeFatT2 = QtWidgets.QCheckBox(self.widget)
        self.optimizeFatT2.setText("")
        self.optimizeFatT2.setChecked(False)
        self.optimizeFatT2.setObjectName("optimizeFatT2")
        self.gridLayout.addWidget(self.optimizeFatT2, 2, 4, 1, 1)

        self.muscleT2value = QtWidgets.QLineEdit(self.widget)
        self.muscleT2value.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.muscleT2value.setProperty("muscleValue", 0.0)
        self.muscleT2value.setProperty("number", 35.0)
        self.muscleT2value.setObjectName("muscleT2value")
        self.gridLayout.addWidget(self.muscleT2value, 1, 1, 1, 1)

        self.fatT2label = QtWidgets.QLabel(self.widget)
        self.fatT2label.setObjectName("fatT2label")
        self.gridLayout.addWidget(self.fatT2label, 2, 0, 1, 1)

        self.fatT2max = QtWidgets.QLineEdit(self.widget)
        self.fatT2max.setValidator(QtGui.QDoubleValidator())
        self.fatT2max.setObjectName("fatT2max")
        self.gridLayout.addWidget(self.fatT2max, 2, 3, 1, 1)

        self.muscleT2max = QtWidgets.QLineEdit(self.widget)
        self.muscleT2max.setValidator(QtGui.QDoubleValidator())
        self.muscleT2max.setObjectName("muscleT2max")
        self.gridLayout.addWidget(self.muscleT2max, 1, 3, 1, 1)

        self.opimizedHeadingLabel = QtWidgets.QLabel(self.widget)
        self.opimizedHeadingLabel.setObjectName("opimizedHeadingLabel")
        self.gridLayout.addWidget(self.opimizedHeadingLabel, 0, 4, 1, 1)

        self.muscleT2label = QtWidgets.QLabel(self.widget)
        self.muscleT2label.setObjectName("muscleT2label")
        self.gridLayout.addWidget(self.muscleT2label, 1, 0, 1, 1)

        self.muscleT2min = QtWidgets.QLineEdit(self.widget)
        self.muscleT2min.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.muscleT2min.setObjectName("muscleT2min")
        self.gridLayout.addWidget(self.muscleT2min, 1, 2, 1, 1)

        self.optimizeMuscleT2 = QtWidgets.QCheckBox(self.widget)
        self.optimizeMuscleT2.setText("")
        self.optimizeMuscleT2.setChecked(True)
        self.optimizeMuscleT2.setObjectName("optimizeMuscleT2")
        self.gridLayout.addWidget(self.optimizeMuscleT2, 1, 4, 1, 1)

        self.optimizeB1scale = QtWidgets.QCheckBox(self.widget)
        self.optimizeB1scale.setText("")
        self.optimizeB1scale.setChecked(True)
        self.optimizeB1scale.setObjectName("optimizeB1scale")
        self.gridLayout.addWidget(self.optimizeB1scale, 5, 4, 1, 1)

        self.optimizeFatFraction = QtWidgets.QCheckBox(self.widget)
        self.optimizeFatFraction.setText("")
        self.optimizeFatFraction.setChecked(True)
        self.optimizeFatFraction.setObjectName("optimizeFatFraction")
        self.gridLayout.addWidget(self.optimizeFatFraction, 4, 4, 1, 1)

        self.b1scaleLabel = QtWidgets.QLabel(self.widget)
        self.b1scaleLabel.setObjectName("b1scaleLabel")
        self.gridLayout.addWidget(self.b1scaleLabel, 5, 0, 1, 1)

        self.muscleT1value = QtWidgets.QLineEdit(self.widget)
        self.muscleT1value.setObjectName("muscleT1value")
        self.gridLayout.addWidget(self.muscleT1value, 6, 1, 1, 1)

        self.T2echoValue = QtWidgets.QLineEdit(self.widget)
        self.T2echoValue.setValidator(QtGui.QDoubleValidator())
        self.T2echoValue.setObjectName("T2echoValue")
        self.gridLayout.addWidget(self.T2echoValue, 8, 1, 1, 1)

        self.muscleFractionValue = QtWidgets.QLineEdit(self.widget)
        self.muscleFractionValue.setValidator(QtGui.QDoubleValidator())
        self.muscleFractionValue.setObjectName("muscleFractionValue")
        self.gridLayout.addWidget(self.muscleFractionValue, 3, 1, 1, 1)

        self.muscleFractionLabel = QtWidgets.QLabel(self.widget)
        self.muscleFractionLabel.setObjectName("muscleFractionLabel")
        self.gridLayout.addWidget(self.muscleFractionLabel, 3, 0, 1, 1)

        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 8, 0, 1, 1)

        self.fatT1label = QtWidgets.QLabel(self.widget)
        self.fatT1label.setObjectName("fatT1label")
        self.gridLayout.addWidget(self.fatT1label, 7, 0, 1, 1)



        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.dialog_ok_clicked)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "EPG"))
        self.fatT1value.setText(_translate("Dialog", "1450"))
        self.muscleFractionMax.setText(_translate("Dialog", "10"))
        self.fatFractionMin.setText(_translate("Dialog", "0"))
        self.fatFractionMax.setText(_translate("Dialog", "10"))
        self.b1scaleMax.setText(_translate("Dialog", "2"))
        self.muscleFractionMin.setText(_translate("Dialog", "0"))
        self.b1scaleValue.setText(_translate("Dialog", "1"))
        self.b1scaleMin.setText(_translate("Dialog", "0"))
        self.fatFractionLabel.setText(_translate("Dialog", "Fat Fraction"))
        self.fatFractionValue.setText(_translate("Dialog", ".3"))
        self.muscleT1label.setText(_translate("Dialog", "<html><head/><body><p>Muscle T<span style=\" vertical-align:sub;\">1</span> (ms)</p></body></html>"))
        self.fatT2min.setText(_translate("Dialog", "0"))
        self.maxHeadingLabel.setText(_translate("Dialog", "maximum"))
        self.minHeadingLabel.setText(_translate("Dialog", "minimum"))
        self.valueHeadingLabel.setText(_translate("Dialog", "value"))
        self.fatT2value.setText(_translate("Dialog", "200"))
        self.muscleT2value.setText(_translate("Dialog", "35"))
        self.fatT2label.setText(_translate("Dialog", "<html><head/><body><p>Fat T<span style=\" vertical-align:sub;\">2</span> (ms)</p></body></html>"))
        self.fatT2max.setText(_translate("Dialog", "2000"))
        self.muscleT2max.setText(_translate("Dialog", "150"))
        self.opimizedHeadingLabel.setText(_translate("Dialog", "optimized"))
        self.muscleT2label.setText(_translate("Dialog", "<html><head/><body><p>Muscle T<span style=\" vertical-align:sub;\">2</span> (ms)</p></body></html>"))
        self.muscleT2min.setText(_translate("Dialog", "0"))
        self.b1scaleLabel.setText(_translate("Dialog", "B<sub>1</sub> scale"))
        self.muscleT1value.setText(_translate("Dialog", "500"))
        self.T2echoValue.setText(_translate("Dialog", "10"))
        self.muscleFractionValue.setText(_translate("Dialog", "0.7"))
        self.muscleFractionLabel.setText(_translate("Dialog", "Muscle Fraction"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p>T<span style=\" vertical-align:sub;\">2</span> Echo (ms)</p></body></html>"))
        self.fatT1label.setText(_translate("Dialog", "<html><head/><body><p>Fat T<span style=\" vertical-align:sub;\">1</span> (ms)</p></body></html>"))

    def dialog_ok_clicked(self):
        print("dialog_ok_clicked")
        self.Dialog.setResult(1)
        worked =self.get_fitparameters()
        if worked:
            self.params.pretty_print()
            self.Dialog.accept()



    def get_fitparameters( self ):

        print("self.optimizeFatFraction.isChecked()", self.optimizeFatFraction.isChecked() )

        #epgt2fitparams = lm.Parameters()
        worked = True
        try:

            self.params.add(name='T2muscle', value = float(self.muscleT2value.text()),
                                                min   = float(self.muscleT2min.text()),
                                                max   = float(self.muscleT2max.text()),
                                                vary  = self.optimizeMuscleT2.isChecked())

            self.params.add(name='T2fat',    value = float(self.fatT2value.text()),
                                                min   = float(self.fatT2min.text()),
                                                max   = float(self.fatT2max.text()),
                                                vary  = self.optimizeFatT2.isChecked())

            self.params.add(name='Amuscle',  value = float(self.muscleFractionValue.text()),
                                                min   = float(self.muscleFractionMin.text()),
                                                max   = float(self.muscleFractionMax.text()),
                                                vary  = self.optimizeMuscleFraction.isChecked())

            self.params.add(name='Afat',    value  = float(self.fatFractionValue.text()),
                                               min    = float(self.fatFractionMin.text()),
                                               max    = float(self.fatFractionMax.text()),
                                               vary   = self.optimizeFatFraction.isChecked())

            self.params.add(name='B1scale',    value  = float(self.b1scaleValue.text()),
                                               min    = float(self.b1scaleMin.text()),
                                               max    = float(self.b1scaleMax.text()),
                                               vary   = self.optimizeB1scale.isChecked())

            self.params.add(name='T1muscle', value = float(self.muscleT1value.text()),
                                                vary  = False)

            self.params.add(name='T1fat',  value   = float(self.fatT1value.text()),
                                              vary    = False)

            self.params.add(name='echo',  value   = float(self.T2echoValue.text()),
                                              vary    = False)

            buttonsChecked = [not self.optimizeFatFraction.isChecked(),
                              not self.optimizeMuscleFraction.isChecked(),
                              not self.optimizeMuscleT2.isChecked(),
                              not self.optimizeFatT2.isChecked(),
                              not self.optimizeB1scale.isChecked()]

            print(buttonsChecked)

            if all(buttonsChecked):
                worked=False

            self.lmparams['epgt2fitparams'] = self.params
        except:

            worked = False
        return  worked


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    Dialog.setModal(False)

    lmparams = {}
    epgt2fitparams = lm.Parameters()

    epgt2fitparams.add('T2fat',    value = 180.0, min=0, max=5000, vary=False)
    epgt2fitparams.add('T2muscle', value = 35,    min=0, max=100,  vary=True )
    epgt2fitparams.add('Afat',     value = 0.01,  min=0, max=10,   vary=True )
    epgt2fitparams.add('Amuscle',  value = 0.1,   min=0, max=10,   vary=True )
    epgt2fitparams.add('T1fat',    value = 365.0,                  vary=False)
    epgt2fitparams.add('T1muscle', value = 1400,                   vary=False)
    epgt2fitparams.add('echo',     value = 10.0,                   vary=False)
    epgt2fitparams.add('B1scale',     value = 1.0, min=0, max=2,    vary=True)

    lmparams['epgt2fitparams']=epgt2fitparams

    ui = EpgT2paramsDialog(lmparams)
    ui.setupEpgT2paramsDialog(Dialog)
    rt=Dialog.open()
    print("Dialog.result() =",Dialog.result())

    #print( "get_fitparameters(ui).items()", ui.get_fitparameters().items())
    sys.exit(app.exec_())

