# T2EPGviewer
pyQT Dashboard display of MRI T2 EPG muscle data

### Running the main program

```
  python simple_pandas_plot.py
```

![alt text](screenshot.png "Logo Title Text 1")

This progam summarizes the fitting of muscle MRI T2 data. 

It reads in data from a study directory structure that was created from the .

Example data is provided in the studydata directory.

Below is a screenshot of the fileopen dialog showing the data file required to be read in.

![open file directory](openDialog.png "Read in data set" )

### Requirements

The program has been tested on python 3.7

In order for the EPG fitting to work the following module has to be installed

https://github.com/EricHughesABC/epg

pandas
seaborn
matplotlib
lmfit
pydicom

