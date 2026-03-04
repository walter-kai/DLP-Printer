# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"3D Printer", pos = wx.DefaultPosition, size = wx.Size( 831,336 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.AddGrowableCol( 0 )
		fgSizer1.SetFlexibleDirection( wx.VERTICAL )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		settings = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Settings", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		self.m_staticText14.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		settings.Add( self.m_staticText14, 0, wx.ALIGN_CENTER|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticline5 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		settings.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )
		
		gSizer1 = wx.GridSizer( 1, 2, 0, 0 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Resolution (nm)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		gSizer1.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Distance (cm)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		gSizer1.Add( self.m_staticText2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.resolution = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.resolution, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.distance = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		gSizer1.Add( self.distance, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Time of Exposure (s)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		gSizer1.Add( self.m_staticText3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		gSizer1.Add( self.m_staticText4, 0, wx.ALIGN_CENTER|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		self.exposure = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.exposure, 0, wx.ALIGN_CENTER|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		gSizer1.Add( self.m_staticText13, 0, wx.ALL, 5 )
		
		self.Direction = wx.StaticText( self, wx.ID_ANY, u"Direction", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Direction.Wrap( -1 )
		gSizer1.Add( self.Direction, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Instruction", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		gSizer1.Add( self.m_staticText11, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		directionChoices = [ u"Forward", u"Backward" ]
		self.direction = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, directionChoices, 0 )
		self.direction.SetSelection( 0 )
		gSizer1.Add( self.direction, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		instructionChoices = [ u"Move", u"Step Motor w Image", u"Step Motor wo Image", u"Flash Image", wx.EmptyString ]
		self.instruction = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, instructionChoices, 0 )
		self.instruction.SetSelection( 1 )
		gSizer1.Add( self.instruction, 0, wx.ALIGN_CENTER|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		
		settings.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( settings, 1, wx.EXPAND, 5 )
		
		motor = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText71 = wx.StaticText( self, wx.ID_ANY, u"Motor", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )
		self.m_staticText71.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		motor.Add( self.m_staticText71, 0, wx.ALIGN_CENTER|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		motor.Add( self.m_staticline3, 0, wx.EXPAND|wx.ALL, 5 )
		
		gSizer3 = wx.GridSizer( 1, 3, 0, 0 )
		
		self.motor_left = wx.RadioButton( self, wx.ID_ANY, u"Left", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.motor_left, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.motor_both = wx.RadioButton( self, wx.ID_ANY, u"Both", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.motor_both, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.motor_right = wx.RadioButton( self, wx.ID_ANY, u"Right", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.motor_right, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		motor.Add( gSizer3, 1, wx.EXPAND, 5 )
		
		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Sensor", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		self.m_staticText16.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		motor.Add( self.m_staticText16, 0, wx.ALIGN_CENTER|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticline31 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		motor.Add( self.m_staticline31, 0, wx.EXPAND |wx.ALL, 5 )
		
		gSizer4 = wx.GridSizer( 0, 3, 0, 0 )
		
		self.sensor_on = wx.CheckBox( self, wx.ID_ANY, u"Enable", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sensor_on.SetValue(True) 
		gSizer4.Add( self.sensor_on, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.button_calibrate = wx.Button( self, wx.ID_ANY, u"Calibrate Out", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.button_calibrate, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.button_calibrate1 = wx.Button( self, wx.ID_ANY, u"Calibrate In", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.button_calibrate1, 0, wx.ALL, 5 )
		
		
		motor.Add( gSizer4, 1, wx.EXPAND, 5 )
		
		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		motor.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Image to use", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		self.m_staticText7.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		motor.Add( self.m_staticText7, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.image_file = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		motor.Add( self.image_file, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		
		fgSizer1.Add( motor, 1, wx.EXPAND, 5 )
		
		presets = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText131 = wx.StaticText( self, wx.ID_ANY, u"Presets", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText131.Wrap( -1 )
		self.m_staticText131.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		presets.Add( self.m_staticText131, 0, wx.ALIGN_CENTER|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		presets.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		gSizer31 = wx.GridSizer( 0, 3, 0, 0 )
		
		self.button_load = wx.Button( self, wx.ID_ANY, u"Load", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer31.Add( self.button_load, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.button_delete = wx.Button( self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer31.Add( self.button_delete, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.button_save = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer31.Add( self.button_save, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		presets.Add( gSizer31, 1, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
		
		combobox_presetsChoices = []
		self.combobox_presets = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, combobox_presetsChoices, wx.CB_SORT )
		presets.Add( self.combobox_presets, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer1.Add( presets, 1, wx.EXPAND, 5 )
		
		total_time1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Total Time", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		self.m_staticText15.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		total_time1.Add( self.m_staticText15, 0, wx.ALIGN_CENTER|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		total_time1.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.total_time = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_READONLY )
		total_time1.Add( self.total_time, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.button_go = wx.Button( self, wx.ID_ANY, u"Go", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.button_go.SetBackgroundColour( wx.Colour( 66, 255, 66 ) )
		
		gSizer5.Add( self.button_go, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.button_stop = wx.Button( self, wx.ID_ANY, u"Stop!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.button_stop.SetBackgroundColour( wx.Colour( 255, 70, 70 ) )
		
		gSizer5.Add( self.button_stop, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		total_time1.Add( gSizer5, 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( total_time1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.resolution.Bind( wx.EVT_TEXT, self.calculate_time )
		self.distance.Bind( wx.EVT_TEXT, self.calculate_time )
		self.exposure.Bind( wx.EVT_TEXT, self.calculate_time )
		self.button_calibrate.Bind( wx.EVT_BUTTON, self.sensor_calibrate_out )
		self.button_calibrate1.Bind( wx.EVT_BUTTON, self.sensor_calibrate_in )
		self.button_load.Bind( wx.EVT_BUTTON, self.preset_load )
		self.button_delete.Bind( wx.EVT_BUTTON, self.preset_delete )
		self.button_save.Bind( wx.EVT_BUTTON, self.preset_save )
		self.combobox_presets.Bind( wx.EVT_COMBOBOX, self.preset_load )
		self.button_go.Bind( wx.EVT_BUTTON, self.execute_printer )
		self.button_stop.Bind( wx.EVT_BUTTON, self.stop_printer )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def calculate_time( self, event ):
		event.Skip()
	
	
	
	def sensor_calibrate_out( self, event ):
		event.Skip()
	
	def sensor_calibrate_in( self, event ):
		event.Skip()
	
	def preset_load( self, event ):
		event.Skip()
	
	def preset_delete( self, event ):
		event.Skip()
	
	def preset_save( self, event ):
		event.Skip()
	
	
	def execute_printer( self, event ):
		event.Skip()
	
	def stop_printer( self, event ):
		event.Skip()
	

