import wx
import gui
import numpy as np
import cv2

from Camara import WebcamFeed

global Hmin,Hmax,Smax,Smin,Vmax,Vmin,D,E,ImagenEncontrar,ImagenOriginal,figura,label,AreaObjeto,XObjeto
HminSave=[]
HmaxSave=[]
SminSave=[]
SmaxSave=[]
VminSave=[]
VmaxSave=[]
DSave=[]
ESave=[]
"""
The Controller and View class.
It creates an openCV object and on each update retrieves a webcam image from it.
It will then draw the webcam image onto the frame.
"""
class VideoFrame(gui.ProyectoFinal):

    def __init__(self, parent):
        self.parent = parent
        gui.ProyectoFinal.__init__(self, parent)
        globals().update(HminSave=[])
        globals().update(Hmax=self.H_MAX.GetValue())
        globals().update(Hmin=self.H_MIN.GetValue())
        globals().update(Smin=self.S_MIN.GetValue())
        globals().update(Smax=self.S_MAX.GetValue())
        globals().update(Vmin=self.V_MIN.GetValue())
        globals().update(Vmax=self.V_MAX.GetValue())
        globals().update(E=self.erosion.GetValue())
        globals().update(D=self.dilatacion.GetValue())
        """ Create the webcam feed/openCV object  """
        self.webcam = WebcamFeed()
        if not self.webcam.has_webcam():
            print 'Webcam has not been detected.'
            self.Close()

        """ Sets the size based on the webcam image size """
        h, w = self.webcam.size()
        self.SetSize(wx.Size(w, h))

        """ Creates a 30 fps timer for the update loop """
        self.timer = wx.Timer(self)
        self.timer.Start(1000. / 30.)
        self.Bind(wx.EVT_TIMER, self.onUpdate, self.timer)
        self.updating = False

        """ Bind custom paint events """
        self.m_panelVideo.Bind(wx.EVT_ERASE_BACKGROUND, self.onEraseBackground)
        self.m_panelVideo.Bind(wx.EVT_PAINT, self.onPaint)

        """ Bind a custom close event (needed for Windows) """
        self.Bind(wx.EVT_CLOSE, self.onClose)

        """ App states """
        self.STATE_RUNNING = 1
        self.STATE_CLOSING = 2
        self.state = self.STATE_RUNNING

    """ When closing, timer needs to be stopped and frame destroyed """

    def onClose(self, event):
        if not self.state == self.STATE_CLOSING:
            self.state = self.STATE_CLOSING
            self.timer.Stop()
            self.Destroy()

    """ Main Update loop that calls the Paint function """

    def onUpdate(self, event):
        if self.state == self.STATE_RUNNING:
            self.Refresh()

    """ Retrieves a new webcam image and paints it onto the frame """

    def Mensaje(self, msg, title, style):
        dlg = wx.MessageDialog(parent=None, message=msg, caption=title, style=style)
        dlg.ShowModal()
        dlg.Destroy()


    def onPaint(self, event):
        fw, fh = self.m_panelVideo.GetSize()
        ImagenOriginal = self.webcam.get_image(fw, fh)
        ImagenFiltradaBW,ImagenFiltradaView=self.webcam.get_imageHSV(ImagenOriginal,fw,fh,Hmin,Smin,Vmin,Hmax,Smax,Vmax)
        ImagenEroBW,ImagenEro = self.webcam.get_imageEro(ImagenOriginal, ImagenFiltradaBW, E, fw, fh)
        ImagenDilaBW,ImagenDila = self.webcam.get_imageDila(ImagenOriginal, ImagenEroBW, D, fw, fh, 0)
        ImageCmasa,x,y,area=self.webcam.get_centroMasa(ImagenOriginal,ImagenDilaBW,fw,fh)
        globals().update(ImagenOriginal=ImagenOriginal)
        globals().update(Imagenguardar=ImagenDilaBW)
        globals().update(AreaObjeto=area)
        globals().update(XObjeto=x)
        #print (AreaObjeto)


        h, w = ImagenOriginal.shape[:2]
        image = wx.BitmapFromBuffer(w, h, ImagenOriginal)
        image2= wx.BitmapFromBuffer(w,h,ImagenFiltradaView)
        image3=wx.BitmapFromBuffer(w,h,ImagenEro)
        image4=wx.BitmapFromBuffer(w,h,ImagenDila)
        image5=wx.BitmapFromBuffer(w,h,ImageCmasa)
        # Use Buffered Painting to avoid flickering
        dc = wx.BufferedPaintDC(self.m_panelVideo)
        dc.DrawBitmap(image, 0, 0)
        dc2= wx.BufferedPaintDC(self.m_panelVideo2)
        dc2.DrawBitmap(image2, 0, 0)
        dc3 = wx.BufferedPaintDC(self.m_panelVideo3)
        dc3.DrawBitmap(image3, 0, 0)
        dc4 = wx.BufferedPaintDC(self.m_panelVideo4)
        dc4.DrawBitmap(image4, 0, 0)
        dc4 = wx.BufferedPaintDC(self.m_panelVideo5)
        dc4.DrawBitmap(image5, 0, 0)

    def GuardarImagen( self, event ):
        Icontornos,figuraEncontrada = self.webcam.contornos(ImagenOriginal, ImagenEncontrar)
        if figuraEncontrada != 'nada':

            globals().update(label=figuraEncontrada)
            self.selectFigure.SetValue(label)
            self.selectFigure.Append(label)
            HminSave.append(Hmin)
            HmaxSave.append(Hmax)
            SminSave.append(Smin)
            SmaxSave.append(Smax)
            VminSave.append(Vmin)
            VmaxSave.append(Vmax)
            ESave.append(E)
            DSave.append(D)
            self.Mensaje('Figura: '+label, 'Figura Agregada', wx.OK | wx.ICON_INFORMATION)
            #cv2.imshow('objeto',Icontornos)

    def UbicarHSVFigura( self, event ):
        posicion=self.selectFigure.GetSelection()
        globals().update(Hmax=HmaxSave[posicion])
        globals().update(Hmin=HminSave[posicion])
        globals().update(Smin=SminSave[posicion])
        globals().update(Smax=SmaxSave[posicion])
        globals().update(Vmin=VminSave[posicion])
        globals().update(Vmax=VmaxSave[posicion])
        globals().update(E=ESave[posicion])
        globals().update(D=DSave[posicion])
        self.H_MIN.SetValue(Hmin)
        self.H_MAX.SetValue(Hmax)
        self.S_MIN.SetValue(Smin)
        self.S_MAX.SetValue(Smax)
        self.V_MIN.SetValue(Vmin)
        self.V_MAX.SetValue(Vmax)
        self.dilatacion.SetValue(D)
        self.erosion.SetValue(E)

    def StartComunication( self, event ):
        print ('inicio de comunicacion serial')

    def onEraseBackground(self, event):
        return

    def hmax( self, event ):
        globals().update(Hmax=self.H_MAX.GetValue())
        self.Hvalue.SetLabel("H:" + str(Hmin)+ "-"+str(Hmax) )

    def hmin( self, event ):
        globals().update(Hmin=self.H_MIN.GetValue())
        self.Hvalue.SetLabel("H:" + str(Hmin)+ "-"+str(Hmax) )

    def smax(self, event):
        globals().update(Smax=self.S_MAX.GetValue())
        self.Svalue.SetLabel("S:" + str(Smin) + "-" + str(Smax))

    def smin(self, event):
        globals().update(Smin=self.S_MIN.GetValue())
        self.Svalue.SetLabel("S:" + str(Smin) + "-" + str(Smax))

    def vmin( self, event ):
        globals().update(Vmin=self.V_MIN.GetValue())
        self.Vvalue.SetLabel("V:" + str(Vmin) + "-" + str(Vmax))

    def vmax(self, event):
        globals().update(Vmax=self.V_MAX.GetValue())
        self.Vvalue.SetLabel("V:" + str(Vmin) + "-" + str(Vmax))

    def Dilat( self, event ):
        globals().update(D=self.dilatacion.GetValue())
        self.Dvalue.SetLabel("D:"+str(D))

    def Erod( self, event ):
        globals().update(E=self.erosion.GetValue())
        self.Evalue.SetLabel("E:"+str(E))

