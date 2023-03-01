import vtkmodules.all as vtk
import os
# try:
#     from vtk.util.vtkImageImportFromArray import *
#     import vtkmodules.all as vtk
#     import SimpleITK as sitk
#     import numpy as np
#     import time
#     import os


# except ImportError:
#     os.system("pip3 install vtk")
#     os.system("pip3 install SimpleITK")
#     os.system("pip3 install numpy")
#     os.system("pip install vtk")
#     os.system("pip install SimpleITK")
#     os.system("pip install numpy")
from vtkmodules.util.vtkImageImportFromArray import *
import SimpleITK as sitk
import numpy as np
import time



os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
np.set_printoptions(threshold=np.inf)
def crop_image(image, new_size, cropmode='center', left_top_point=(0,0)):
    '''
    crop a picture
    :param image: numpy.array, shgape = [H,W,C]
    :param new_size: list (like [H, W, C]), shape = [3]
    :param cropmode: choose from below:
                    'center'
                    'handcraft': need param left_top_point
    :param left_top_point: tuple(like (h,w)), shape = [2]          
    :return: numpy.array, shape = new_size
    '''
    assert (new_size[-1] == image.shape[-1]) &\
           (image.shape[0] >= new_size[0]) &\
           (image.shape[1] >= new_size[1])
    if cropmode == 'center':
        h_top = int((image.shape[0] - new_size[0]) / 2)
        h_bottom = h_top + new_size[0]
        w_left = int((image.shape[1] - new_size[1]) / 2)
        w_right = w_left + new_size[1]
    if cropmode == 'handcraft':
        assert (left_top_point[0] + new_size[0]) <= image.shape[0]
        h_top = left_top_point[0]
        h_bottom = left_top_point[0] + new_size[0]
        assert (left_top_point[1] + new_size[1]) <= image.shape[1]
        w_left = left_top_point[1]
        w_right = left_top_point[1] + new_size[1]
    return image[h_top:h_bottom, w_left:w_right, :] 
def open_nii(filename):
    path = filename 
    ds = sitk.ReadImage(path)  

    #print('ds: ',ds)
    data = sitk.GetArrayFromImage(ds)
    #print(data)
    #input()
    data[data>250]=0
    #data[data==1]=0
    data[data<0]=0

    # print('shape_of_data',data.shape)



    spacing = ds.GetSpacing()       
    # print('spacing_of_data',spacing)

    srange = [np.min(data),np.max(data)]
    # print('shape_of_data_chenged',data.shape)
    img_arr = vtkImageImportFromArray()       

    img_arr.SetArray(data)                          
    img_arr.SetDataSpacing(spacing)                 
    origin = (0,0,0)
    img_arr.SetDataOrigin(origin)
    img_arr.Update()

    32
    # print('spacing: ',spacing)
    # print('srange: ',srange)

    # 键盘控制交互式操作
    class KeyPressInteractorStyle(vtk.vtkInteractorStyleTrackballCamera):
     
        def __init__(self,parent=None):
            self.parent = vtk.vtkRenderWindowInteractor()
            if(parent is not None):
                self.parent = parent
 
            self.AddObserver("KeyPressEvent",self.keyPress)
 
        def keyPress(self,obj,event):
            key = self.parent.GetKeySym()
            if key == 'Up':
            
                gradtfun.AddPoint(-100, 1.0)
                gradtfun.AddPoint(10, 1.0)
                gradtfun.AddPoint(20, 1.0)
            
                volumeProperty.SetGradientOpacity(gradtfun)

                renWin.Render()
            if key == 'Down':
            
            
                tfun.AddPoint(1129, 0)
                tfun.AddPoint(1300.0, 0.1)
                tfun.AddPoint(1600.0, 0.2)
                tfun.AddPoint(2000.0, 0.1)
                tfun.AddPoint(2200.0, 0.1)
                tfun.AddPoint(2500.0, 0.1)
                tfun.AddPoint(2800.0, 0.1)
                tfun.AddPoint(3000.0, 0.1)

                renWin.Render()
    

    def StartInteraction():
        renWin.SetDesiredUpdateRate(10)

    def EndInteraction():
        renWin.SetDesiredUpdateRate(0.001)

    def ClipVolumeRender(obj):
        obj.GetPlanes(planes)
        volumeMapper.SetClippingPlanes(planes)

    

    ren = vtk.vtkRenderer()
    renWin= vtk.vtkRenderWindow()
    renWin.AddRenderer(ren)     
    renWin.AddRenderer(ren)
    iren = vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin) 
    iren.SetInteractorStyle(KeyPressInteractorStyle(parent = iren)) 
    min = srange[0]
    max = srange[1]

    diff = max - min            
    inter = 4200 / diff
    shift = -min
    # print(min, max, inter, shift)  



    shifter = vtk.vtkImageShiftScale()  
    shifter.SetShift(shift)
    shifter.SetScale(inter)
    shifter.SetOutputScalarTypeToUnsignedShort()
    shifter.SetInputData(img_arr.GetOutput())
    shifter.ReleaseDataFlagOff()
    shifter.Update()
    # print(shifter.GetOutput())
    tfun = vtk.vtkPiecewiseFunction()
    tfun.AddPoint(1129, 0)
    tfun.AddPoint(1300.0, 0.00)
    tfun.AddPoint(1600.0, 0.0012)
    tfun.AddPoint(2000.0, 0.0013)
    #tfun.AddPoint(2150.0, 0.14)
    tfun.AddPoint(2200.0, 0.14)
    tfun.AddPoint(2500.0, 0.16)
    tfun.AddPoint(2800.0, 0.17)
    tfun.AddPoint(3000.0, 0.18)

    gradtfun = vtk.vtkPiecewiseFunction()
    gradtfun.AddPoint(-1000, 9)
    gradtfun.AddPoint(0.5, 9.9)
    gradtfun.AddPoint(1, 10)

    ctfun = vtk.vtkColorTransferFunction()
    ctfun.AddRGBPoint(0.0, 0.5, 0.0, 0.0)
    ctfun.AddRGBPoint(600.0, 1.0, 0.5, 0.5)
    ctfun.AddRGBPoint(1280.0, 0.9, 0.2, 0.3)
    ctfun.AddRGBPoint(1960.0, 0.81, 0.27, 0.1)
    ctfun.AddRGBPoint(2200.0, 0.9, 0.2, 0.3)
    ctfun.AddRGBPoint(2500.0, 2.5, 2.0, 0.87)
    #ctfun.AddRGBPoint(3024.0, 0.5, 5, 0.5)

    volumeMapper = vtk.vtkGPUVolumeRayCastMapper()
    volumeMapper.SetInputData(shifter.GetOutput()) 
    volumeProperty = vtk.vtkVolumeProperty()
    actorProperty=vtk.vtkProperty()
    volumeProperty.SetColor(ctfun)  
    volumeProperty.SetScalarOpacity(tfun)
    
    volumeProperty.SetInterpolationTypeToLinear()    
    volumeProperty.ShadeOn()            



    contourfilter=vtk.vtkContourFilter()
    contourfilter.SetInputData(img_arr.GetOutput())
    contourfilter.SetValue(0,100)
    '''
    smooth_filter=vtk.vtkSmoothPolyDataFilter()
    smooth_filter.SetInputConnection(contourfilter.GetOutputPort())
    smooth_filter.SetNumberOfIterations(20)
    smooth_filter.SetFeatureEdgeSmoothing(True);
    smooth_filter.SetBoundarySmoothing(True); 
    smooth_filter.Update()
    '''
    mapper_poly=vtk.vtkPolyDataMapper()
    mapper_poly.SetInputConnection( contourfilter.GetOutputPort())
    newvol = vtk.vtkVolume()
    newvol.SetMapper(volumeMapper)
    newvol.SetProperty(volumeProperty)


    actor=vtk.vtkActor()
    actor.SetMapper(mapper_poly)
    actor.GetProperty().SetOpacity(0.6)
    return newvol,mapper_poly
#open_nii("\segmentation.nii.gz")