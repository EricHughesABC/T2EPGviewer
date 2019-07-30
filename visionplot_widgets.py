# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 13:11:07 2018

@author: neh69
"""
import sys
import numpy as np
#import matplotlib
import pandas as pd
#import mplcursors

from uncertainties import ufloat
import t2fit
import lmfit as lm

from matplotlib import pyplot as plt
#import seaborn as sns

from matplotlib.backends.qt_compat import QtCore,  QtWidgets, is_pyqt5
import seaborn as sns

if is_pyqt5():
    print("pyqt5")
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    print("pyqt4")
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure


from ImageData import T2imageData
import epgT2paramsDialog
import azzT2paramsDialog



#mxyz90 = np.fromfile( 'epg\mxyz90.txt', sep=' ' )
#mxyz180 = np.fromfile('epg\mxyz180.txt', sep=' ')
#
#mxyz90 = mxyz90.reshape(5,512)
#mxyz180 = mxyz180.reshape(5,512)
#
#offset=130
#step=10
#epg_slice_xxx =mxyz90[0][offset:-offset+step:step] # mm
#epg_p90 = mxyz90[-1][offset:-offset+step:step]     # degrees
#epg_p180 = mxyz180[-1][offset:-offset+step:step]   # degrees
#epg_dx=epg_slice_xxx[1]-epg_slice_xxx[0]



class PlotWidget(QtWidgets.QWidget):

    def __init__(self, parent=None, showToolbar=True):

        super(PlotWidget,self).__init__(parent)

        fig =Figure(figsize=(3, 5))
        fig.set_tight_layout(True)
        self.plot_canvas = FigureCanvas(fig)
        self.ax = fig.add_subplot(111)



        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.plot_canvas)

        if showToolbar:
            self.toolbar = NavigationToolbar(self.plot_canvas, self)
            self.layout.addWidget(self.toolbar)

    def return_ax(self):
        return(self.ax)



class HistogramPlotWidget(PlotWidget):

    def __init__(self, parent=None, showToolbar=False, mri_plot=None, data_df=None, image_size=256):

        self.data_df = data_df
        self.image_size = image_size

        super(HistogramPlotWidget,self).__init__(parent=parent, showToolbar=showToolbar)

        self.buttonUpdate = QtWidgets.QPushButton('Update')
        self.buttonUpdate.clicked.connect(self.update)
        self.layout.addWidget(self.buttonUpdate)


    def update(self):

        print((self.ax.get_xlim()))
        xmin,xmax = self.ax.get_xlim()



    def update_plot(self, slice_info,data_dframes, plot_param):

        self.ax.cla()
        self.plot_canvas.draw()

        print("Entered HistogramPlotWidget.update_image, plot_param =", plot_param)

        data_df=None

        slice_displayed = slice_info[0]
        T2_slices = slice_info[1]
        dixon_slices = slice_info[2]

        print("data_dframes[0]", type(data_dframes[0]), data_dframes[0].columns)
        print("data_dframes[1]", type(data_dframes[1]), data_dframes[1].columns)


        if isinstance(data_dframes[0],pd.core.frame.DataFrame):
            if plot_param in data_dframes[0].columns:
                print("plot_param {} found in dataframe is T2".format(plot_param))
                data_df = data_dframes[0]
                data_df=data_df[data_df["slice"]==slice_displayed]
            elif isinstance(data_dframes[1],pd.core.frame.DataFrame):
                print("plot_param {} found in dataframe is Dixon".format(plot_param))
                print("data_dframes[1].columns",data_dframes[1].columns)
                if plot_param in data_dframes[1].columns:
                    print("plot_param in data_dframes[1]:", plot_param)
                    data_df = data_dframes[1]
                    if slice_displayed in T2_slices:
                        slice_displayed = dixon_slices[T2_slices.index(slice_displayed)]
                    data_df=data_df[data_df["slice"]==slice_displayed]
                else:
                    print( "HIST", plot_param, " not found")
                    return False
            else:
                print("HIST", isinstance(data_dframes[1],pd.core.frame.DataFrame))
                return False

        print("HIST data_df.shape[0]",data_df.shape[0])
        if data_df.shape[0] == 0 or type(data_df) == type(None):
            print("HIST return because df shape[0] = 0 or type of data_df = type None")
            return False

#        self.ax2.cla()
        if  isinstance(data_df, pd.core.frame.DataFrame):
            print("Plotting HIST Plot" )
            data_df = data_df.sort_values(by=['roi'])
            #plot_param = "T2value"
            for roi in data_df.roi.unique():
                print(roi)
                query_str = '(slice == {}) and (roi == "{}")'.format(slice_displayed, roi)
                sns.distplot(data_df.query(query_str)[plot_param], hist=False, label=roi, ax=self.ax)
#                self.ax.hist( data_df.query(query_str)[plot_param], bins=100, label=roi, alpha=0.7);
            self.ax.legend()

            if plot_param == "T2m":
                self.ax.set_xlabel("$T_2$ [ms]")

            elif plot_param == "Am100":
                self.ax.set_xlabel("$A_m$ [%]")

            elif plot_param == "Af100":
                self.ax.set_xlabel("$A_f$ [%]")
            elif plot_param == "B1":
                self.ax.set_xlabel("$B_1$")

            elif plot_param == "fatPC":
                self.ax.set_xlabel("ff [%]")

            self.ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

            self.plot_canvas.draw()

        return True




class BarPlotWidget(PlotWidget):

    def __init__(self, parent=None, showToolbar=True, data_df=None, image_size=256):

        self.data_df = data_df
        self.image_size = image_size

        super(BarPlotWidget,self).__init__(parent=parent, showToolbar=showToolbar)

#        self.buttonUpdate = QtWidgets.QPushButton('Update')
#        self.buttonUpdate.clicked.connect(self.update)
#        self.layout.addWidget(self.buttonUpdate)


    def update(self):

        print((self.ax.get_xlim()))
        xmin,xmax = self.ax.get_xlim()



    def update_plot(self, slice_info,data_dframes, plot_param):

        self.ax.cla()
        self.plot_canvas.draw()

        print("Entered BarPlotWidget.update_image, plot_param =", plot_param)
        #print(data_.columns)

        slice_displayed = slice_info[0]
        T2_slices = slice_info[1]
        dixon_slices = slice_info[2]

        data_df=None

        print("data_dframes[0]", type(data_dframes[0]), data_dframes[0].columns)
        print("data_dframes[1]", type(data_dframes[1]), data_dframes[1].columns)


        if isinstance(data_dframes[0],pd.core.frame.DataFrame):

            if plot_param in data_dframes[0].columns:

                print("plot_param {} found in dataframe is T2".format(plot_param))
                data_df = data_dframes[0]
                data_df=data_df[data_df["slice"]==slice_displayed]

            elif isinstance(data_dframes[1],pd.core.frame.DataFrame):

                print("plot_param {} found in dataframe is Dixon".format(plot_param))
                print("data_dframes[1].columns",data_dframes[1].columns)

                if plot_param in data_dframes[1].columns:

                    print("plot_param in data_dframes[1]:", plot_param)
                    data_df = data_dframes[1]

                    if slice_displayed in T2_slices:

                        slice_displayed = dixon_slices[T2_slices.index(slice_displayed)]
#                    else:
#                        dixon_slice = slice_displayed
#                    slice_displayed = dixon_slices[T2_slices.index(slice_displayed)]
                    data_df=data_df[data_df["slice"]==slice_displayed]
                else:
                    print( plot_param, " not found")
                    return(False)
            else:
                print(isinstance(data_dframes[1],pd.core.frame.DataFrame))
                return(False)

        print("HIST data_df.shape[0]", data_df.shape[0])

        if data_df.shape[0] == 0 or type(data_df) == type(None):
            print("return because df shape[0] = 0 or type of data_df = type None")
            return False

        data_df = data_df.sort_values(by=['roi'])

        if  isinstance(data_df, pd.core.frame.DataFrame):
            print("Plotting BAR Plot" )
            #plot_param = "T2value"
#            for roi in data_df.roi.unique():
#                print(roi)
#                query_str = '(slice == {}) and (roi == "{}")'.format(slice_displayed, roi)
#                self.ax.hist( data_df.query(query_str)[plot_param], bins=100, label=roi, alpha=0.4);
#            self.ax.legend()

#            numRois = data_df.roi.unique().shape[0]

            sns.catplot( kind='bar',
                           x='slice',
                           y=plot_param,
                           data=data_df,
                           hue='roi',
                           ci="sd",
                           ax=self.return_ax()
                           );

            self.ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
            if plot_param == "T2m":
                self.ax.set_ylabel("$T_2$ [ms]")
            elif plot_param == "Am100":
                self.ax.set_ylabel("$A_m$ [%]")
            elif plot_param == "Af100":
                self.ax.set_ylabel("$A_f$ [%]")
            elif plot_param == "B1":
                self.ax.set_ylabel("$B_1$")
            elif plot_param == "fatPC":
                self.ax.set_ylabel("ff [%]")

            self.ax.set_xlabel("slices")
#            plt.tight_layout()
            self.plot_canvas.draw()

        return True






class T2PlotWidget(PlotWidget):

    def __init__( self, lmparams, parent=None, showToolbar=True):

        super(T2PlotWidget, self).__init__(parent, showToolbar=showToolbar)
        self.plot_T2_startup()

        self.lmparams = lmparams



        self.T2epgnorm_btns = radiobuttons_EPGWidget(self.lmparams, self)
        self.layout.addWidget(self.T2epgnorm_btns)





    def plot_T2_startup(self):
        ttt = np.linspace(0,170, 17)
        yyy =  80*np.exp(-ttt/35.0)+20*np.exp(-ttt/120.0)
        yyy1 = yyy+np.random.randn(len(yyy))

        self.ax.semilogy(ttt, yyy1, 'o')
        self.ax.semilogy(ttt, yyy,  '-')
        self.ax.set_xlabel('Time [ms]')
        self.ax.set_ylabel('Signal')
        self.ax.set_ylim(1,110)



    def update_plot(self, xcoord, ycoord, t2data):

        print("update_T2PlotImag called")
        #self.ttt = np.linspace(0,170, 17)

        self.ax.cla()  # clear the plot area

        if self.T2epgnorm_btns.epg_rbtn.isChecked():
            print("Run EPG Fit")
            print('echo value', self.lmparams['epgt2fitparams']['echo'])

#            params = lm.Parameters()
#            params.add('T2fat',    value = 180.0, min=0, max=5000, vary=False)
#            params.add('T2muscle', value = 35,    min=0, max=100,  vary=True )
#            params.add('Afat',     value = 0.01,  min=0, max=10,   vary=True )
#            params.add('Amuscle',  value = 0.1,   min=0, max=10,   vary=True )
#            params.add('T1fat',    value = 365.0,                  vary=False)
#            params.add('T1muscle', value = 1400,                   vary=False)
#            params.add('echo',     value = 10.0,                   vary=False)



            #xxx = np.linspace(10,10*len(t2data), len(t2data))
#            self.params.pretty_print()

            #fit_values, fit_curve, fit_data, lmresults = t2fit.calculate_T2values_on_slice_muscleEPG(self.lmparams, t2data, len(t2data),  xxx, epg_dx,  epg_p90, epg_p180)
            fit_curve, fit_data, lmresults, xxx = t2fit.calculate_T2values_on_slice_muscleEPG(self.lmparams, t2data)

        else:
            print("Run Normal T2 Fit")

            fit_curve, fit_data, lmresults, xxx = t2fit.calculate_T2values_on_slice_muscleAzz(self.lmparams,t2data)

        print(dir(lmresults))
        print(lmresults.success)

        if not lmresults.success:
            return
        #
        # Create uncertainty floats of varied params
        #
        ufs = {}
        for vname in lmresults.var_names:
            v = lmresults.params[vname].value
            e = lmresults.params[vname].stderr
            ufs[vname] = ufloat( v,e)

        if ('Amuscle' in ufs.keys()) and ('Afat' in ufs.keys()):
            ufs['Amuscle'] = 100.0*ufs['Amuscle']/(ufs['Amuscle']+ufs['Afat'])
            ufs['Afat'] = 100.0-ufs['Amuscle']

        t2m_str = ""
        t2f_str = ""
        Am_str  = ""
        Af_str  = ""
        B1_str  = ""

        for name, value in ufs.items():

            print(name)

            if name == 'T2muscle':

                t2m_str = "$T_{{2m}}$ = ${:5.2fL}$  ms\n".format(value)

            elif name == 'T2fat':

                t2f_str = "$T_{{2f}}$ = ${:5.2fL}$  ms\n".format(value)

            elif name == 'Amuscle':

                Am_str = "$A_m$ = ${:5.2fL}$\n".format(value)

            elif name == 'Afat':

                Af_str = "$A_f$ = ${:5.2fL}$\n".format(value)

            elif name == 'B1scale':

                B1_str = "$B_1$ scale = ${:5.2fL}$\n".format(value)


        results_legend = "{}{}{}{}{}".format(t2m_str, t2f_str, Am_str, Af_str, B1_str)

        if self.T2epgnorm_btns.epg_rbtn.isChecked():
            self.ax.semilogy(xxx, 100*fit_data,  'o')
            self.ax.semilogy(xxx, 100*fit_curve, '-', label=results_legend)
        else:

            self.ax.semilogy(xxx[2:], 100*fit_curve, '-', label=results_legend)
            self.ax.semilogy(xxx,     100*fit_data,  'o')

        self.ax.legend( fontsize=8)
        #self.ax.set_ylim(1,110)
        self.ax.set_xlabel('Time [ms]')
        self.ax.set_ylabel('Signal')
        self.ax.set_ylim(0.5,150)

        self.plot_canvas.draw()



class radiobuttons_EPGWidget(QtWidgets.QWidget):

    def __init__(self, lmparams, parent=None):

        self.lmparams = lmparams

        self.epgDialog = QtWidgets.QDialog()
        self.epgT2params_widget = epgT2paramsDialog.EpgT2paramsDialog(self.lmparams)
        self.epgT2params_widget.setupEpgT2paramsDialog(self.epgDialog)

        self.azzDialog = QtWidgets.QDialog()
        self.azzT2params_widget = azzT2paramsDialog.AzzT2paramsDialog(self.lmparams)
        self.azzT2params_widget.setupAzzT2paramsDialog(self.azzDialog)

        super(radiobuttons_EPGWidget, self).__init__(parent)
        hlayout = QtWidgets.QHBoxLayout(self)

        group_rbtns = QtWidgets.QButtonGroup()
        group_rbtns.exclusive()

        self.epg_rbtn = QtWidgets.QRadioButton("EPG T2")
        self.norm_rbtn = QtWidgets.QRadioButton("normal T2")
        self.norm_rbtn.setChecked(True);
        self.T2params_btn = QtWidgets.QPushButton("T2 Parameters")

        self.epg_rbtn.fittingParam = "epg"
        self.norm_rbtn.fittingParam= 'norm'

        self.epg_rbtn.toggled.connect(lambda:self.btnstate(self.epg_rbtn))
        self.norm_rbtn.toggled.connect(lambda:self.btnstate(self.norm_rbtn))

        self.T2params_btn.clicked.connect(self.T2params_btn_clicked)

        group_rbtns.addButton(self.epg_rbtn)
        group_rbtns.addButton(self.norm_rbtn)


        hlayout.addWidget(self.norm_rbtn)
        hlayout.addWidget(self.epg_rbtn)
        hlayout.addStretch(1)
        hlayout.addWidget(self.T2params_btn)

    def T2params_btn_clicked(self):
        print("T2params_btn_clicked")

        if self.epg_rbtn.isChecked():
            rt = self.epgDialog.show()

        else:
            rt = self.azzDialog.show()


        print("rt =", rt)

    def btnstate(self,b):

        if b.isChecked():
            print(b.text())
            print(b.fittingParam)
            #self.mri_window.on_fittingParams_rbtn_toggled( str(b.fittingParam))






class radiobuttons_fitWidget(QtWidgets.QWidget):

    def __init__(self, parent=None, mri_window=None):

        super(radiobuttons_fitWidget, self).__init__(parent)
        self.mri_window = mri_window

        vbox1_radiobuttons = QtWidgets.QVBoxLayout(self)

        group_fittingParams_rbtns = QtWidgets.QButtonGroup()
        group_fittingParams_rbtns.exclusive()

        self.T2_rbtn = QtWidgets.QRadioButton("T2")
        self.Am_rbtn = QtWidgets.QRadioButton("Am")
        self.Af_rbtn = QtWidgets.QRadioButton("Af")
        self.B1_rbtn = QtWidgets.QRadioButton("B1")
        self.Dixon_rbtn = QtWidgets.QRadioButton("Dixon Fat [%]")

        self.T2_rbtn.setChecked(True)

        self.T2_rbtn.fittingParam = "T2m"
        self.Am_rbtn.fittingParam = "Am100"
        self.Af_rbtn.fittingParam = "Af100"
        self.B1_rbtn.fittingParam = "B1"
        self.Dixon_rbtn.fittingParam = "fatPC"

        self.T2_rbtn.toggled.connect(lambda:self.btnstate(self.T2_rbtn))
        self.Am_rbtn.toggled.connect(lambda:self.btnstate(self.Am_rbtn))
        self.Af_rbtn.toggled.connect(lambda:self.btnstate(self.Af_rbtn))
        self.B1_rbtn.toggled.connect(lambda:self.btnstate(self.B1_rbtn))
        self.Dixon_rbtn.toggled.connect(lambda:self.btnstate(self.Dixon_rbtn))

        group_fittingParams_rbtns.addButton(self.T2_rbtn)
        group_fittingParams_rbtns.addButton(self.Am_rbtn)
        group_fittingParams_rbtns.addButton(self.Af_rbtn)
        group_fittingParams_rbtns.addButton(self.B1_rbtn)
        group_fittingParams_rbtns.addButton(self.Dixon_rbtn)

        vbox1_radiobuttons.addWidget(self.T2_rbtn)
        vbox1_radiobuttons.addWidget(self.Am_rbtn)
        vbox1_radiobuttons.addWidget(self.Af_rbtn)
        vbox1_radiobuttons.addWidget(self.B1_rbtn)
        vbox1_radiobuttons.addWidget(self.Dixon_rbtn)

        vbox1_radiobuttons.addStretch(1)

    def btnstate(self,b):

        if b.isChecked():
            print(b.text())
            print(b.fittingParam)
            self.mri_window.on_fittingParams_rbtn_toggled( str(b.fittingParam))






class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self, params):

        self.params = params

        imageData = T2imageData()

        print("imageData.fittingParam:",imageData.fittingParam)

        npts = 256*100

        iii = np.random.permutation(np.arange(255*255))[:npts]
        ddd = np.random.randn(npts)*100+500

        data_df = pd.DataFrame({'iii': iii, 'ddd':ddd})

        super(ApplicationWindow, self).__init__()
        leftwindow = QtWidgets.QWidget()
        rightwindow = QtWidgets.QWidget()

        splitHwidget = QtWidgets.QSplitter(QtCore.Qt.Horizontal)



        #hlayout = QtWidgets.QHBoxLayout(self._main)
        hlayout = QtWidgets.QHBoxLayout(leftwindow)
        vlayout = QtWidgets.QVBoxLayout(rightwindow)




        mriplot_window = MRIPlotWidget(imageData=imageData)
        rbtns_window = radiobuttons_fitWidget(mri_window=mriplot_window)
        t2plot_window = T2PlotWidget( self.params, showToolbar=False)
        h1_window = PlotWidget( showToolbar=False)
        h2_window = HistogramPlotWidget(showToolbar=True)
        #hlayout.addWidget(mriplot_window)

        mriplot_window.register_PlotWidgets(t2plot_window, h1_window, h2_window)

        #vbox1_radiobuttons = QtWidgets.QVBoxLayout()

#        hbox.addLayout(vbox1_radiobuttons)
#        hbox.addLayout(vbox1_image)
#        hbox.addLayout(vbox2_image)

        hlayout.addWidget(rbtns_window)
        hlayout.addWidget(mriplot_window)
        vlayout.addWidget(t2plot_window)
        vlayout.addWidget(h1_window)
        vlayout.addWidget(h2_window)

        def func3(x, y):
            return (1 - x / 2 + x**5 + y**3) * np.exp(-(x**2 + y**2))


        # make these smaller to increase the resolution
        dx, dy = 0.05, 0.05

        x = np.arange(-3.0, 3.0, dx)
        y = np.arange(-3.0, 3.0, dy)
        X, Y = np.meshgrid(x, y)

        # when layering multiple images, the images need to have the same
        # extent.  This does not mean they need to have the same shape, but
        # they both need to render to the same coordinate system determined by
        # xmin, xmax, ymin, ymax.  Note if you use different interpolations
        # for the images their apparent extent could be different due to
        # interpolation edge effects

        extent = np.min(x), np.max(x), np.min(y), np.max(y)


        Z1 = np.add.outer(range(8), range(8)) % 2  # chessboard
        mriplot_window.return_ax().imshow(Z1, cmap=plt.cm.gray,
                                interpolation='nearest', extent=extent)

        Z2 = func3(X, Y)

        mriplot_window.return_ax().imshow(Z2, cmap=plt.cm.viridis, alpha=.9,
                                interpolation='bilinear',  extent=extent)

        splitHwidget.addWidget(leftwindow)
        splitHwidget.addWidget(rightwindow )


        print(data_df.head())
        plot_image = np.zeros(255*255)
        plot_image[data_df['iii']] = data_df['ddd']

        h1_window.return_ax().imshow( plot_image.reshape((255,255)))
        h1_window.return_ax().set_xlabel('x')
        h1_window.return_ax().set_ylabel('y')


        h2_window.return_ax().hist(ddd, bins=100)
        h2_window.return_ax().set_xlabel('x')
        h2_window.return_ax().set_ylabel('y')


        self.setCentralWidget(splitHwidget)



    def zoom(self):
        self.histtoolbar.zoom()

    def ax_changed(self,ax):
        old_xlim, old_ylim = self.lim_dict[ax]
        print("old xlim", old_xlim, "ylim", old_ylim)
        print("new xlim", ax.get_xlim(), "ylim", ax.get_ylim())
        return np.all(old_xlim == ax.get_xlim()) and np.all(old_ylim == ax.get_ylim())

    def onrelease(self,event):
        print("Active Toolbar button:",self.histtoolbar._active )
        print("plot release")
        print(event)
        self.static_canvas.flush_events()

        changed_axes     = [ax for ax in self.static_canvas.figure.axes if     self.ax_changed(ax)]
        not_changed_axes = [ax for ax in self.static_canvas.figure.axes if not self.ax_changed(ax)]
        print("changed_axes",changed_axes)
        print("not_changed_axes",not_changed_axes)

        for ax in changed_axes:
            print("Changed xlim", ax.get_xlim(), "ylim", ax.get_ylim())




if __name__ == "__main__":

    epgt2fitparams = lm.Parameters()

    epgt2fitparams.add('T2fat',    value = 180.0, min=0, max=5000, vary=False)
    epgt2fitparams.add('T2muscle', value = 35,    min=0, max=100,  vary=True )
    epgt2fitparams.add('Afat',     value = 0.2,  min=0, max=10,   vary=True )
    epgt2fitparams.add('Amuscle',  value = 0.8,   min=0, max=10,   vary=True )
    epgt2fitparams.add('T1fat',    value = 365.0,                  vary=False)
    epgt2fitparams.add('T1muscle', value = 1400,                   vary=False)
    epgt2fitparams.add('echo',     value = 10.0,                   vary=False)
    qapp = QtWidgets.QApplication(sys.argv)

    app = ApplicationWindow(epgt2fitparams)
    app.show()
    qapp.exec_()

