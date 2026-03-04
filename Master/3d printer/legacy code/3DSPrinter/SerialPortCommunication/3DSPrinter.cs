using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using PCComm;
using System.Runtime.InteropServices;
using System.Threading;

namespace PCComm
{
    public partial class frmMain : Form
    {
        CommunicationManager _comm = new CommunicationManager();
        PrintManager _print = new PrintManager();
        Boolean _stop;

        string transType = string.Empty;

        public frmMain()
        {
            InitializeComponent();
            
        }

        private void frmMain_Load(object sender, EventArgs e)
        {
           LoadValues();
           SetDefaults();
           SetControlState();
        }

        private void cmdOpen_Click(object sender, EventArgs e)
        {
            _comm.Parity = cboParity.Text;
            _comm.StopBits = cboStop.Text;
            _comm.DataBits = cboData.Text;
            _comm.BaudRate = cboBaud.Text;
            _comm.PortName = cboPort.Text;
            _comm.DisplayWindow = rtbDisplay;
            _comm.OpenPort();

            cmdOpen.Enabled = false;
            cmdClose.Enabled = true;
            cmdSend.Enabled = true;

            XMinus.Enabled = true;
            XPlus.Enabled = true;
            YMinus.Enabled = true;
            YPlus.Enabled = true;
            //StopButton.Enabled = true;

            SlowMotorRadioButton.Enabled = true;
            FastMotorRadioButton.Enabled = true;
        }

        /// <summary>
        /// Method to initialize serial port
        /// values to standard defaults
        /// </summary>
        private void SetDefaults()
        {
            if(cboPort.Items.Count > 0)
                cboPort.SelectedIndex = 0;
            cboBaud.SelectedText = "115200";
            cboParity.SelectedIndex = 0;
            cboStop.SelectedIndex = 1;
            cboData.SelectedIndex = 1;
            BlankImagePathTextBox.Text = System.IO.Path.GetDirectoryName(Application.ExecutablePath) + "\\..\\..\\..\\blank.jpg";
            PrintImagePathTextBox.Text = System.IO.Path.GetDirectoryName(Application.ExecutablePath) + "\\..\\..\\..\\print.jpg";
            SpruceSliceCountTextBox.Text = "32";
            SliceCountTextBox.Text = "32";
            SliceThicknessTextBox.Text = "250";
            ExposureTextBox.Text = "5000";
            InitialExposureTextBox.Text = "60000";
            sprewXRadioButton.Checked = true;
            sprewYRadioButton.Checked = false;
            _comm.CurrentTransmissionType = PCComm.CommunicationManager.TransmissionType.Text;
            MovementTextBox.Text = "1000";
            FastMotorRadioButton.Checked = false;
            SlowMotorRadioButton.Checked = true;
            StartPrintButton.Enabled = false;
            StopPrintButton.Enabled = false;
            XMinus.Enabled = false;
            XPlus.Enabled = false;
            YMinus.Enabled = false;
            YPlus.Enabled = false;
            StopButton.Enabled = false;
            SlowMotorRadioButton.Enabled = false;
            FastMotorRadioButton.Enabled = false;
            BothSidedStart.Checked = false;
            _stop = false;
        }

        /// <summary>
        /// methos to load our serial
        /// port option values
        /// </summary>
        private void LoadValues()
        {
            _comm.SetPortNameValues(cboPort);
            _comm.SetParityValues(cboParity);
            _comm.SetStopBitValues(cboStop);
        }

        /// <summary>
        /// method to set the state of controls
        /// when the form first loads
        /// </summary>
        private void SetControlState()
        {
            cmdSend.Enabled = false;
            cmdClose.Enabled = false;
        }

        private void cmdSend_Click(object sender, EventArgs e)
        {
            _comm.WriteData(txtSend.Text);
        }


        private void cmdClose_Click(object sender, EventArgs e)
        {
            _comm.ClosePort();

            cmdOpen.Enabled = true;
            cmdClose.Enabled = false;
            cmdSend.Enabled = false;
            XMinus.Enabled = false;
            XPlus.Enabled = false;
            YMinus.Enabled = false;
            YPlus.Enabled = false;
            StopButton.Enabled = false;
            SlowMotorRadioButton.Enabled = false;
            FastMotorRadioButton.Enabled = false;
        }

        private void Refresh_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
            // For each screen, add the screen properties to a list box. 
            foreach (var screen in System.Windows.Forms.Screen.AllScreens)
            {
                listBox1.Items.Add(screen.DeviceName);
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                MonitorManager monitorTest = new MonitorManager(BlankImagePathTextBox.Text, PrintImagePathTextBox.Text);

                if (ExtendMonitorsRadioButton.Checked)
                {
                    monitorTest.LoadProjectors(true);
                }
                else
                {
                    monitorTest.LoadProjectors(false);
                }

                Thread.Sleep(5000);
                monitorTest.DestroyProjectors();
            }
            catch(Exception ex)
            {
                MessageBox.Show(ex.Message, "Incorrect Image Path", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void BrowseBlankImageButton_Click(object sender, EventArgs e)
        {
            var FD = new System.Windows.Forms.OpenFileDialog();

            if (FD.ShowDialog() == System.Windows.Forms.DialogResult.OK)
            {
                BlankImagePathTextBox.Text = FD.FileName;
            }
        }

        private void BrowsePrintImageButton_Click(object sender, EventArgs e)
        {
            var FD = new System.Windows.Forms.OpenFileDialog();

            if (FD.ShowDialog() == System.Windows.Forms.DialogResult.OK)
            {
                PrintImagePathTextBox.Text = FD.FileName;
            }
        }

        private void XPlus_Click(object sender, EventArgs e)
        {
            String speed;

            if (SlowMotorRadioButton.Checked)
                speed = "G0";
            else
                speed = "G1";

            if (_comm.IsOpen())
            {
                _comm.WriteData(speed + " X" + MovementTextBox.Text);
            }
        }

        private void XMinus_Click(object sender, EventArgs e)
        {
            String speed;

            if (SlowMotorRadioButton.Checked)
                speed = "G0";
            else
                speed = "G1";

            if (_comm.IsOpen())
            {
                _comm.WriteData(speed + " X-" + MovementTextBox.Text);
            }
        }

        private void YPlus_Click(object sender, EventArgs e)
        {
            String speed;

            if (SlowMotorRadioButton.Checked)
                speed = "G0";
            else
                speed = "G1";

            if (_comm.IsOpen())
            {
                _comm.WriteData(speed + " Y" + MovementTextBox.Text);
            }
        }

        private void YMinus_Click(object sender, EventArgs e)
        {
            String speed;

            if (SlowMotorRadioButton.Checked)
                speed = "G0";
            else
                speed = "G1";

            if (_comm.IsOpen())
            {
                _comm.WriteData(speed + " Y-" + MovementTextBox.Text);
            }
        }

        private void StopButton_Click(object sender, EventArgs e)
        {
            if (_comm.IsOpen())
            {
                _comm.WriteData("STOP");
            }
        }

        private void LoadButton_Click(object sender, EventArgs e)
        {
            try
            {
                String path = System.IO.Path.GetDirectoryName(Application.ExecutablePath) + "\\..\\..\\..\\print.xml";
                _print.Load(path);
                SpruceSliceCountTextBox.Text = _print.SprewSliceCount.ToString();
                SliceCountTextBox.Text = _print.SliceCount.ToString();
                SliceThicknessTextBox.Text = _print.SliceThickness.ToString();
                ExposureTextBox.Text = _print.Exposure.ToString();
                InitialExposureTextBox.Text = _print.InitialExposure.ToString();

                StopPrintButton.Enabled = true;
                StartPrintButton.Enabled = true;

                if (_print.InitialLongPrint)
                {
                    BothSidedStart.Checked = true;
                }
                else
                {
                    BothSidedStart.Checked = false;
                }

                if (_print.PullOffAndInSteps)
                {
                    PullOffAndInRadioBox.Checked = true;
                    PullOfRadioBox.Checked = false;
                }
                else
                {
                    PullOffAndInRadioBox.Checked = false;
                    PullOfRadioBox.Checked = true;
                }

                if (_print.SprewSide == 'X')
                {
                    sprewXRadioButton.Checked = true;
                    sprewYRadioButton.Checked = false;
                }
                else
                {
                    sprewXRadioButton.Checked = false;
                    sprewYRadioButton.Checked = true;
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Invalid File", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void StartPrintButton_Click(object sender, EventArgs e)
        {
            new Thread(delegate()
            {
                try
                {
                    MonitorManager monitor = new MonitorManager(BlankImagePathTextBox.Text, PrintImagePathTextBox.Text);
                    int monitorCount;
                    String speed;
                    _stop = false;

                    if (!_comm.IsOpen())
                        throw new Exception(@"port not opened");

                    if (ExtendMonitorsRadioButton.Checked)
                    {
                        monitor.LoadProjectors(true);
                    }
                    else
                    {
                        monitor.LoadProjectors(false);
                    }

                    monitorCount = monitor.MonitorCount();

                    //if (SlowMotorRadioButton.Checked)
                    speed = "G0";
                    //else
                    //  speed = "G1";
                    
                    //InitialExposure
                    if (_print.InitialLongPrint)
                    {
                        for (int i = 0; i < monitorCount; i++)
                        {
                            monitor.SetPrintImage(i);
                        }
                        Thread.Sleep(_print.InitialExposure);

                        if (_stop)
                            return;
                    }

                    for (int i = 0; i < monitorCount; i++)
                    {
                        monitor.SetBlankImage(i);
                    }

                    //Sprew Print
                    for (int i = 0; i < _print.SprewSliceCount; i++)
                    {
                        if (_print.PullOffAndInSteps)
                        {
                            _comm.WriteData(speed + " " + _print.SprewSide + (_print.SliceThickness * 3).ToString());
                            while (String.Compare(_comm.messageRecieved(), "OK\r\n") != 0) ;
                            _comm.WriteData(speed + " " + _print.SprewSide + "-" + (2 * _print.SliceThickness).ToString());
                            while (String.Compare(_comm.messageRecieved(), "OK\r\n") != 0) ;
                        }
                        else
                        {
                            _comm.WriteData(speed + " " + _print.SprewSide + _print.SliceThickness.ToString());
                            while (String.Compare(_comm.messageRecieved(), "OK\r\n") != 0) ;
                        }

                        monitor.SetPrintImage((_print.SprewSide == 'X') ? 0 : 1);
                        monitor.SetBlankImage((_print.SprewSide == 'X') ? 1 : 0);

                        Thread.Sleep(_print.Exposure);
                        for (int j = 0; j < monitorCount; j++)
                        {
                            monitor.SetBlankImage(j);
                        }

                        if (_stop)
                            return;
                    }

                    //Main Print
                    for (int i = 0; i < _print.SliceCount; i++)
                    {
                        if (_print.PullOffAndInSteps)
                        {
                            _comm.WriteData(speed + " " + "X" + (3 * _print.SliceThickness).ToString() + " Y" + (3 * _print.SliceThickness).ToString());
                            while (String.Compare(_comm.messageRecieved(), "OK\r\n") != 0) ;
                            _comm.WriteData(speed + " " + "X-" + (2 * _print.SliceThickness).ToString() + " Y-" + (2 * _print.SliceThickness).ToString());
                            while (String.Compare(_comm.messageRecieved(), "OK\r\n") != 0) ;                      
                        }
                        else
                        {
                            _comm.WriteData(speed + " " + "X" + _print.SliceThickness.ToString() + " Y" + _print.SliceThickness.ToString());
                            while (String.Compare(_comm.messageRecieved(), "OK\r\n") != 0) ;                      
                        }

                        monitor.SetPrintImage(0);
                        monitor.SetPrintImage(1);

                        Thread.Sleep(_print.Exposure);
                        for (int j = 0; j < monitorCount; j++)
                        {
                            monitor.SetBlankImage(j);
                        }

                        if (_stop)
                            return;
                    }

                    monitor.DestroyProjectors();
                    return;
                }
                catch (Exception ex) 
                {
                    MessageBox.Show(ex.Message, "Print Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }).Start();
        }

        private void SaveButton_Click(object sender, EventArgs e)
        {
            String path = System.IO.Path.GetDirectoryName(Application.ExecutablePath) + "\\..\\..\\..\\print.xml";

            _print.InitialLongPrint = BothSidedStart.Checked;
            _print.InitialExposure = Int32.Parse(InitialExposureTextBox.Text);
            _print.SprewSliceCount = Int32.Parse(SpruceSliceCountTextBox.Text);
            _print.SliceCount = Int32.Parse(SliceCountTextBox.Text);
            _print.SliceThickness = Int32.Parse(SliceThicknessTextBox.Text);
            _print.Exposure = Int32.Parse(ExposureTextBox.Text);
            _print.PullOffAndInSteps = PullOffAndInRadioBox.Checked;
            _print.SprewSide = sprewXRadioButton.Checked ? 'X' : 'Y';

            _print.Save(path);
        }

        private void StopPrintButton_Click(object sender, EventArgs e)
        {
            _stop = true;
        }
    }
}