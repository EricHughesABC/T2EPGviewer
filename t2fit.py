# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 11:30:41 2018

@author: ERIC
"""
import numpy as np
import lmfit
from epg import cpmg_epg_b1 as cpmg_epg_b1_c

from scipy import integrate

mxyz90 = np.fromfile( 'epg\mxyz90.txt', sep=' ' )
mxyz180 = np.fromfile('epg\mxyz180.txt', sep=' ')

mxyz90 = mxyz90.reshape(5,512)
mxyz180 = mxyz180.reshape(5,512)

offset=130
step=10
epg_slice_xxx =mxyz90[0][offset:-offset+step:step] # mm
epg_p90 = mxyz90[-1][offset:-offset+step:step]     # degrees
epg_p180 = mxyz180[-1][offset:-offset+step:step]   # degrees
epg_dx=epg_slice_xxx[1]-epg_slice_xxx[0]


def fit_cpmg_epg_muscle_philips_hargreaves_c( params,  xxx,  dx, p90_array, p180_array, yyy_exp=None):

    parvals  = params.valuesdict()

    T1fat    = parvals[ 'T1fat' ]      # fixed
    T1muscle = parvals[ 'T1muscle' ]      # fixed
    echo     = parvals[ 'echo' ]     # fixed
    T2fat    = parvals[ 'T2fat' ]     # fixed/optimized
    T2muscle = parvals['T2muscle']       # optimized
    Afat     = parvals[ 'Afat']       # optimized
    Amuscle  = parvals['Amuscle']        # optimized
    B1scale  = parvals['B1scale']

    Nechos = len(xxx)
    Ngauss = len(p90_array)

    signal        = np.zeros([Ngauss,Nechos])
    fat_signal    = np.zeros(Nechos)
    muscle_signal = np.zeros(Nechos)

    for i,(p90,p180) in enumerate(zip(p90_array,p180_array)):

        cpmg_epg_b1_c( fat_signal,    p90, p180, T1fat,    T2fat,    echo, B1scale )
        cpmg_epg_b1_c( muscle_signal, p90, p180, T1muscle, T2muscle, echo, B1scale )

        signal[i] = Afat*fat_signal+Amuscle*muscle_signal

    int_signal = integrate.simps(signal, dx=dx,axis=0)
    if isinstance(yyy_exp, np.ndarray):
        return( int_signal-yyy_exp)
    else:
        return(int_signal)



def calculate_T2values_on_slice_muscleEPG(lmparams, yyy_exp):

#    params = lmfit.Parameters()
#    params.add('T2fat',    value = 180.0, min=0, max=5000, vary=False)
#    params.add('T2muscle', value = 35,    min=0, max=100,  vary=True )
#    params.add('Afat',     value = 0.01,  min=0, max=10,   vary=True )
#    params.add('Amuscle',  value = 0.1,   min=0, max=10,   vary=True )
#    params.add('T1fat',    value = 365.0,                  vary=False)
#    params.add('T1muscle', value = 1400,                   vary=False)
#    params.add('echo',     value = 10.0,                   vary=False)

    params = lmparams['epgt2fitparams']
    echo_time = params['echo'].value
    num_echoes = yyy_exp.size

    parvals  = params.valuesdict()

    print("parvals")
    for k,v in parvals.items():
        print(k,v)

    print("EPG echo time =", echo_time)
    xxx = np.linspace( echo_time, echo_time*num_echoes, num_echoes)
    dx = xxx[1]-xxx[0]


    yyy_exp_max =yyy_exp.max()
    if yyy_exp_max == 0:
        yyy_exp_max = 1.0
    yyy_exp_norm = yyy_exp/yyy_exp_max

    fitModel = lmfit.Minimizer(fit_cpmg_epg_muscle_philips_hargreaves_c, lmparams['epgt2fitparams'], fcn_args=( xxx, dx,  epg_p90, epg_p180, yyy_exp_norm))
    results = fitModel.minimize()

    fit_plot = np.zeros(num_echoes)

    if results.success:
        fit_plot = results.residual + yyy_exp_norm

    return( fit_plot, yyy_exp_norm, results, xxx)




def calculate_T2values_on_slice_muscleAzz(lmparams, yyy_exp):

    params = lmparams['azzt2fitparams']
    echo_time = params['echo'].value
    num_echoes = yyy_exp.size

    model  = lmfit.models.ExpressionModel('Afat * (c_l*exp(-x/t2_fl)+c_s*exp(-x/t2_fs)) + Amuscle * (exp(-x/T2muscle))')

    parvals  = params.valuesdict()
    print("parvals")
    for k,v in parvals.items():
        print(k,v)

    print("azzabou  echo time", echo_time)

#    saved_output = {'T2muscle_value': [],
#                    'T2muscle_stderr': [],
#                     'Amuscle_value': [],
#                    'Amuscle_stderr': [],
#                     'Afat_value': [],
#                    'Afat_stderr': [],
#                    'chisqr': [],
#                    'redchi':[],
#                    'AIC':[],
#                    'BIC':[],
#                    'slice':[],
#                    'pixel_index':[],
#               }

    xxx = np.linspace( echo_time, echo_time*num_echoes, num_echoes)


    yyy_exp_max = yyy_exp.max()
    fit_plot = np.zeros(num_echoes-2)
    if yyy_exp_max == 0.0:
        yyy_exp_max = 1.0
    yyy_exp_norm = yyy_exp/yyy_exp_max


    print("fitting data")

    results = model.fit(yyy_exp_norm[2:] , x=xxx[2:], params=lmparams['azzt2fitparams'])
    #mi.plot()
    #saved_output['name'].append('t2_m')
#    saved_output['T2muscle_value'].append(results.params['T2muscle'].value)
#    saved_output['T2muscle_stderr'].append(results.params['T2muscle'].stderr)
#    saved_output['chisqr'].append(results.chisqr)
#    saved_output['redchi'].append(results.redchi)
#    saved_output['AIC'].append(results.aic)
#    saved_output['BIC'].append(results.bic)
#
#
#    saved_output['Amuscle_value'].append(results.params['Amuscle'].value)
#    saved_output['Amuscle_stderr'].append(results.params['Amuscle'].stderr)

#    saved_output['Afat_value'].append(results.params['Afat'].value)
#    saved_output['Afat_stderr'].append(results.params['Afat'].stderr)

    fit_plot = results.residual + yyy_exp_norm[2:]

    return(  fit_plot, yyy_exp_norm, results, xxx)