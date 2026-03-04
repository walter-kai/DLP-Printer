///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Jun  5 2014)
// http://www.wxformbuilder.org/
//
// PLEASE DO "NOT" EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#ifndef __NONAME_H__
#define __NONAME_H__

#include <wx/artprov.h>
#include <wx/xrc/xmlres.h>
#include <wx/string.h>
#include <wx/button.h>
#include <wx/gdicmn.h>
#include <wx/font.h>
#include <wx/colour.h>
#include <wx/settings.h>
#include <wx/textctrl.h>
#include <wx/stattext.h>
#include <wx/sizer.h>
#include <wx/frame.h>

///////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////
/// Class MainFrame
///////////////////////////////////////////////////////////////////////////////
class MainFrame : public wxFrame 
{
	private:
	
	protected:
		wxButton* m_button1;
		wxTextCtrl* resolution;
		wxStaticText* m_staticText1;
		wxTextCtrl* offset;
		wxStaticText* m_staticText2;
		wxTextCtrl* exposure;
		wxStaticText* m_staticText3;
		wxTextCtrl* m_textCtrl4;
		wxStaticText* m_staticText4;
		wxStaticText* total_time;
		wxStaticText* m_staticText6;
		
		// Virtual event handlers, overide them in your derived class
		virtual void calculate_time( wxCommandEvent& event ) { event.Skip(); }
		
	
	public:
		
		MainFrame( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxEmptyString, const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 697,669 ), long style = wxDEFAULT_FRAME_STYLE|wxSTAY_ON_TOP|wxTAB_TRAVERSAL );
		
		~MainFrame();
	
};

#endif //__NONAME_H__
