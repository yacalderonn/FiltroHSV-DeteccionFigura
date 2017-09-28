# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Feb 16 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class ProyectoFinal
###########################################################################

class ProyectoFinal ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Proyecto Final DSPII", pos = wx.DefaultPosition, size = wx.Size( 980,570 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 980,570 ), wx.Size( 980,570 ) )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer1 = wx.FlexGridSizer( 2, 3, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Filtro De Color", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		self.m_staticText2.SetFont( wx.Font( 10, 70, 90, 92, False, "Arial" ) )
		
		bSizer3.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		fgSizer5 = wx.FlexGridSizer( 15, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer5.SetMinSize( wx.Size( 310,1 ) ) 
		selectFigureChoices = []
		self.selectFigure = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,25 ), selectFigureChoices, 0 )
		self.selectFigure.SetSelection( 0 )
		fgSizer5.Add( self.selectFigure, 0, wx.ALL, 5 )
		
		self.Find = wx.Button( self, wx.ID_ANY, u"Encontrar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.Find, 0, wx.ALL, 5 )
		
		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer5.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer5.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		fgSizer3 = wx.FlexGridSizer( 6, 3, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Minimo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		self.m_staticText14.SetFont( wx.Font( 9, 70, 90, 90, False, "Arial" ) )
		
		fgSizer3.Add( self.m_staticText14, 0, wx.ALL, 5 )
		
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Maximo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		self.m_staticText15.SetFont( wx.Font( 9, 70, 90, 90, False, "Arial" ) )
		
		fgSizer3.Add( self.m_staticText15, 0, wx.ALL, 5 )
		
		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"H", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		self.m_staticText16.SetFont( wx.Font( 10, 70, 90, 90, False, "Arial" ) )
		
		fgSizer3.Add( self.m_staticText16, 0, wx.ALL, 5 )
		
		self.H_MIN = wx.Slider( self, wx.ID_ANY, 0, 0, 255, wx.DefaultPosition, wx.Size( 80,25 ), wx.SL_HORIZONTAL )
		fgSizer3.Add( self.H_MIN, 0, wx.ALL, 5 )
		
		self.H_MAX = wx.Slider( self, wx.ID_ANY, 255, 0, 255, wx.DefaultPosition, wx.Size( 80,25 ), wx.SL_HORIZONTAL )
		fgSizer3.Add( self.H_MAX, 0, wx.ALL, 5 )
		
		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"S", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		fgSizer3.Add( self.m_staticText17, 0, wx.ALL, 5 )
		
		self.S_MIN = wx.Slider( self, wx.ID_ANY, 0, 0, 255, wx.DefaultPosition, wx.Size( 80,25 ), wx.SL_HORIZONTAL )
		fgSizer3.Add( self.S_MIN, 0, wx.ALL, 5 )
		
		self.S_MAX = wx.Slider( self, wx.ID_ANY, 255, 0, 255, wx.DefaultPosition, wx.Size( 80,25 ), wx.SL_HORIZONTAL )
		fgSizer3.Add( self.S_MAX, 0, wx.ALL, 5 )
		
		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"V", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		fgSizer3.Add( self.m_staticText18, 0, wx.ALL, 5 )
		
		self.V_MIN = wx.Slider( self, wx.ID_ANY, 0, 0, 255, wx.DefaultPosition, wx.Size( 80,25 ), wx.SL_HORIZONTAL )
		fgSizer3.Add( self.V_MIN, 0, wx.ALL, 5 )
		
		self.V_MAX = wx.Slider( self, wx.ID_ANY, 255, 0, 255, wx.DefaultPosition, wx.Size( 80,25 ), wx.SL_HORIZONTAL )
		fgSizer3.Add( self.V_MAX, 0, wx.ALL, 5 )
		
		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"D", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		fgSizer3.Add( self.m_staticText19, 0, wx.ALL, 5 )
		
		self.dilatacion = wx.Slider( self, wx.ID_ANY, 1, 1, 15, wx.DefaultPosition, wx.Size( 80,25 ), wx.SL_HORIZONTAL )
		fgSizer3.Add( self.dilatacion, 0, wx.ALL, 5 )
		
		
		fgSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"E", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		fgSizer3.Add( self.m_staticText20, 0, wx.ALL, 5 )
		
		self.erosion = wx.Slider( self, wx.ID_ANY, 1, 1, 15, wx.DefaultPosition, wx.Size( 80,25 ), wx.SL_HORIZONTAL )
		fgSizer3.Add( self.erosion, 0, wx.ALL, 5 )
		
		self.startButton = wx.Button( self, wx.ID_ANY, u"Iniciar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.startButton, 0, wx.ALL, 5 )
		
		
		fgSizer5.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer10.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer10.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer10.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.Hvalue = wx.StaticText( self, wx.ID_ANY, u"H:0-255", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Hvalue.Wrap( -1 )
		self.Hvalue.SetFont( wx.Font( 10, 70, 90, 90, False, "Arial" ) )
		
		bSizer10.Add( self.Hvalue, 0, wx.ALL, 5 )
		
		
		bSizer10.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.Svalue = wx.StaticText( self, wx.ID_ANY, u"S:0-255", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Svalue.Wrap( -1 )
		self.Svalue.SetFont( wx.Font( 10, 70, 90, 90, False, "Arial" ) )
		
		bSizer10.Add( self.Svalue, 0, wx.ALL, 5 )
		
		
		bSizer10.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.Vvalue = wx.StaticText( self, wx.ID_ANY, u"V:0-255", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Vvalue.Wrap( -1 )
		self.Vvalue.SetFont( wx.Font( 10, 70, 90, 90, False, "Arial" ) )
		
		bSizer10.Add( self.Vvalue, 0, wx.ALL, 5 )
		
		
		bSizer10.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.Dvalue = wx.StaticText( self, wx.ID_ANY, u"D:1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Dvalue.Wrap( -1 )
		self.Dvalue.SetFont( wx.Font( 10, 70, 90, 90, False, "Arial" ) )
		
		bSizer10.Add( self.Dvalue, 0, wx.ALL, 5 )
		
		
		bSizer10.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.Evalue = wx.StaticText( self, wx.ID_ANY, u"E:1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Evalue.Wrap( -1 )
		self.Evalue.SetFont( wx.Font( 10, 70, 90, 90, False, "Arial" ) )
		
		bSizer10.Add( self.Evalue, 0, wx.ALL, 5 )
		
		
		bSizer10.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer5.Add( bSizer10, 1, wx.EXPAND, 5 )
		
		
		bSizer3.Add( fgSizer5, 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Imagen Original", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		self.m_staticText3.SetFont( wx.Font( 10, 70, 90, 92, False, "Arial" ) )
		
		bSizer4.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.m_panelVideo = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 310,230 ), wx.TAB_TRAVERSAL )
		self.m_panelVideo.SetMinSize( wx.Size( 310,230 ) )
		self.m_panelVideo.SetMaxSize( wx.Size( 310,230 ) )
		
		bSizer4.Add( self.m_panelVideo, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		fgSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Imagen Filtrada HSV", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		self.m_staticText31.SetFont( wx.Font( 10, 70, 90, 92, False, "Arial" ) )
		
		bSizer5.Add( self.m_staticText31, 0, wx.ALL, 5 )
		
		self.m_panelVideo2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 310,230 ), wx.TAB_TRAVERSAL )
		self.m_panelVideo2.SetMinSize( wx.Size( 310,230 ) )
		self.m_panelVideo2.SetMaxSize( wx.Size( 310,230 ) )
		
		bSizer5.Add( self.m_panelVideo2, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		fgSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u"Imagen Erosionada", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )
		self.m_staticText32.SetFont( wx.Font( 10, 70, 90, 92, False, "Arial" ) )
		
		bSizer6.Add( self.m_staticText32, 0, wx.ALL, 5 )
		
		self.m_panelVideo3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 310,230 ), wx.TAB_TRAVERSAL )
		self.m_panelVideo3.SetMinSize( wx.Size( 310,230 ) )
		self.m_panelVideo3.SetMaxSize( wx.Size( 310,230 ) )
		
		bSizer6.Add( self.m_panelVideo3, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		fgSizer1.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Imagen Dilatada", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )
		self.m_staticText33.SetFont( wx.Font( 10, 70, 90, 92, False, "Arial" ) )
		
		bSizer7.Add( self.m_staticText33, 0, wx.ALL, 5 )
		
		self.m_panelVideo4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 310,230 ), wx.TAB_TRAVERSAL )
		self.m_panelVideo4.SetMinSize( wx.Size( 310,230 ) )
		self.m_panelVideo4.SetMaxSize( wx.Size( 310,230 ) )
		
		bSizer7.Add( self.m_panelVideo4, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		fgSizer1.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u"Detección De Objeto", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )
		self.m_staticText34.SetFont( wx.Font( 10, 70, 90, 92, False, "Arial" ) )
		
		bSizer8.Add( self.m_staticText34, 0, wx.ALL, 5 )
		
		self.m_panelVideo5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 310,230 ), wx.TAB_TRAVERSAL )
		self.m_panelVideo5.SetMinSize( wx.Size( 310,230 ) )
		self.m_panelVideo5.SetMaxSize( wx.Size( 310,230 ) )
		
		bSizer8.Add( self.m_panelVideo5, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		fgSizer1.Add( bSizer8, 1, wx.EXPAND, 5 )
		
		
		bSizer2.Add( fgSizer1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.selectFigure.Bind( wx.EVT_COMBOBOX, self.UbicarHSVFigura )
		self.Find.Bind( wx.EVT_BUTTON, self.GuardarImagen )
		self.H_MIN.Bind( wx.EVT_SCROLL, self.hmin )
		self.H_MAX.Bind( wx.EVT_SCROLL, self.hmax )
		self.S_MIN.Bind( wx.EVT_SCROLL, self.smin )
		self.S_MAX.Bind( wx.EVT_SCROLL, self.smax )
		self.V_MIN.Bind( wx.EVT_SCROLL, self.vmin )
		self.V_MAX.Bind( wx.EVT_SCROLL, self.vmax )
		self.dilatacion.Bind( wx.EVT_SCROLL, self.Dilat )
		self.erosion.Bind( wx.EVT_SCROLL, self.Erod )
		self.startButton.Bind( wx.EVT_BUTTON, self.StartComunication )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def UbicarHSVFigura( self, event ):
		event.Skip()
	
	def GuardarImagen( self, event ):
		event.Skip()
	
	def hmin( self, event ):
		event.Skip()
	
	def hmax( self, event ):
		event.Skip()
	
	def smin( self, event ):
		event.Skip()
	
	def smax( self, event ):
		event.Skip()
	
	def vmin( self, event ):
		event.Skip()
	
	def vmax( self, event ):
		event.Skip()
	
	def Dilat( self, event ):
		event.Skip()
	
	def Erod( self, event ):
		event.Skip()
	
	def StartComunication( self, event ):
		event.Skip()
	

