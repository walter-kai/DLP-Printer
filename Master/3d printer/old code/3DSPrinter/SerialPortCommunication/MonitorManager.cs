using System;
using System.Collections.Generic;
using System.Text;
using System.Windows.Forms;
using System.Drawing;

namespace PCComm
{
    class MonitorManager
    {
        private Form[] _monitors;
        private int _monitorIndex;
        private Screen[] _screens;
        private Image _defaultImage;
        private Image _printImage;
        private bool _isExtended;

        public MonitorManager(String defaultImagePath, String printImagePath)
        {           
            try
            {
                _monitors = new Form[Screen.AllScreens.Length];
                _monitorIndex = 0;
                _isExtended = false;

                _defaultImage = Image.FromFile(defaultImagePath);
                _printImage = Image.FromFile(printImagePath);
            }
            catch (Exception ex)
            {
                throw new Exception(@"Image files not found.", ex);
            }
        }

        public void SetPrintImage(int index)
        {
            if (index < _monitorIndex)
            {
                _monitors[index].BackgroundImage = _printImage;
                _monitors[index].Update();
            }
        }

        public void SetBlankImage(int index)
        {
            if (index < _monitorIndex)
            {
                _monitors[index].BackgroundImage = _defaultImage;
                _monitors[index].Update();
            }
        }

        public void LoadProjectors(bool isExtendedMonitors)
        {
            if (isExtendedMonitors)
            {
                LoadMultipleMonitorSetup();
                _isExtended = true;
            }
            else
            {
                LoadDuplicateMonitorSetup();
                _isExtended = false;
            }
        }

        public void DestroyProjectors()
        {
            for(int i = 0; i < _monitorIndex; i++)
            {
                _monitors[i].Close();
            }

            _monitorIndex = 0;
        }

        private void LoadDuplicateMonitorSetup()
        {
            Screen screen = Screen.PrimaryScreen;
            int number;

            for (int i = 0; i < screen.DeviceName.Length; i++)
            {
                if (Char.IsDigit(screen.DeviceName[i]))
                {
                    char buffer = screen.DeviceName[i];
                    number = int.Parse(char.ToString(buffer));
                    break;
                }
            }

            _monitors[_monitorIndex] = new Form();
            Rectangle tempRect = screen.Bounds;
            _monitors[_monitorIndex].Text = "Image";
            _monitors[_monitorIndex].DesktopBounds = tempRect;
            _monitors[_monitorIndex].StartPosition = FormStartPosition.Manual;
            _monitors[_monitorIndex].WindowState = FormWindowState.Maximized;
            _monitors[_monitorIndex].FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            _monitors[_monitorIndex].BackColor = System.Drawing.Color.Black;
            _defaultImage = (Image)(new Bitmap(_defaultImage, new Size(tempRect.Width, tempRect.Height)));
            _printImage = (Image)(new Bitmap(_printImage, new Size(tempRect.Width, tempRect.Height)));
            _monitors[_monitorIndex].BackgroundImage = _defaultImage;
            _monitors[_monitorIndex].Show();
            _monitorIndex++;
        }

        private void LoadMultipleMonitorSetup()
        {
            foreach (Screen screen in Screen.AllScreens)
            {
                int number = 0;

                for (int i = 0; i < screen.DeviceName.Length; i++)
                {
                    if (Char.IsDigit(screen.DeviceName[i]))
                    {
                        char buffer = screen.DeviceName[i];
                        number = int.Parse(char.ToString(buffer));
                        break;
                    }
                }

                if (number > 1)
                {
                    _monitors[_monitorIndex] = new Form();
                    Rectangle tempRect = screen.Bounds;
                    _monitors[_monitorIndex].Text = "Image";
                    _monitors[_monitorIndex].DesktopBounds = tempRect;
                    _monitors[_monitorIndex].StartPosition = FormStartPosition.Manual;
                    _monitors[_monitorIndex].WindowState = FormWindowState.Maximized;
                    _monitors[_monitorIndex].FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
                    _monitors[_monitorIndex].BackColor = System.Drawing.Color.Black;
                    _defaultImage = (Image)(new Bitmap(_defaultImage, new Size(tempRect.Width, tempRect.Height)));
                    _printImage = (Image)(new Bitmap(_printImage, new Size(tempRect.Width, tempRect.Height)));
                    _monitors[_monitorIndex].BackgroundImage = _defaultImage;
                    _monitors[_monitorIndex].Show();
                    _monitorIndex++;
                }
            }

            if (_monitorIndex == 0)
            {
                MessageBox.Show("Only one monitor is detected, extended multiple monitor setup not possible.", "Multiple Monitor Setup", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        public Form[] GetMonitors()
        {
            return _monitors;
        }

        public int MonitorCount()
        {
            return _monitorIndex;
        }

        public bool isExtended()
        {
            return _isExtended;
        }
    }
}
