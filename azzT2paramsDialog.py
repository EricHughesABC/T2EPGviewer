# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'azz_fit_parameters_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class AzzT2paramsDialog(object):


    def __init__(self, lmparams):

        self.lmparams = lmparams
        self.params = self.lmparams['azzt2fitparams']


    def setupAzzT2paramsDialog(self, Dialog):
        self.dialog = Dialog
        Dialog.setObjectName("Azzabou")
        Dialog.resize(398, 335)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(230, 280, 156, 23))

        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 361, 252))

        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.setObjectName("gridLayout")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 7, 0, 1, 1)

        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 8, 0, 1, 1)

        self.echoTimeValue = QtWidgets.QLineEdit(self.layoutWidget)
        self.echoTimeValue.setValidator(QtGui.QDoubleValidator())
        self.echoTimeValue.setObjectName("echoTimeValue")
        self.gridLayout.addWidget(self.echoTimeValue, 8, 1, 1, 1)

        self.longFatT2value = QtWidgets.QLineEdit(self.layoutWidget)
        self.longFatT2value.setValidator(QtGui.QDoubleValidator())
        self.longFatT2value.setObjectName("longFatT2value")
        self.gridLayout.addWidget(self.longFatT2value, 6, 1, 1, 1)

        self.shortFatT2value = QtWidgets.QLineEdit(self.layoutWidget)
        self.shortFatT2value.setValidator(QtGui.QDoubleValidator())
        self.shortFatT2value.setObjectName("shortFatT2value")
        self.gridLayout.addWidget(self.shortFatT2value, 7, 1, 1, 1)

        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)

        self.muscleT2minimum = QtWidgets.QLineEdit(self.layoutWidget)
        self.muscleT2minimum.setValidator(QtGui.QDoubleValidator())
        self.muscleT2minimum.setObjectName("muscleT2minimum")
        self.gridLayout.addWidget(self.muscleT2minimum, 1, 2, 1, 1)

        self.fatFractionMinimum = QtWidgets.QLineEdit(self.layoutWidget)
        self.fatFractionMinimum.setValidator(QtGui.QDoubleValidator())
        self.fatFractionMinimum.setObjectName("fatFractionMinimum")
        self.gridLayout.addWidget(self.fatFractionMinimum, 3, 2, 1, 1)

        self.fatFractionMaximum = QtWidgets.QLineEdit(self.layoutWidget)
        self.fatFractionMaximum.setValidator(QtGui.QDoubleValidator())
        self.fatFractionMaximum.setObjectName("fatFractionMaximum")
        self.gridLayout.addWidget(self.fatFractionMaximum, 3, 3, 1, 1)

        self.muscleFractionMinimum = QtWidgets.QLineEdit(self.layoutWidget)
        self.muscleFractionMinimum.setValidator(QtGui.QDoubleValidator())
        self.muscleFractionMinimum.setObjectName("muscleFractionMinimum")
        self.gridLayout.addWidget(self.muscleFractionMinimum, 2, 2, 1, 1)

        self.optimizeMuscleFraction = QtWidgets.QCheckBox(self.layoutWidget)
        self.optimizeMuscleFraction.setText("")
        self.optimizeMuscleFraction.setChecked(True)
        self.optimizeMuscleFraction.setObjectName("optimizeMuscleFraction")
        self.gridLayout.addWidget(self.optimizeMuscleFraction, 2, 4, 1, 1)

        self.muscleFractionMaximum = QtWidgets.QLineEdit(self.layoutWidget)
        self.muscleFractionMaximum.setValidator(QtGui.QDoubleValidator())
        self.muscleFractionMaximum.setObjectName("muscleFractionMaximum")
        self.gridLayout.addWidget(self.muscleFractionMaximum, 2, 3, 1, 1)

        self.optimizeFatFraction = QtWidgets.QCheckBox(self.layoutWidget)
        self.optimizeFatFraction.setText("")
        self.optimizeFatFraction.setChecked(True)
        self.optimizeFatFraction.setObjectName("optimizeFatFraction")
        self.gridLayout.addWidget(self.optimizeFatFraction, 3, 4, 1, 1)

        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)

        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)

        self.optimizeMuscleT2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.optimizeMuscleT2.setText("")
        self.optimizeMuscleT2.setChecked(True)
        self.optimizeMuscleT2.setObjectName("optimizeMuscleT2")
        self.gridLayout.addWidget(self.optimizeMuscleT2, 1, 4, 1, 1)

        self.fatFractionLongT2value = QtWidgets.QLineEdit(self.layoutWidget)
        self.fatFractionLongT2value.setValidator(QtGui.QDoubleValidator())
        self.fatFractionLongT2value.setObjectName("fatFractionLongT2value")
        self.gridLayout.addWidget(self.fatFractionLongT2value, 4, 1, 1, 1)

        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 4, 1, 1)

        self.muscleT2value = QtWidgets.QLineEdit(self.layoutWidget)
        self.muscleT2value.setObjectName("muscleT2value")
        self.gridLayout.addWidget(self.muscleT2value, 1, 1, 1, 1)

        self.fatFractionShortT2value = QtWidgets.QLineEdit(self.layoutWidget)
        self.fatFractionShortT2value.setValidator(QtGui.QDoubleValidator())
        self.fatFractionShortT2value.setObjectName("fatFractionShortT2value")
        self.gridLayout.addWidget(self.fatFractionShortT2value, 5, 1, 1, 1)

        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 1)

        self.muscleT2maximum = QtWidgets.QLineEdit(self.layoutWidget)
        self.muscleT2maximum.setValidator(QtGui.QDoubleValidator())
        self.muscleT2maximum.setObjectName("muscleT2maximum")
        self.gridLayout.addWidget(self.muscleT2maximum, 1, 3, 1, 1)

        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 6, 0, 1, 1)

        self.muscleFractionValue = QtWidgets.QLineEdit(self.layoutWidget)
        self.muscleFractionValue.setValidator(QtGui.QDoubleValidator())
        self.muscleFractionValue.setObjectName("muscleFractionValue")
        self.gridLayout.addWidget(self.muscleFractionValue, 2, 1, 1, 1)

        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.fatFractionValue = QtWidgets.QLineEdit(self.layoutWidget)
        self.fatFractionValue.setValidator(QtGui.QDoubleValidator())
        self.fatFractionValue.setObjectName("fatFractionValue")
        self.gridLayout.addWidget(self.fatFractionValue, 3, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.dialog_ok_clicked)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Azzabou", "Azzabout T2 model"))
        self.label_11.setText(_translate("Azzabou", "Short Fat T<sub>2</sub> (ms)"))
        self.label_12.setText(_translate("Azzabou", "Echo Time (ms)"))
        self.echoTimeValue.setText(_translate("Azzabou", "10.0"))
        self.longFatT2value.setText(_translate("Azzabou", "250.0"))
        self.shortFatT2value.setText(_translate("Azzabou", "43.0"))
        self.label_2.setText(_translate("Azzabou", "minimum"))
        self.label_3.setText(_translate("Azzabou", "maximum"))
        self.muscleT2minimum.setText(_translate("Azzabou", "0.0"))
        self.fatFractionMinimum.setText(_translate("Azzabou", "0.0"))
        self.fatFractionMaximum.setText(_translate("Azzabou", "10.0"))
        self.muscleFractionMinimum.setText(_translate("Azzabou", "0.0"))
        self.muscleFractionMaximum.setText(_translate("Azzabou", "10.0"))
        self.label_7.setText(_translate("Azzabou", "Fat Fraction"))
        self.label_8.setText(_translate("Azzabou", "Fat Fraction (Long T<sub>2</sub>)"))
        self.fatFractionLongT2value.setText(_translate("Azzabou", "0.6"))
        self.label_4.setText(_translate("Azzabou", "optimized"))
        self.muscleT2value.setText(_translate("Azzabou", "35.0"))
        self.fatFractionShortT2value.setText(_translate("Azzabou", "0.4"))
        self.label_5.setText(_translate("Azzabou", "Muscle  T<sub>2</sub> (ms)"))
        self.label_6.setText(_translate("Azzabou", "Muscle Fraction"))
        self.label_9.setText(_translate("Azzabou", "Fat Fraction (Short T<sub>2</sub>)"))
        self.muscleT2maximum.setText(_translate("Azzabou", "100.0"))
        self.label_10.setText(_translate("Azzabou", "Long Fat T<sub>2</sub> (ms)"))
        self.muscleFractionValue.setText(_translate("Azzabou", "0.8"))
        self.label.setText(_translate("Azzabou", "value"))
        self.fatFractionValue.setText(_translate("Azzabou", "0.2"))



    def dialog_ok_clicked(self):
        print("dialog_ok_clicked")
        self.dialog.setResult(1)
        worked =self.get_fitparameters()
        if worked:
            self.params.pretty_print()
            self.dialog.accept()


    def get_fitparameters( self ):

        print("self.optimizeFatFraction.isChecked()", self.optimizeFatFraction.isChecked() )

        #epgt2fitparams = lm.Parameters()
        worked = True
        try:

            self.params.add(name='T2muscle',    value = float(self.muscleT2value.text()),
                                                min   = float(self.muscleT2minimum.text()),
                                                max   = float(self.muscleT2maximum.text()),
                                                vary  = self.optimizeMuscleT2.isChecked())

            self.params.add(name='Amuscle',     value = float(self.muscleFractionValue.text()),
                                                min   = float(self.muscleFractionMinimum.text()),
                                                max   = float(self.muscleFractionMaximum.text()),
                                                vary  = self.optimizeMuscleFraction.isChecked())

            self.params.add(name='Afat',    value     = float(self.fatFractionValue.text()),
                                               min    = float(self.fatFractionMinimum.text()),
                                               max    = float(self.fatFractionMaximum.text()),
                                               vary   = self.optimizeFatFraction.isChecked())

            self.params.add(name='c_l',   value=float(self.fatFractionLongT2value.text()), vary=False)
            self.params.add(name='c_s',   value=float(self.fatFractionShortT2value.text()), vary=False)
            self.params.add(name='t2_fl', value=float(self.longFatT2value.text()), vary=False)
            self.params.add(name='t2_fs', value=float(self.shortFatT2value.text()), vary=False)
            self.params.add(name='echo',  value=float(self.echoTimeValue.text()), vary=False)

            buttonsUnChecked = [not self.optimizeFatFraction.isChecked(),
                              not self.optimizeMuscleFraction.isChecked(),
                              not self.optimizeMuscleT2.isChecked()]

            print(buttonsUnChecked)

            if all(buttonsUnChecked):
                print("all buttuns unchecked")
                worked=False

            self.lmparams['azzt2fitparams'] = self.params
        except:
            print("exception occurred")
            worked = False
        return  worked



if __name__ == "__main__":
    import sys
    import lmfit as lm

    lmparams = {}

    epgt2fitparams = lm.Parameters()
    azzt2fitparams = lm.Parameters()

    epgt2fitparams.add('T2fat',    value = 180.0, min=0, max=5000, vary=False)
    epgt2fitparams.add('T2muscle', value = 35,    min=0, max=100,  vary=True )
    epgt2fitparams.add('Afat',     value = 0.20,  min=0, max=10,   vary=True )
    epgt2fitparams.add('Amuscle',  value = 0.80,  min=0, max=10,   vary=True )
    epgt2fitparams.add('T1fat',    value = 365.0,                  vary=False)
    epgt2fitparams.add('T1muscle', value = 1400,                   vary=False)
    epgt2fitparams.add('echo',     value = 10.0,                   vary=False)


    azzt2fitparams.add_many(('Afat',      60.0,  True,  0,  250,  None),
                            ('Amuscle',   40.0,  True,  0,  250,  None),
                            ('T2muscle',  40.0,  True,  0,  100,  None),
                            ('c_l',        0.55, False, 0,  2000, None),
                            ('c_s',        0.45, False, 0,  2000, None),
                            ('t2_fl',    250.0,  False, 0,  2000, None),
                            ('t2_fs',     43.0,  False, 0,  2000, None),
                            ('echo',      10.0,  False, 0,  2000, None))


    lmparams['epgt2fitparams'] = epgt2fitparams
    lmparams['azzt2fitparams'] = azzt2fitparams

    app = QtWidgets.QApplication(sys.argv)
    Azzabou = QtWidgets.QDialog()
    ui = AzzT2paramsDialog(lmparams)
    ui.setupAzzT2paramsDialog(Azzabou)
    Azzabou.show()
    sys.exit(app.exec_())

