namespace PCComm
{
    partial class frmMain
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.cboData = new System.Windows.Forms.ComboBox();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.cmdClose = new System.Windows.Forms.Button();
            this.cboStop = new System.Windows.Forms.ComboBox();
            this.GroupBox1 = new System.Windows.Forms.GroupBox();
            this.cmdSend = new System.Windows.Forms.Button();
            this.txtSend = new System.Windows.Forms.TextBox();
            this.rtbDisplay = new System.Windows.Forms.RichTextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.label2 = new System.Windows.Forms.Label();
            this.cboParity = new System.Windows.Forms.ComboBox();
            this.Label1 = new System.Windows.Forms.Label();
            this.cboBaud = new System.Windows.Forms.ComboBox();
            this.cboPort = new System.Windows.Forms.ComboBox();
            this.cmdOpen = new System.Windows.Forms.Button();
            this.groupBox4 = new System.Windows.Forms.GroupBox();
            this.groupBox6 = new System.Windows.Forms.GroupBox();
            this.BrowsePrintImageButton = new System.Windows.Forms.Button();
            this.PrintImagePathTextBox = new System.Windows.Forms.TextBox();
            this.BlankImagePathTextBox = new System.Windows.Forms.TextBox();
            this.label8 = new System.Windows.Forms.Label();
            this.label7 = new System.Windows.Forms.Label();
            this.BrowseBlankImageButton = new System.Windows.Forms.Button();
            this.groupBox5 = new System.Windows.Forms.GroupBox();
            this.DuplicateMonitorsRadioButton = new System.Windows.Forms.RadioButton();
            this.ExtendMonitorsRadioButton = new System.Windows.Forms.RadioButton();
            this.button1 = new System.Windows.Forms.Button();
            this.Refresh = new System.Windows.Forms.Button();
            this.listBox1 = new System.Windows.Forms.ListBox();
            this.groupBox7 = new System.Windows.Forms.GroupBox();
            this.groupBox8 = new System.Windows.Forms.GroupBox();
            this.groupBox11 = new System.Windows.Forms.GroupBox();
            this.label13 = new System.Windows.Forms.Label();
            this.InitialExposureTextBox = new System.Windows.Forms.TextBox();
            this.BothSidedStart = new System.Windows.Forms.CheckBox();
            this.sprewXRadioButton = new System.Windows.Forms.RadioButton();
            this.sprewYRadioButton = new System.Windows.Forms.RadioButton();
            this.groupBox10 = new System.Windows.Forms.GroupBox();
            this.SaveButton = new System.Windows.Forms.Button();
            this.LoadButton = new System.Windows.Forms.Button();
            this.groupBox9 = new System.Windows.Forms.GroupBox();
            this.PullOffAndInRadioBox = new System.Windows.Forms.RadioButton();
            this.PullOfRadioBox = new System.Windows.Forms.RadioButton();
            this.label11 = new System.Windows.Forms.Label();
            this.ExposureTextBox = new System.Windows.Forms.TextBox();
            this.label10 = new System.Windows.Forms.Label();
            this.label9 = new System.Windows.Forms.Label();
            this.SliceThicknessTextBox = new System.Windows.Forms.TextBox();
            this.SliceCountTextBox = new System.Windows.Forms.TextBox();
            this.label6 = new System.Windows.Forms.Label();
            this.SpruceSliceCountTextBox = new System.Windows.Forms.TextBox();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.StartPrintButton = new System.Windows.Forms.Button();
            this.StopPrintButton = new System.Windows.Forms.Button();
            this.label12 = new System.Windows.Forms.Label();
            this.XMinus = new System.Windows.Forms.Button();
            this.XPlus = new System.Windows.Forms.Button();
            this.YPlus = new System.Windows.Forms.Button();
            this.YMinus = new System.Windows.Forms.Button();
            this.MovementTextBox = new System.Windows.Forms.TextBox();
            this.groupBox3 = new System.Windows.Forms.GroupBox();
            this.SlowMotorRadioButton = new System.Windows.Forms.RadioButton();
            this.FastMotorRadioButton = new System.Windows.Forms.RadioButton();
            this.StopButton = new System.Windows.Forms.Button();
            this.GroupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.groupBox4.SuspendLayout();
            this.groupBox6.SuspendLayout();
            this.groupBox5.SuspendLayout();
            this.groupBox7.SuspendLayout();
            this.groupBox8.SuspendLayout();
            this.groupBox11.SuspendLayout();
            this.groupBox10.SuspendLayout();
            this.groupBox9.SuspendLayout();
            this.groupBox3.SuspendLayout();
            this.SuspendLayout();
            // 
            // cboData
            // 
            this.cboData.FormattingEnabled = true;
            this.cboData.Items.AddRange(new object[] {
            "7",
            "8",
            "9"});
            this.cboData.Location = new System.Drawing.Point(9, 195);
            this.cboData.Name = "cboData";
            this.cboData.Size = new System.Drawing.Size(76, 21);
            this.cboData.TabIndex = 14;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(7, 139);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(49, 13);
            this.label4.TabIndex = 18;
            this.label4.Text = "Stop Bits";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(6, 179);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(50, 13);
            this.label5.TabIndex = 19;
            this.label5.Text = "Data Bits";
            // 
            // cmdClose
            // 
            this.cmdClose.Location = new System.Drawing.Point(416, 277);
            this.cmdClose.Name = "cmdClose";
            this.cmdClose.Size = new System.Drawing.Size(100, 23);
            this.cmdClose.TabIndex = 0;
            this.cmdClose.Text = "Close Port";
            this.cmdClose.Click += new System.EventHandler(this.cmdClose_Click);
            // 
            // cboStop
            // 
            this.cboStop.FormattingEnabled = true;
            this.cboStop.Location = new System.Drawing.Point(9, 155);
            this.cboStop.Name = "cboStop";
            this.cboStop.Size = new System.Drawing.Size(76, 21);
            this.cboStop.TabIndex = 13;
            // 
            // GroupBox1
            // 
            this.GroupBox1.Controls.Add(this.cmdSend);
            this.GroupBox1.Controls.Add(this.txtSend);
            this.GroupBox1.Controls.Add(this.rtbDisplay);
            this.GroupBox1.Location = new System.Drawing.Point(12, 12);
            this.GroupBox1.Name = "GroupBox1";
            this.GroupBox1.Size = new System.Drawing.Size(398, 169);
            this.GroupBox1.TabIndex = 4;
            this.GroupBox1.TabStop = false;
            this.GroupBox1.Text = "Serial Port Communication";
            // 
            // cmdSend
            // 
            this.cmdSend.Location = new System.Drawing.Point(312, 142);
            this.cmdSend.Name = "cmdSend";
            this.cmdSend.Size = new System.Drawing.Size(75, 23);
            this.cmdSend.TabIndex = 5;
            this.cmdSend.Text = "Send";
            this.cmdSend.UseVisualStyleBackColor = true;
            this.cmdSend.Click += new System.EventHandler(this.cmdSend_Click);
            // 
            // txtSend
            // 
            this.txtSend.Location = new System.Drawing.Point(7, 142);
            this.txtSend.Name = "txtSend";
            this.txtSend.Size = new System.Drawing.Size(299, 20);
            this.txtSend.TabIndex = 4;
            // 
            // rtbDisplay
            // 
            this.rtbDisplay.Location = new System.Drawing.Point(7, 19);
            this.rtbDisplay.Name = "rtbDisplay";
            this.rtbDisplay.Size = new System.Drawing.Size(380, 117);
            this.rtbDisplay.TabIndex = 3;
            this.rtbDisplay.Text = "";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(6, 98);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(33, 13);
            this.label3.TabIndex = 17;
            this.label3.Text = "Parity";
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.label5);
            this.groupBox2.Controls.Add(this.cboData);
            this.groupBox2.Controls.Add(this.label4);
            this.groupBox2.Controls.Add(this.cboStop);
            this.groupBox2.Controls.Add(this.label3);
            this.groupBox2.Controls.Add(this.label2);
            this.groupBox2.Controls.Add(this.cboParity);
            this.groupBox2.Controls.Add(this.Label1);
            this.groupBox2.Controls.Add(this.cboBaud);
            this.groupBox2.Controls.Add(this.cboPort);
            this.groupBox2.Location = new System.Drawing.Point(416, 13);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(93, 257);
            this.groupBox2.TabIndex = 6;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "Options";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(6, 58);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(58, 13);
            this.label2.TabIndex = 16;
            this.label2.Text = "Baud Rate";
            // 
            // cboParity
            // 
            this.cboParity.FormattingEnabled = true;
            this.cboParity.Location = new System.Drawing.Point(9, 114);
            this.cboParity.Name = "cboParity";
            this.cboParity.Size = new System.Drawing.Size(76, 21);
            this.cboParity.TabIndex = 12;
            // 
            // Label1
            // 
            this.Label1.AutoSize = true;
            this.Label1.Location = new System.Drawing.Point(6, 18);
            this.Label1.Name = "Label1";
            this.Label1.Size = new System.Drawing.Size(26, 13);
            this.Label1.TabIndex = 15;
            this.Label1.Text = "Port";
            // 
            // cboBaud
            // 
            this.cboBaud.FormattingEnabled = true;
            this.cboBaud.Items.AddRange(new object[] {
            "300",
            "1200",
            "2400",
            "4800",
            "9600",
            "14400",
            "19200",
            "28800",
            "38400",
            "57600",
            "115200"});
            this.cboBaud.Location = new System.Drawing.Point(9, 74);
            this.cboBaud.Name = "cboBaud";
            this.cboBaud.Size = new System.Drawing.Size(76, 21);
            this.cboBaud.TabIndex = 11;
            // 
            // cboPort
            // 
            this.cboPort.FormattingEnabled = true;
            this.cboPort.Location = new System.Drawing.Point(9, 34);
            this.cboPort.Name = "cboPort";
            this.cboPort.Size = new System.Drawing.Size(76, 21);
            this.cboPort.TabIndex = 10;
            // 
            // cmdOpen
            // 
            this.cmdOpen.Location = new System.Drawing.Point(416, 306);
            this.cmdOpen.Name = "cmdOpen";
            this.cmdOpen.Size = new System.Drawing.Size(100, 21);
            this.cmdOpen.TabIndex = 8;
            this.cmdOpen.Text = "Open Port";
            this.cmdOpen.UseVisualStyleBackColor = true;
            this.cmdOpen.Click += new System.EventHandler(this.cmdOpen_Click);
            // 
            // groupBox4
            // 
            this.groupBox4.Controls.Add(this.groupBox6);
            this.groupBox4.Controls.Add(this.groupBox5);
            this.groupBox4.Location = new System.Drawing.Point(522, 13);
            this.groupBox4.Name = "groupBox4";
            this.groupBox4.Size = new System.Drawing.Size(766, 135);
            this.groupBox4.TabIndex = 10;
            this.groupBox4.TabStop = false;
            this.groupBox4.Text = "Display Configuration";
            // 
            // groupBox6
            // 
            this.groupBox6.Controls.Add(this.BrowsePrintImageButton);
            this.groupBox6.Controls.Add(this.PrintImagePathTextBox);
            this.groupBox6.Controls.Add(this.BlankImagePathTextBox);
            this.groupBox6.Controls.Add(this.label8);
            this.groupBox6.Controls.Add(this.label7);
            this.groupBox6.Controls.Add(this.BrowseBlankImageButton);
            this.groupBox6.Location = new System.Drawing.Point(307, 22);
            this.groupBox6.Name = "groupBox6";
            this.groupBox6.Size = new System.Drawing.Size(443, 102);
            this.groupBox6.TabIndex = 15;
            this.groupBox6.TabStop = false;
            this.groupBox6.Text = "Load Images";
            // 
            // BrowsePrintImageButton
            // 
            this.BrowsePrintImageButton.Location = new System.Drawing.Point(357, 54);
            this.BrowsePrintImageButton.Name = "BrowsePrintImageButton";
            this.BrowsePrintImageButton.Size = new System.Drawing.Size(75, 23);
            this.BrowsePrintImageButton.TabIndex = 16;
            this.BrowsePrintImageButton.Text = "Browse";
            this.BrowsePrintImageButton.UseVisualStyleBackColor = true;
            this.BrowsePrintImageButton.Click += new System.EventHandler(this.BrowsePrintImageButton_Click);
            // 
            // PrintImagePathTextBox
            // 
            this.PrintImagePathTextBox.Location = new System.Drawing.Point(79, 56);
            this.PrintImagePathTextBox.Name = "PrintImagePathTextBox";
            this.PrintImagePathTextBox.Size = new System.Drawing.Size(272, 20);
            this.PrintImagePathTextBox.TabIndex = 4;
            // 
            // BlankImagePathTextBox
            // 
            this.BlankImagePathTextBox.Location = new System.Drawing.Point(79, 30);
            this.BlankImagePathTextBox.Name = "BlankImagePathTextBox";
            this.BlankImagePathTextBox.Size = new System.Drawing.Size(272, 20);
            this.BlankImagePathTextBox.TabIndex = 3;
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(12, 59);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(60, 13);
            this.label8.TabIndex = 2;
            this.label8.Text = "Print Image";
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(6, 33);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(66, 13);
            this.label7.TabIndex = 1;
            this.label7.Text = "Blank Image";
            // 
            // BrowseBlankImageButton
            // 
            this.BrowseBlankImageButton.Location = new System.Drawing.Point(357, 28);
            this.BrowseBlankImageButton.Name = "BrowseBlankImageButton";
            this.BrowseBlankImageButton.Size = new System.Drawing.Size(75, 23);
            this.BrowseBlankImageButton.TabIndex = 0;
            this.BrowseBlankImageButton.Text = "Browse";
            this.BrowseBlankImageButton.UseVisualStyleBackColor = true;
            this.BrowseBlankImageButton.Click += new System.EventHandler(this.BrowseBlankImageButton_Click);
            // 
            // groupBox5
            // 
            this.groupBox5.Controls.Add(this.DuplicateMonitorsRadioButton);
            this.groupBox5.Controls.Add(this.ExtendMonitorsRadioButton);
            this.groupBox5.Controls.Add(this.button1);
            this.groupBox5.Location = new System.Drawing.Point(175, 21);
            this.groupBox5.Name = "groupBox5";
            this.groupBox5.Size = new System.Drawing.Size(126, 103);
            this.groupBox5.TabIndex = 14;
            this.groupBox5.TabStop = false;
            this.groupBox5.Text = "Mode";
            // 
            // DuplicateMonitorsRadioButton
            // 
            this.DuplicateMonitorsRadioButton.AutoSize = true;
            this.DuplicateMonitorsRadioButton.Location = new System.Drawing.Point(7, 20);
            this.DuplicateMonitorsRadioButton.Name = "DuplicateMonitorsRadioButton";
            this.DuplicateMonitorsRadioButton.Size = new System.Drawing.Size(113, 17);
            this.DuplicateMonitorsRadioButton.TabIndex = 1;
            this.DuplicateMonitorsRadioButton.TabStop = true;
            this.DuplicateMonitorsRadioButton.Text = "Duplicate Monitors";
            this.DuplicateMonitorsRadioButton.UseVisualStyleBackColor = true;
            // 
            // ExtendMonitorsRadioButton
            // 
            this.ExtendMonitorsRadioButton.AutoSize = true;
            this.ExtendMonitorsRadioButton.Checked = true;
            this.ExtendMonitorsRadioButton.Location = new System.Drawing.Point(7, 43);
            this.ExtendMonitorsRadioButton.Name = "ExtendMonitorsRadioButton";
            this.ExtendMonitorsRadioButton.Size = new System.Drawing.Size(113, 17);
            this.ExtendMonitorsRadioButton.TabIndex = 0;
            this.ExtendMonitorsRadioButton.TabStop = true;
            this.ExtendMonitorsRadioButton.Text = "Extended Monitors";
            this.ExtendMonitorsRadioButton.UseVisualStyleBackColor = true;
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(7, 72);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(113, 23);
            this.button1.TabIndex = 13;
            this.button1.Text = "Test Monitors";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // Refresh
            // 
            this.Refresh.Location = new System.Drawing.Point(7, 74);
            this.Refresh.Name = "Refresh";
            this.Refresh.Size = new System.Drawing.Size(150, 23);
            this.Refresh.TabIndex = 12;
            this.Refresh.Text = "Refresh Monitors";
            this.Refresh.UseVisualStyleBackColor = true;
            this.Refresh.Click += new System.EventHandler(this.Refresh_Click);
            // 
            // listBox1
            // 
            this.listBox1.FormattingEnabled = true;
            this.listBox1.Location = new System.Drawing.Point(6, 19);
            this.listBox1.Name = "listBox1";
            this.listBox1.Size = new System.Drawing.Size(150, 43);
            this.listBox1.TabIndex = 11;
            // 
            // groupBox7
            // 
            this.groupBox7.Controls.Add(this.listBox1);
            this.groupBox7.Controls.Add(this.Refresh);
            this.groupBox7.Location = new System.Drawing.Point(528, 32);
            this.groupBox7.Name = "groupBox7";
            this.groupBox7.Size = new System.Drawing.Size(163, 105);
            this.groupBox7.TabIndex = 15;
            this.groupBox7.TabStop = false;
            this.groupBox7.Text = "List of Monitors";
            // 
            // groupBox8
            // 
            this.groupBox8.Controls.Add(this.groupBox11);
            this.groupBox8.Controls.Add(this.groupBox10);
            this.groupBox8.Controls.Add(this.groupBox9);
            this.groupBox8.Controls.Add(this.label11);
            this.groupBox8.Controls.Add(this.ExposureTextBox);
            this.groupBox8.Controls.Add(this.label10);
            this.groupBox8.Controls.Add(this.label9);
            this.groupBox8.Controls.Add(this.SliceThicknessTextBox);
            this.groupBox8.Controls.Add(this.SliceCountTextBox);
            this.groupBox8.Controls.Add(this.label6);
            this.groupBox8.Controls.Add(this.SpruceSliceCountTextBox);
            this.groupBox8.Location = new System.Drawing.Point(522, 154);
            this.groupBox8.Name = "groupBox8";
            this.groupBox8.Size = new System.Drawing.Size(474, 122);
            this.groupBox8.TabIndex = 16;
            this.groupBox8.TabStop = false;
            this.groupBox8.Text = "Print Configurations";
            // 
            // groupBox11
            // 
            this.groupBox11.Controls.Add(this.label13);
            this.groupBox11.Controls.Add(this.InitialExposureTextBox);
            this.groupBox11.Controls.Add(this.BothSidedStart);
            this.groupBox11.Controls.Add(this.sprewXRadioButton);
            this.groupBox11.Controls.Add(this.sprewYRadioButton);
            this.groupBox11.Location = new System.Drawing.Point(323, 14);
            this.groupBox11.Name = "groupBox11";
            this.groupBox11.Size = new System.Drawing.Size(135, 102);
            this.groupBox11.TabIndex = 19;
            this.groupBox11.TabStop = false;
            this.groupBox11.Text = "Sprew Location";
            // 
            // label13
            // 
            this.label13.AutoSize = true;
            this.label13.Location = new System.Drawing.Point(6, 59);
            this.label13.Name = "label13";
            this.label13.Size = new System.Drawing.Size(78, 13);
            this.label13.TabIndex = 4;
            this.label13.Text = "Initial Exposure";
            // 
            // InitialExposureTextBox
            // 
            this.InitialExposureTextBox.Location = new System.Drawing.Point(87, 56);
            this.InitialExposureTextBox.Name = "InitialExposureTextBox";
            this.InitialExposureTextBox.Size = new System.Drawing.Size(42, 20);
            this.InitialExposureTextBox.TabIndex = 3;
            // 
            // BothSidedStart
            // 
            this.BothSidedStart.AutoSize = true;
            this.BothSidedStart.Location = new System.Drawing.Point(7, 81);
            this.BothSidedStart.Name = "BothSidedStart";
            this.BothSidedStart.Size = new System.Drawing.Size(101, 17);
            this.BothSidedStart.TabIndex = 2;
            this.BothSidedStart.Text = "Initial Long Print";
            this.BothSidedStart.UseVisualStyleBackColor = true;
            // 
            // sprewXRadioButton
            // 
            this.sprewXRadioButton.AutoSize = true;
            this.sprewXRadioButton.Location = new System.Drawing.Point(7, 17);
            this.sprewXRadioButton.Name = "sprewXRadioButton";
            this.sprewXRadioButton.Size = new System.Drawing.Size(32, 17);
            this.sprewXRadioButton.TabIndex = 1;
            this.sprewXRadioButton.TabStop = true;
            this.sprewXRadioButton.Text = "X";
            this.sprewXRadioButton.UseVisualStyleBackColor = true;
            // 
            // sprewYRadioButton
            // 
            this.sprewYRadioButton.AutoSize = true;
            this.sprewYRadioButton.Checked = true;
            this.sprewYRadioButton.Location = new System.Drawing.Point(7, 35);
            this.sprewYRadioButton.Name = "sprewYRadioButton";
            this.sprewYRadioButton.Size = new System.Drawing.Size(32, 17);
            this.sprewYRadioButton.TabIndex = 0;
            this.sprewYRadioButton.TabStop = true;
            this.sprewYRadioButton.Text = "Y";
            this.sprewYRadioButton.UseVisualStyleBackColor = true;
            // 
            // groupBox10
            // 
            this.groupBox10.Controls.Add(this.SaveButton);
            this.groupBox10.Controls.Add(this.LoadButton);
            this.groupBox10.Location = new System.Drawing.Point(182, 72);
            this.groupBox10.Name = "groupBox10";
            this.groupBox10.Size = new System.Drawing.Size(135, 44);
            this.groupBox10.TabIndex = 18;
            this.groupBox10.TabStop = false;
            this.groupBox10.Text = "Print Settings";
            // 
            // SaveButton
            // 
            this.SaveButton.Location = new System.Drawing.Point(76, 19);
            this.SaveButton.Name = "SaveButton";
            this.SaveButton.Size = new System.Drawing.Size(53, 19);
            this.SaveButton.TabIndex = 22;
            this.SaveButton.Text = "Save";
            this.SaveButton.UseVisualStyleBackColor = true;
            this.SaveButton.Click += new System.EventHandler(this.SaveButton_Click);
            // 
            // LoadButton
            // 
            this.LoadButton.Location = new System.Drawing.Point(6, 19);
            this.LoadButton.Name = "LoadButton";
            this.LoadButton.Size = new System.Drawing.Size(53, 19);
            this.LoadButton.TabIndex = 18;
            this.LoadButton.Text = "Load ";
            this.LoadButton.UseVisualStyleBackColor = true;
            this.LoadButton.Click += new System.EventHandler(this.LoadButton_Click);
            // 
            // groupBox9
            // 
            this.groupBox9.Controls.Add(this.PullOffAndInRadioBox);
            this.groupBox9.Controls.Add(this.PullOfRadioBox);
            this.groupBox9.Location = new System.Drawing.Point(182, 14);
            this.groupBox9.Name = "groupBox9";
            this.groupBox9.Size = new System.Drawing.Size(135, 57);
            this.groupBox9.TabIndex = 17;
            this.groupBox9.TabStop = false;
            this.groupBox9.Text = "Print Mode";
            // 
            // PullOffAndInRadioBox
            // 
            this.PullOffAndInRadioBox.AutoSize = true;
            this.PullOffAndInRadioBox.Location = new System.Drawing.Point(7, 17);
            this.PullOffAndInRadioBox.Name = "PullOffAndInRadioBox";
            this.PullOffAndInRadioBox.Size = new System.Drawing.Size(122, 17);
            this.PullOffAndInRadioBox.TabIndex = 1;
            this.PullOffAndInRadioBox.TabStop = true;
            this.PullOffAndInRadioBox.Text = "Pull Off and In Steps";
            this.PullOffAndInRadioBox.UseVisualStyleBackColor = true;
            // 
            // PullOfRadioBox
            // 
            this.PullOfRadioBox.AutoSize = true;
            this.PullOfRadioBox.Checked = true;
            this.PullOfRadioBox.Location = new System.Drawing.Point(7, 35);
            this.PullOfRadioBox.Name = "PullOfRadioBox";
            this.PullOfRadioBox.Size = new System.Drawing.Size(89, 17);
            this.PullOfRadioBox.TabIndex = 0;
            this.PullOfRadioBox.TabStop = true;
            this.PullOfRadioBox.Text = "Pull Off Steps";
            this.PullOfRadioBox.UseVisualStyleBackColor = true;
            // 
            // label11
            // 
            this.label11.AutoSize = true;
            this.label11.Location = new System.Drawing.Point(35, 99);
            this.label11.Name = "label11";
            this.label11.Size = new System.Drawing.Size(73, 13);
            this.label11.TabIndex = 8;
            this.label11.Text = "Exposure (ms)";
            // 
            // ExposureTextBox
            // 
            this.ExposureTextBox.Location = new System.Drawing.Point(114, 96);
            this.ExposureTextBox.Name = "ExposureTextBox";
            this.ExposureTextBox.Size = new System.Drawing.Size(56, 20);
            this.ExposureTextBox.TabIndex = 7;
            // 
            // label10
            // 
            this.label10.AutoSize = true;
            this.label10.Location = new System.Drawing.Point(3, 73);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(105, 13);
            this.label10.TabIndex = 6;
            this.label10.Text = "Slice Thickness (um)";
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Location = new System.Drawing.Point(47, 47);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(61, 13);
            this.label9.TabIndex = 5;
            this.label9.Text = "Slice Count";
            // 
            // SliceThicknessTextBox
            // 
            this.SliceThicknessTextBox.Location = new System.Drawing.Point(113, 70);
            this.SliceThicknessTextBox.Name = "SliceThicknessTextBox";
            this.SliceThicknessTextBox.Size = new System.Drawing.Size(56, 20);
            this.SliceThicknessTextBox.TabIndex = 3;
            // 
            // SliceCountTextBox
            // 
            this.SliceCountTextBox.Location = new System.Drawing.Point(114, 44);
            this.SliceCountTextBox.Name = "SliceCountTextBox";
            this.SliceCountTextBox.Size = new System.Drawing.Size(55, 20);
            this.SliceCountTextBox.TabIndex = 2;
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(14, 21);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(94, 13);
            this.label6.TabIndex = 1;
            this.label6.Text = "Sprew Slice Count";
            // 
            // SpruceSliceCountTextBox
            // 
            this.SpruceSliceCountTextBox.Location = new System.Drawing.Point(114, 18);
            this.SpruceSliceCountTextBox.Name = "SpruceSliceCountTextBox";
            this.SpruceSliceCountTextBox.Size = new System.Drawing.Size(55, 20);
            this.SpruceSliceCountTextBox.TabIndex = 0;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(522, 282);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(750, 45);
            this.richTextBox1.TabIndex = 17;
            this.richTextBox1.Text = "";
            // 
            // StartPrintButton
            // 
            this.StartPrintButton.Location = new System.Drawing.Point(1002, 159);
            this.StartPrintButton.Name = "StartPrintButton";
            this.StartPrintButton.Size = new System.Drawing.Size(132, 111);
            this.StartPrintButton.TabIndex = 18;
            this.StartPrintButton.Text = "Start";
            this.StartPrintButton.UseVisualStyleBackColor = true;
            this.StartPrintButton.Click += new System.EventHandler(this.StartPrintButton_Click);
            // 
            // StopPrintButton
            // 
            this.StopPrintButton.Location = new System.Drawing.Point(1140, 159);
            this.StopPrintButton.Name = "StopPrintButton";
            this.StopPrintButton.Size = new System.Drawing.Size(132, 111);
            this.StopPrintButton.TabIndex = 19;
            this.StopPrintButton.Text = "Stop";
            this.StopPrintButton.UseVisualStyleBackColor = true;
            this.StopPrintButton.Click += new System.EventHandler(this.StopPrintButton_Click);
            // 
            // label12
            // 
            this.label12.AutoSize = true;
            this.label12.Location = new System.Drawing.Point(16, 314);
            this.label12.Name = "label12";
            this.label12.Size = new System.Drawing.Size(221, 13);
            this.label12.TabIndex = 21;
            this.label12.Text = "Movement Command ex: G0 X100 Y-1000     ";
            // 
            // XMinus
            // 
            this.XMinus.Location = new System.Drawing.Point(20, 240);
            this.XMinus.Name = "XMinus";
            this.XMinus.Size = new System.Drawing.Size(75, 23);
            this.XMinus.TabIndex = 22;
            this.XMinus.Text = "-X";
            this.XMinus.UseVisualStyleBackColor = true;
            this.XMinus.Click += new System.EventHandler(this.XMinus_Click);
            // 
            // XPlus
            // 
            this.XPlus.Location = new System.Drawing.Point(172, 241);
            this.XPlus.Name = "XPlus";
            this.XPlus.Size = new System.Drawing.Size(75, 23);
            this.XPlus.TabIndex = 23;
            this.XPlus.Text = "+X";
            this.XPlus.UseVisualStyleBackColor = true;
            this.XPlus.Click += new System.EventHandler(this.XPlus_Click);
            // 
            // YPlus
            // 
            this.YPlus.Location = new System.Drawing.Point(95, 214);
            this.YPlus.Name = "YPlus";
            this.YPlus.Size = new System.Drawing.Size(75, 23);
            this.YPlus.TabIndex = 24;
            this.YPlus.Text = "+Y";
            this.YPlus.UseVisualStyleBackColor = true;
            this.YPlus.Click += new System.EventHandler(this.YPlus_Click);
            // 
            // YMinus
            // 
            this.YMinus.Location = new System.Drawing.Point(95, 269);
            this.YMinus.Name = "YMinus";
            this.YMinus.Size = new System.Drawing.Size(75, 23);
            this.YMinus.TabIndex = 25;
            this.YMinus.Text = "-Y";
            this.YMinus.UseVisualStyleBackColor = true;
            this.YMinus.Click += new System.EventHandler(this.YMinus_Click);
            // 
            // MovementTextBox
            // 
            this.MovementTextBox.Location = new System.Drawing.Point(101, 243);
            this.MovementTextBox.Name = "MovementTextBox";
            this.MovementTextBox.Size = new System.Drawing.Size(65, 20);
            this.MovementTextBox.TabIndex = 26;
            // 
            // groupBox3
            // 
            this.groupBox3.Controls.Add(this.SlowMotorRadioButton);
            this.groupBox3.Controls.Add(this.FastMotorRadioButton);
            this.groupBox3.Location = new System.Drawing.Point(264, 192);
            this.groupBox3.Name = "groupBox3";
            this.groupBox3.Size = new System.Drawing.Size(135, 59);
            this.groupBox3.TabIndex = 27;
            this.groupBox3.TabStop = false;
            this.groupBox3.Text = "Motor Speed";
            // 
            // SlowMotorRadioButton
            // 
            this.SlowMotorRadioButton.AutoSize = true;
            this.SlowMotorRadioButton.Location = new System.Drawing.Point(7, 17);
            this.SlowMotorRadioButton.Name = "SlowMotorRadioButton";
            this.SlowMotorRadioButton.Size = new System.Drawing.Size(48, 17);
            this.SlowMotorRadioButton.TabIndex = 1;
            this.SlowMotorRadioButton.TabStop = true;
            this.SlowMotorRadioButton.Text = "Slow";
            this.SlowMotorRadioButton.UseVisualStyleBackColor = true;
            // 
            // FastMotorRadioButton
            // 
            this.FastMotorRadioButton.AutoSize = true;
            this.FastMotorRadioButton.Checked = true;
            this.FastMotorRadioButton.Location = new System.Drawing.Point(7, 35);
            this.FastMotorRadioButton.Name = "FastMotorRadioButton";
            this.FastMotorRadioButton.Size = new System.Drawing.Size(45, 17);
            this.FastMotorRadioButton.TabIndex = 0;
            this.FastMotorRadioButton.TabStop = true;
            this.FastMotorRadioButton.Text = "Fast";
            this.FastMotorRadioButton.UseVisualStyleBackColor = true;
            // 
            // StopButton
            // 
            this.StopButton.Location = new System.Drawing.Point(264, 252);
            this.StopButton.Name = "StopButton";
            this.StopButton.Size = new System.Drawing.Size(135, 69);
            this.StopButton.TabIndex = 28;
            this.StopButton.Text = "STOP";
            this.StopButton.UseVisualStyleBackColor = true;
            this.StopButton.Click += new System.EventHandler(this.StopButton_Click);
            // 
            // frmMain
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1296, 333);
            this.Controls.Add(this.StopButton);
            this.Controls.Add(this.groupBox3);
            this.Controls.Add(this.MovementTextBox);
            this.Controls.Add(this.YMinus);
            this.Controls.Add(this.YPlus);
            this.Controls.Add(this.XPlus);
            this.Controls.Add(this.XMinus);
            this.Controls.Add(this.label12);
            this.Controls.Add(this.StopPrintButton);
            this.Controls.Add(this.StartPrintButton);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.groupBox8);
            this.Controls.Add(this.groupBox7);
            this.Controls.Add(this.groupBox4);
            this.Controls.Add(this.cmdClose);
            this.Controls.Add(this.GroupBox1);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.cmdOpen);
            this.Name = "frmMain";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "frmMain";
            this.Load += new System.EventHandler(this.frmMain_Load);
            this.GroupBox1.ResumeLayout(false);
            this.GroupBox1.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            this.groupBox4.ResumeLayout(false);
            this.groupBox6.ResumeLayout(false);
            this.groupBox6.PerformLayout();
            this.groupBox5.ResumeLayout(false);
            this.groupBox5.PerformLayout();
            this.groupBox7.ResumeLayout(false);
            this.groupBox8.ResumeLayout(false);
            this.groupBox8.PerformLayout();
            this.groupBox11.ResumeLayout(false);
            this.groupBox11.PerformLayout();
            this.groupBox10.ResumeLayout(false);
            this.groupBox9.ResumeLayout(false);
            this.groupBox9.PerformLayout();
            this.groupBox3.ResumeLayout(false);
            this.groupBox3.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ComboBox cboData;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Button cmdClose;
        private System.Windows.Forms.ComboBox cboStop;
        private System.Windows.Forms.GroupBox GroupBox1;
        private System.Windows.Forms.Button cmdSend;
        private System.Windows.Forms.TextBox txtSend;
        private System.Windows.Forms.RichTextBox rtbDisplay;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.ComboBox cboParity;
        private System.Windows.Forms.Label Label1;
        private System.Windows.Forms.ComboBox cboBaud;
        private System.Windows.Forms.ComboBox cboPort;
        private System.Windows.Forms.Button cmdOpen;
        private System.Windows.Forms.GroupBox groupBox4;
        private System.Windows.Forms.Button Refresh;
        private System.Windows.Forms.ListBox listBox1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.GroupBox groupBox5;
        private System.Windows.Forms.RadioButton ExtendMonitorsRadioButton;
        private System.Windows.Forms.RadioButton DuplicateMonitorsRadioButton;
        private System.Windows.Forms.GroupBox groupBox6;
        private System.Windows.Forms.Button BrowseBlankImageButton;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.Button BrowsePrintImageButton;
        private System.Windows.Forms.TextBox PrintImagePathTextBox;
        private System.Windows.Forms.TextBox BlankImagePathTextBox;
        private System.Windows.Forms.GroupBox groupBox7;
        private System.Windows.Forms.GroupBox groupBox8;
        private System.Windows.Forms.TextBox SpruceSliceCountTextBox;
        private System.Windows.Forms.Label label10;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.TextBox SliceThicknessTextBox;
        private System.Windows.Forms.TextBox SliceCountTextBox;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.GroupBox groupBox9;
        private System.Windows.Forms.RadioButton PullOffAndInRadioBox;
        private System.Windows.Forms.RadioButton PullOfRadioBox;
        private System.Windows.Forms.Label label11;
        private System.Windows.Forms.TextBox ExposureTextBox;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button StartPrintButton;
        private System.Windows.Forms.Button StopPrintButton;
        private System.Windows.Forms.Label label12;
        private System.Windows.Forms.Button LoadButton;
        private System.Windows.Forms.GroupBox groupBox10;
        private System.Windows.Forms.Button SaveButton;
        private System.Windows.Forms.GroupBox groupBox11;
        private System.Windows.Forms.RadioButton sprewXRadioButton;
        private System.Windows.Forms.RadioButton sprewYRadioButton;
        private System.Windows.Forms.Button XMinus;
        private System.Windows.Forms.Button XPlus;
        private System.Windows.Forms.Button YPlus;
        private System.Windows.Forms.Button YMinus;
        private System.Windows.Forms.TextBox MovementTextBox;
        private System.Windows.Forms.GroupBox groupBox3;
        private System.Windows.Forms.RadioButton SlowMotorRadioButton;
        private System.Windows.Forms.RadioButton FastMotorRadioButton;
        private System.Windows.Forms.Button StopButton;
        private System.Windows.Forms.CheckBox BothSidedStart;
        private System.Windows.Forms.Label label13;
        private System.Windows.Forms.TextBox InitialExposureTextBox;
    }
}