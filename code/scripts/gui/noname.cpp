///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Jun  5 2014)
// http://www.wxformbuilder.org/
//
// PLEASE DO "NOT" EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "noname.h"

///////////////////////////////////////////////////////////////////////////

MainFrame::MainFrame( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );
	
	wxBoxSizer* bSizer1;
	bSizer1 = new wxBoxSizer( wxVERTICAL );
	
	m_button1 = new wxButton( this, wxID_ANY, wxT("MyButton"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer1->Add( m_button1, 0, wxALL, 5 );
	
	resolution = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer1->Add( resolution, 0, wxALL, 5 );
	
	m_staticText1 = new wxStaticText( this, wxID_ANY, wxT("Resolution (nm)"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText1->Wrap( -1 );
	bSizer1->Add( m_staticText1, 0, wxALL, 5 );
	
	offset = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer1->Add( offset, 0, wxALL, 5 );
	
	m_staticText2 = new wxStaticText( this, wxID_ANY, wxT("Offset (cm)"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText2->Wrap( -1 );
	bSizer1->Add( m_staticText2, 0, wxALL, 5 );
	
	exposure = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer1->Add( exposure, 0, wxALL, 5 );
	
	m_staticText3 = new wxStaticText( this, wxID_ANY, wxT("Time of Exposure (s)"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText3->Wrap( -1 );
	bSizer1->Add( m_staticText3, 0, wxALL, 5 );
	
	m_textCtrl4 = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer1->Add( m_textCtrl4, 0, wxALL, 5 );
	
	m_staticText4 = new wxStaticText( this, wxID_ANY, wxT("Length (cm) [temporary]"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText4->Wrap( -1 );
	bSizer1->Add( m_staticText4, 0, wxALL, 5 );
	
	total_time = new wxStaticText( this, wxID_ANY, wxT("time"), wxDefaultPosition, wxDefaultSize, 0 );
	total_time->Wrap( -1 );
	bSizer1->Add( total_time, 0, wxALL, 5 );
	
	m_staticText6 = new wxStaticText( this, wxID_ANY, wxT("Total Time (s)"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText6->Wrap( -1 );
	bSizer1->Add( m_staticText6, 0, wxALL, 5 );
	
	
	this->SetSizer( bSizer1 );
	this->Layout();
	
	this->Centre( wxBOTH );
	
	// Connect Events
	resolution->Connect( wxEVT_COMMAND_TEXT_UPDATED, wxCommandEventHandler( MainFrame::calculate_time ), NULL, this );
	offset->Connect( wxEVT_COMMAND_TEXT_UPDATED, wxCommandEventHandler( MainFrame::calculate_time ), NULL, this );
	exposure->Connect( wxEVT_COMMAND_TEXT_UPDATED, wxCommandEventHandler( MainFrame::calculate_time ), NULL, this );
	m_textCtrl4->Connect( wxEVT_COMMAND_TEXT_UPDATED, wxCommandEventHandler( MainFrame::calculate_time ), NULL, this );
}

MainFrame::~MainFrame()
{
	// Disconnect Events
	resolution->Disconnect( wxEVT_COMMAND_TEXT_UPDATED, wxCommandEventHandler( MainFrame::calculate_time ), NULL, this );
	offset->Disconnect( wxEVT_COMMAND_TEXT_UPDATED, wxCommandEventHandler( MainFrame::calculate_time ), NULL, this );
	exposure->Disconnect( wxEVT_COMMAND_TEXT_UPDATED, wxCommandEventHandler( MainFrame::calculate_time ), NULL, this );
	m_textCtrl4->Disconnect( wxEVT_COMMAND_TEXT_UPDATED, wxCommandEventHandler( MainFrame::calculate_time ), NULL, this );
	
}
