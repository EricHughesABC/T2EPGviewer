# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 10:29:38 2017

@author: neh69
"""
import os
import sys
import numpy as np
import pandas as pd
import lmfit as lm

import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

from PyQt5 import QtCore, QtWidgets


import visionplot_widgets
import mriplotwidget


from ImageData import T2imageData



def openStudyDir():
    dlg = QtWidgets.QFileDialog()
    returned_data = dlg.getExistingDirectory(None, "Study Directory", "")
    print("openStudyDir\n",returned_data, type(returned_data))

#    tree_window.setRootIndex(tree_window.model.index(returned_data))



def openNiftiAnalyzeFile():
    dlg = QtWidgets.QFileDialog()
    returned_data = dlg.getOpenFileName(None, "MRI data nifti/analyze", procDataDirPath, "nii files (*.nii);;analyze files (*.img);;All files (*)")
    print(returned_data)


def getH5file():
    dlg =  QtWidgets.QFileDialog()
    returned_data = dlg.getOpenFileName(None, "select results file", procDataDirPath, "CSV files (*.csv);;All files (*)")
    pathandfilename = returned_data[0]

    #self.hd5_store = pd.HDFStore(pathandfilename)


    if len(pathandfilename) > 0:
        ### attempt to extract details from data
        print(pathandfilename)
        imageData.readin_alldata_from_results_filename(  os.path.abspath(pathandfilename))

        if imageData.read_T2_img_hdr_files():

            print("just before read_T2_data()")

            if  imageData.read_T2_data():

                imageData.read_Dixon_data()

                print("just after read_T2_data()")

                mainWindow.setWindowTitle(imageData.T2resultsFilenameAndPath)

                ####  Update image displayed in window
                imageData.overlayRoisOnImage(0, imageData.fittingParam)
#                mri_window.update_plot(imageData.img1)
                mri_window.update_plot(imageData.mriSliceIMG, imageData.maskedROIs)
                print("type(imageData.ImageDataT2)",type(imageData.ImageDataT2))

                hist_window.update_plot([1,imageData.T2slices,imageData.dixonSlices], [imageData.t2_data_summary_df, imageData.dixon_data_summary_df], "T2m")
                bar_window.update_plot([1,imageData.T2slices,imageData.dixonSlices], [imageData.t2_data_summary_df, imageData.dixon_data_summary_df], "T2m")

                #### set min max on sliders

                mri_window.slicesSlider.setMinimum(0)
                mri_window.slicesSlider.setMaximum(imageData.numSlicesT2-1)
                mri_window.slicesSlider.setValue(0)

                mri_window.echoesSlider.setMinimum(0)
                mri_window.echoesSlider.setMaximum(imageData.numEchoesT2-1)
                mri_window.slicesSlider.setValue(0)
        else:
            print(imageData.t2_image_hdr_pathfilename, " not found")







def fileQuit(self):
    self.close()

def closeEvent(self, ce):
    self.fileQuit()


if __name__ == "__main__":


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
    epgt2fitparams.add('B1scale',  value = 1.0,  min=0, max=2,     vary=True )


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

    params=azzt2fitparams

    matplotlib.use('Qt5Agg')
    plt.style.context('seaborn-colorblind')
    sns.set(font_scale = 0.6)

#    sns.set_palette("pastel")

    procDataDirPath = r"Z:\testPhenoDM1\PDM001A\sess-1\upperleg\T2\results\muscle\muscleEPG1"


    progname = os.path.basename(sys.argv[0])
    qApp = QtWidgets.QApplication(sys.argv)
    imageData = T2imageData()

    print("imageData.fittingParam:",imageData.fittingParam)

    mainWindow = QtWidgets.QMainWindow()

    mainWindow.setAttribute(QtCore.Qt.WA_DeleteOnClose)

    mainWindow.setWindowTitle("application main window")

    file_menu = QtWidgets.QMenu('&File', mainWindow)

#    file_menu.addAction("&Open study Directory", openStudyDir)
    file_menu.addAction('&Choose Study Results File', getH5file,    QtCore.Qt.CTRL + QtCore.Qt.Key_H)
#    file_menu.addAction('&Open nifti/analyze image File', openNiftiAnalyzeFile )
#    file_menu.addAction('&Choose Rois',    imageData.getRoiFiles,  QtCore.Qt.CTRL + QtCore.Qt.Key_R)

#    file_menu.addAction('&Quit', fileQuit,   QtCore.Qt.CTRL + QtCore.Qt.Key_Q)

    mainWindow.menuBar().addMenu(file_menu)

    main_widget = QtWidgets.QWidget(mainWindow)

    mainlayout = QtWidgets.QHBoxLayout(main_widget)
   # mainWindow.setCentralWidget(main_widget)

#    plot_window1 = mri_widget(main_widget)

    npts = 256*100

    iii = np.random.permutation(np.arange(255*255))[:npts]
    ddd = np.random.randn(npts)*100+500
    data_df = pd.DataFrame({'iii': iii, 'ddd':ddd})


    leftwindow = QtWidgets.QWidget()
    rightwindow = QtWidgets.QWidget()

    splitHwidget = QtWidgets.QSplitter(QtCore.Qt.Horizontal)

    hlayout = QtWidgets.QHBoxLayout(leftwindow)
    vlayout = QtWidgets.QVBoxLayout(rightwindow)

    mri_window = mriplotwidget.MRIPlotWidget( imageData=imageData)

    rbtns_window =  visionplot_widgets.radiobuttons_fitWidget(mri_window=mri_window)
    t2plot_window = visionplot_widgets.T2PlotWidget( lmparams, showToolbar=False)
    bar_window =    visionplot_widgets.BarPlotWidget( showToolbar=False, data_df=data_df, image_size=256)
    hist_window =   visionplot_widgets.HistogramPlotWidget( mri_plot=mri_window, showToolbar=True,data_df=data_df, image_size=256)

    mainlayout.addWidget(splitHwidget)
    hlayout.addWidget(rbtns_window)
    hlayout.addWidget(mri_window)
    vlayout.addWidget(t2plot_window)
    vlayout.addWidget(bar_window)
    vlayout.addWidget(hist_window)

    splitHwidget.addWidget(leftwindow)
    splitHwidget.addWidget(rightwindow )

    mri_window.register_PlotWidgets(t2plot_window, bar_window, hist_window, rbtns_window)

    main_widget.setFocus()
    mainWindow.setCentralWidget(main_widget)

    mainWindow.show()
    sys.exit(qApp.exec_())


