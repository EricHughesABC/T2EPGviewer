# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 14:55:05 2018

@author: ERIC
"""
import os
import numpy as np
import pandas as pd
import nibabel

class T2imageData():

    def __init__(self):

        self.currentSlice = None
        self.currentEcho = None

        self.T2imagesDirpath     = None
        self.dixonImagesDirpath  = None
        self.dixonResultsDirpath = None
        self.T2resultsDirpath    = None

        self.root         = None

        self.studyName    = None
        self.subject      = None
        self.session      = None
        self.imagedRegion = None
        self.protocol     = None
        self.results      = None
        self.roiType      = None
        self.fitModel     = None

        self.imagedRegionType = self.roiType

        self.T2imageType = None
        self.T2MRIimageFilenameAndPath = ""

        self.dixonImageType = None
        self.dixonMRIimageFilenameAndPath = ""

        self.T2resultsFilenameAndPath = ""
        self.dixonResultsFilenameAndPath = ""

        self.fittingParam = "T2m"

        self.numRowsT2 = None
        self.numColsT2 = None
        self.numSlicesT2 = None
        self.numEchoesT2 = None

        self.dixonSlices = None
        self.T2slices = None

        self.ImageDataT2 = None
        self.mriSliceIMG = None



    def readin_alldata_from_results_filename(self, fn):

        print("inside readin_alldata_from_results_filename")

        self.set_dataDir_and_results_filenames(fn)
        self.set_T2imageData_filename_and_type()
        self.set_dixonImageData_filename_and_type()

        print("T2resultsDirpath ::            ",self.T2resultsDirpath)
        print("dixonResultsDirpath ::         ", self.dixonResultsDirpath)
        print("T2imagesDirpath ::             ", self.T2imagesDirpath)
        print("dixonImagesDirpath ::          ", self.dixonImagesDirpath)
        print("T2imageType ::                 ", self.T2imageType)
        print("T2MRIimageFilenameAndPath ::   ", self.T2MRIimageFilenameAndPath)
        print("dixonImageType ::              ", self.dixonImageType)
        print("dixonMRIimageFilenameAndPath ::", self.dixonMRIimageFilenameAndPath)
        print("T2resultsFilenameAndPath ::    ", self.T2resultsFilenameAndPath)
        print("dixonResultsFilenameAndPath :: ", self.dixonResultsFilenameAndPath)


    def set_T2imageData_filename_and_type(self):

        """Searches for image data in directory
        can be nifti or analyze sets the type and filename"""

        print("inside set_T2imageData_filename_and_type")

        print("self.T2imagesDirpath", self.T2imagesDirpath)

        if self.T2imagesDirpath == None:
            self.T2imageType = None
            return False
        else:
            imgFilenameList = [ os.path.join(self.T2imagesDirpath,fn)
                                 for fn in os.listdir(self.T2imagesDirpath)
                                 if "nii" in fn or "img" in fn]

            if len(imgFilenameList) == 0:
                self.T2imageType = None
                self.T2MRIimageFilenameAndPath = None
                return False
            else:
                self.T2MRIimageFilenameAndPath = imgFilenameList[0]
                if "nii" in self.T2MRIimageFilenameAndPath:
                    self.T2imageType = "nifti"
                else:
                    self.T2imageType = "analyze"

                return True


    def set_dixonImageData_filename_and_type(self):

        """Searches for image data in directory
        can be nifti or analyze sets the type and filename
        filename must have fatPC. in it"""

        print( "inside set_dixonImageData_filename_and_type")

        print("self.dixonImagesDirpath",self.dixonImagesDirpath)

        if self.dixonImagesDirpath == None:
            self.dionImageType = None
            return False
        else:
            imgFilenameList = [ os.path.join(self.dixonImagesDirpath,fn)
                                 for fn in os.listdir(self.dixonImagesDirpath)
                                 if "fatPC." in fn and ("nii" in fn or "img" in fn)]

            if len(imgFilenameList) == 0:
                self.dixonImageType = None
                self.dixonMRIimageFilenameAndPath = None
                return False
            else:
                self.dixonMRIimageFilenameAndPath = imgFilenameList[0]
                if "nii" in self.dixonMRIimageFilenameAndPath:
                    self.dixonImageType = "nifti"
                else:
                    self.dixonImageType = "analyze"

                return True


    def set_results_dir(self,protocol,  resultsDir):

        resultsDirpath = None

#         resultsDirpath1 = resultsDir

        dirpath = os.path.join(self.root,self.studyName,self.subject,self.session,
                               self.imagedRegion,protocol, self.results,self.roiType,self.fitModel)
        if os.path.exists(dirpath):
            resultsDirpath = dirpath
        else:
            dirpath = os.path.join(self.root,self.studyName,self.subject,self.session,
                                   self.imagedRegion,protocol, self.results,self.roiType)
            if os.path.exists(dirpath):
                fitModels = [f for f in os.listdir(dirpath)]
                if len(fitModels)> 0:
                    resultsDirpath = os.path.join(dirpath, fitModels[0])

        return resultsDir, resultsDirpath



    def set_dataDir_and_results_filenames( self, fn):

        print("inside set_dataDir_and_results_filenames")
        print("fn", fn)

        resultsDir, resultsFilename = os.path.split(fn)
        resultsDirList = resultsDir.split(os.path.sep)

        sessionIndex =  [ i for i,w in  enumerate(resultsDirList) if "sess" in w]

        if len(sessionIndex):
            si = sessionIndex[0]

            print(resultsDirList[0],resultsDirList[0][-1])

            if ":" == resultsDirList[0][-1]:  # add path seperator if root ends in :
                resultsDirList[0] = resultsDirList[0]+os.path.sep

            print("resultsDirList[0]", resultsDirList[0])


            self.root = os.path.sep.join(resultsDirList[:si-2])

            self.studyName    = resultsDirList[si-2]
            self.subject      = resultsDirList[si-1]
            self.session      = resultsDirList[si]
            self.imagedRegion = resultsDirList[si+1]
            self.protocol     = resultsDirList[si+2]
            self.results      = resultsDirList[si+3]
            self.roiType      = imagedRegionType = resultsDirList[si+4]
            self.fitModel     = resultsDirList[si+5]

            print("self.root",self.root)

            ### create directory paths to  T2 and Dixon results and image path

            #     T2_images_dirPath
            #     dixon_images_dirPath
            #     dixon_results_dirPath
            #     T2_results_dirPath

            ## T2 image path

            dirpath = os.path.join(self.root,self.studyName,self.subject,
                                   self.session,self.imagedRegion,"T2")
            if os.path.exists(dirpath):
                self.T2imagesDirpath = dirpath

            ## dixon image path

            dirpath = os.path.join(self.root,self.studyName,self.subject,self.session,
                                   self.imagedRegion,"dixon")
            if os.path.exists(dirpath):
                self.dixonImagesDirpath = dirpath

            ## set T2 and dixon results path

            if self.protocol.lower() == "t2":
                self.T2resultsDirpath, self.dixonResultsDirpath, = self.set_results_dir("dixon", resultsDir)

            elif self.protocol.lower() == "dixon":
                self.dixonResultsDirpath, self.T2resultsDirpath, = self.set_results_dir("T2",  resultsDir)

            print("self.dixonResultsDirpath", self.dixonResultsDirpath)
            print("self.T2resultsDirpath", self.T2resultsDirpath)
            ## set csv results path name for T2 and dixon

            if "T2".lower() in fn.lower():
                self.T2resultsFilenameAndPath = fn

                resultFilenameList = [ os.path.join(self.dixonResultsDirpath,fi)
                                         for fi in os.listdir(self.dixonResultsDirpath)
                                         if "results." in fi.lower() and (".csv" in fi.lower() )]
                if resultFilenameList:
                    self.dixonResultsFilenameAndPath = resultFilenameList[0]

            elif "dixon" in fn.lower():
                self.dixonResultsFilenameAndPath = fn

                resultFilenameList = [ os.path.join(self.T2resultsDirpath,fi)
                                         for fi in os.listdir(self.T2ResultsDirpath)
                                         if "results." in fi.lower() and (".csv" in fi.lower() )]
                if resultFilenameList:
                    self.T2resultsFilenameAndPath = resultFilenameList[0]





    def read_T2_data(self):
        print("read_T2_data function entered")
        if os.path.exists(self.T2resultsFilenameAndPath):
            self.t2_data_summary_df = pd.read_csv(self.T2resultsFilenameAndPath)
            self.T2slices = list(self.t2_data_summary_df["slice"].unique())
            return(True)
        else:
            print(self.T2resultsFilenameAndPath, "not Found" )
            return(False)

    def read_Dixon_data(self):
        print("read_Dixon_data function entered")
        if os.path.exists(self.dixonResultsFilenameAndPath):
            self.dixon_data_summary_df = pd.read_csv(self.dixonResultsFilenameAndPath)
            self.dixonSlices = list(self.dixon_data_summary_df["slice"].unique())
            return(True)
        else:
            print(self.dixonResultsFilenameAndPath, "not Found" )
            self.dixon_data_summary_df = pd.DataFrame()
            return(False)



    def read_T2_img_hdr_files(self):
        if os.path.exists(self.T2MRIimageFilenameAndPath):
            print(self.T2MRIimageFilenameAndPath, " found")
            self.t2_imghdr = nibabel.load(self.T2MRIimageFilenameAndPath)

            image_data = self.t2_imghdr.get_data()

            image_data = np.flipud(image_data.swapaxes(1,0))


            self.update_imageDataT2(image_data)
            [self.numRowsT2, self.numColsT2, self.numSlicesT2, self.numEchoesT2] = self.ImageDataT2.shape

#            self.img1 = np.zeros((self.numRowsT2, self.numColsT2,3), dtype=np.double)
            self.mriSliceIMG = np.zeros((self.numRowsT2, self.numColsT2), dtype=np.double)

#            self.img1[:,:,0] = self.ImageDataT2[:,:,0,0]/(self.ImageDataT2[:,:,0,0].max()*2)
#            self.img1[:,:,0] = self.ImageDataT2[:,:,0,0]
            self.mriSliceIMG = self.ImageDataT2[:,:,0,0]*1.0

            self.currentEcho = 0
            self.currentSlice = 0

#            mainWindow.setWindowTitle(self.study_name)
            return(True)
        else:
            return(False)



    def update_imageDataT2(self, imageData):
        self.ImageDataT2 = imageData






    def overlayRoisOnImage(self, slice_pos, roi_data):

        print("Entering overlayRoisOnImage", slice_pos)
        print("roi_data",roi_data)

        if roi_data in self.t2_data_summary_df.columns:


            roi_image_layer = np.zeros(self.numRowsT2*self.numColsT2)

            t2_data_query_df = self.t2_data_summary_df.query('slice == {}'.format(str(slice_pos)))

            roi_image_layer[t2_data_query_df.pixel_index] = t2_data_query_df[roi_data]

            self.maskedROIs = np.ma.masked_where(roi_image_layer == 0, roi_image_layer)

        elif roi_data in self.dixon_data_summary_df.columns:

#            print("slice_pos", slice_pos)
#            print("self.T2slices.index(slice_pos)",self.T2slices.index(slice_pos))
#            print("self.dixonSlices[self.T2slices.index(slice_pos)]",self.dixonSlices[self.T2slices.index(slice_pos)])

            if slice_pos in self.T2slices:
                dixon_slice = self.dixonSlices[self.T2slices.index(slice_pos)]
            else:
                dixon_slice = slice_pos

            roi_image_layer = np.zeros(self.numRowsT2*self.numColsT2)

            #df_t2 = self.t2_data_summary_df[roi_data, 'pixel_index','roi'].groupby('slice')
            dixon_data_query_df = self.dixon_data_summary_df.query('slice == {}'.format(str(dixon_slice)))

#            roi_image_layer[dixon_data_query_df.pixels] = dixon_data_query_df[roi_data]/dixon_data_query_df[roi_data].max()
            roi_image_layer[dixon_data_query_df.pixel_index] = dixon_data_query_df[roi_data]

#            self.img1[:,:,2] =  roi_image_layer.reshape((self.numRowsT2,self.numColsT2))
            self.maskedROIs = np.ma.masked_where(roi_image_layer == 0, roi_image_layer)



