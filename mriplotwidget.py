# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 14:34:43 2019

@author: neh69
"""
import numpy as np
import matplotlib

from matplotlib import pyplot as plt
#import seaborn as sns

from matplotlib.backends.qt_compat import QtCore,  QtWidgets, is_pyqt5
#import seaborn as sns

if is_pyqt5():
    print("pyqt5")
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    print("pyqt4")
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
#from matplotlib.figure import Figure

import mplcursors

#from ImageData import T2imageData
parameterNames ={'T2m':   [ 'T$_{2m}$ [ms]','{}, T$_{{2m}}$ = {:.1f} [ms]' ],
                 'Am100': [ 'A$_{m}$ [%]', '{}, A$_{{m}}$ = {:.1f} [%]' ],
                 'Af100': [ 'A$_{f}$ [%]', '{}, A$_{{f}}$ = {:.1f} [%]'],
                  'B1':   [ 'B$_{1}$ [-]', '{}, B$_{{1}}$ = {:.1f} [-]'],
                 'fatPC': [ 'fat [%]',  '{}, fat = {:.1f} [%]']
               }

class MRIPlotWidget(QtWidgets.QWidget):

#class PlotWidget(QtWidgets.QWidget):

    def __init__(self, parent=None, showToolbar=True, imageData=None):

        super().__init__(parent)
        self.fig, self.ax = plt.subplots()
#        fig =Figure(figsize=(3, 5))
        self.fig.set_tight_layout(True)
        self.plot_canvas = FigureCanvas(self.fig)
#        self.ax = self.fig.add_subplot(111)

#        mplcursors.cursor(fig,hover=True)

        self.layout = QtWidgets.QVBoxLayout(self)

#    def __init__( self, parent=None, showToolbar=True, imageData=None):


        self.axesList = []
        self.imageData = imageData



        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)


        self.toggleImage = QtWidgets.QRadioButton("Hide background Image")
        self.toggleImage.toggled.connect(lambda: self.toggleImageChanged(self.toggleImage))

        self.toggleImage.isChecked()

        self.layout.addWidget(self.toggleImage)
        self.toggleImage.setSizePolicy(sizePolicy)

        self.sliceLabel = QtWidgets.QLabel("slices")
        self.layout.addWidget(self.sliceLabel)
        self.sliceLabel.setSizePolicy(sizePolicy)

        self.slicesSlider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slicesSlider.setMinimum(0)
        self.slicesSlider.setMaximum(4)
        self.slicesSlider.setValue(0)
        self.slicesSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slicesSlider.setTickInterval(1)
        self.slicesSlider.valueChanged.connect(self.valuechangedSlider)


        self.slicesSlider.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed))
        self.layout.addWidget(self.slicesSlider)


        self.echoesLabel = QtWidgets.QLabel("echoes")
        self.echoesLabel.setSizePolicy(sizePolicy)
        self.layout.addWidget(self.echoesLabel)

        self.echoesSlider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.echoesSlider.setMinimum(0)
        self.echoesSlider.setMaximum(16)
        self.echoesSlider.setValue(0)
        self.echoesSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.echoesSlider.setTickInterval(1)
        self.echoesSlider.valueChanged.connect(self.valuechangedSlider)

        self.echoesSlider.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed))
        self.layout.addWidget(self.echoesSlider)

        self.layout.addWidget(self.plot_canvas)

        if showToolbar:
            self.toolbar = NavigationToolbar(self.plot_canvas, self)
            self.layout.addWidget(self.toolbar)


        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding,
                           QtWidgets.QSizePolicy.Expanding)
        self.updateGeometry()

        self.plot_canvas.mpl_connect('button_press_event', self.onclick)
#        self.plot_canvas.mpl_connect("motion_notify_event", self.onhover)

        self.ax.imshow(matplotlib.image.imread('vision.png')[:,:,0])
#        self.canvas.figure.axes
#        self.mpl_cursor = mplcursors.cursor(self.plot_canvas.figure.axes,hover=True)
        self.ax.grid(False)


    def valuechangedSlider(self):
        slice_ = self.slicesSlider.value()
        echo = self.echoesSlider.value()

        self.imageData.currentSlice = slice_
        self.imageData.currentEcho = echo
        print("slicesSlider Value =", slice_, "echoesSlider Value =", echo )
        if isinstance(self.imageData.ImageDataT2, np.ndarray):
            print("updating image slice")
            if self.toggleImage.isChecked():
                self.imageData.mriSliceIMG *=  0.0
            else:
                self.imageData.mriSiceIMG=self.imageData.ImageDataT2[:,:,slice_,echo].copy()

            self.imageData.overlayRoisOnImage(slice_+1, self.imageData.fittingParam)
            self.update_plot(self.imageData.mriSiceIMG, self.imageData.maskedROIs.reshape(self.imageData.mriSiceIMG.shape))

            self.histPlotWidget.update_plot([slice_+1,self.imageData.T2slices,self.imageData.dixonSlices],
                                            [self.imageData.t2_data_summary_df,self.imageData.dixon_data_summary_df],
                                            self.imageData.fittingParam)

            self.barPlotWidget.update_plot([slice_+1,self.imageData.T2slices,self.imageData.dixonSlices],
                                           [self.imageData.t2_data_summary_df,self.imageData.dixon_data_summary_df],
                                           self.imageData.fittingParam)
        else:
            print("No images to update")



    def on_fittingParams_rbtn_toggled(self, fittingParam):

#        rb = self.fittingParams_rbtn.sender()
        print(fittingParam)
        self.imageData.fittingParam = fittingParam
        self.valuechangedSlider()


    def register_PlotWidgets(self, T2PlotWidget, histPlotWidget,
                             barPlotWidget, radioButtonsWidget):

        self.T2PlotWidget = T2PlotWidget
        self.histPlotWidget = histPlotWidget
        self.barPlotWidget = barPlotWidget
        self.radioButtonsWidget = radioButtonsWidget


#    def onhover(self,event):
#
#        if event.inaxes:
#
#            xcoord = int(round(event.xdata))
#            ycoord = int(round(event.ydata))
#
#            print('on hover, ', xcoord, ycoord)

    def onclick(self,event):

        xcoord = int(round(event.xdata))
        ycoord = int(round(event.ydata))

        print("MRI Plot window On Click")

        print('ycoord =', ycoord)

        print(type(self.imageData.ImageDataT2))

        if type(self.imageData.ImageDataT2) != type(None):

            image_shape = self.imageData.ImageDataT2.shape

            print(image_shape[0],image_shape[0]-ycoord, ycoord)

            t2data = self.imageData.ImageDataT2[ycoord,xcoord,int(self.slicesSlider.value()),:]

            self.T2PlotWidget.update_plot( xcoord, ycoord, t2data)




    def update_plot(self, img, maskedROIs):

        self.ax.cla()
        self.ax.imshow(img,cmap=plt.cm.gray,
                                interpolation='nearest')

        print("maskedROIs.shape", maskedROIs.shape)
        print("img.shape", img.shape)

        print("maskedROIs.max()",maskedROIs.max())

        if maskedROIs.max() > 0:

            self.ax.imshow(maskedROIs.reshape(img.shape),
                                    cmap=plt.cm.jet, alpha=.5,
                                    interpolation='bilinear')

        mpl_cursor = mplcursors.cursor(self.plot_canvas.figure.axes,hover=True)

        @mpl_cursor.connect("add")
        def _(sel):

            ann = sel.annotation
            ttt = ann.get_text()
            xc,yc, zl = [s.split('=') for s in ttt.splitlines()]

            x = round(float(xc[1]))
            y = round(float(yc[1]))

            print("x",x, "y",y)

            nrows,ncols = img.shape
            cslice=self.imageData.currentSlice
            fitParam = self.imageData.fittingParam

            print("cslice",cslice, "nrows", nrows, "ncols")
            print("fitParam",fitParam)

            ### figure out which data set to use

            if fitParam in self.imageData.t2_data_summary_df.columns:
                print(fitParam, "T2 dataFrame chosen")
                data_df = self.imageData.t2_data_summary_df
                slice_df = data_df[data_df.slice==cslice+1]
            elif fitParam in self.imageData.dixon_data_summary_df.columns:
                print(fitParam, "Dixon dataFrame chosen")
                data_df = self.imageData.dixon_data_summary_df
                if cslice+1 in self.imageData.T2slices:
                    dixonSliceIndex = self.imageData.dixonSlices[self.imageData.T2slices.index(cslice+1)]
                    slice_df = data_df[data_df.slice==dixonSliceIndex]
                else:
                    slice_df = data_df[data_df.slice==cslice]



            ### return current slice

#            slice_df = data_df[data_df.slice==cslice+1]

            print("slice_df.shape",slice_df.shape)

            roiList   = slice_df[slice_df['pixel_index']==y*ncols+x]['roi'].values
            valueList = slice_df[slice_df['pixel_index']==y*ncols+x][fitParam].values

            print("roiList", roiList)
            print("valueList",valueList)

            fitParamLabel = parameterNames[fitParam][1]

            if len(roiList)>0:
                roi=roiList[0]
                value=valueList[0]
                ann.set_text(fitParamLabel.format( roi,  value))
            else:
                ann.set_text("x = {:d}\ny = {:d}".format( x,  y ))

        self.ax.grid(False)

        self.plot_canvas.draw()


    def toggleImageChanged(self,b1):

        print("Entered toggleImageChanged")
        if not isinstance(self.imageData.mriSliceIMG, type(None) ):
            if self.toggleImage.isChecked():
                print("Clear background image")
                self.update_plot(np.zeros((self.imageData.mriSliceIMG.shape)),
                                 self.imageData.maskedROIs.reshape((self.imageData.mriSliceIMG.shape)))
            else:
                self.valuechangedSlider()


