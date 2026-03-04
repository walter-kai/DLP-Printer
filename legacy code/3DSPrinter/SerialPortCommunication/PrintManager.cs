using System;
using System.Collections.Generic;
using System.Xml;
using System.Xml.Schema;
using System.Xml.Serialization;
using System.Xml.XPath;
using System.IO;
using System.Text;

namespace PCComm
{
    class PrintManager
    {
        private XmlDocument doc;

        public struct Settings
        {
            public bool InitialLongPrint;
            public int InitialExposure;
            public int SprewSliceCount;
            public int SliceCount;
            public int SliceThickness;
            public int Exposure;
            public bool PullOffAndInSteps;
            public char SprewSide;
        }

        private Settings settings;

        public PrintManager()
        {
            doc = new XmlDocument();
            settings = new Settings();
        }

        public void Load(String fileName)
        {
            try
            {
                doc.Load(fileName);

                XmlNode parentNode = doc.DocumentElement;

                foreach (XmlNode node in parentNode.ChildNodes)
                {
                    switch (node.Name)
                    {
                        case "Settings":
                            settings.InitialLongPrint = Boolean.Parse(node["InitialLongPrint"].InnerText);
                            settings.InitialExposure = Int32.Parse(node["InitialExposure"].InnerText);
                            settings.SprewSliceCount = Int32.Parse(node["SprewSliceCount"].InnerText);
                            settings.SliceCount = Int32.Parse(node["SliceCount"].InnerText);
                            settings.SliceThickness = Int32.Parse(node["SliceThickness"].InnerText);
                            settings.Exposure = Int32.Parse(node["Exposure"].InnerText);
                            settings.PullOffAndInSteps = Boolean.Parse(node["PullOffAndInSteps"].InnerText);
                            settings.SprewSide = Char.Parse(node["SprewSide"].InnerText);
                            break;
                        default:
                            break;
                    }
                }
            }
            catch (Exception ex)
            {
                throw new Exception(@"Invalid file", ex);
            }
        }

        public void Save(String filePath)
        {
            try
            {
                doc.Load(filePath);

                XmlNode parentNode = doc.DocumentElement;

                foreach (XmlNode node in parentNode.ChildNodes)
                {
                    switch (node.Name)
                    {
                        case "Settings":
                            node["InitialLongPrint"].InnerText = settings.InitialLongPrint ? "true" : "false";
                            node["InitialExposure"].InnerText = settings.InitialExposure.ToString();                           
                            node["SprewSliceCount"].InnerText = settings.SprewSliceCount.ToString();
                            node["SliceCount"].InnerText = settings.SliceCount.ToString();
                            node["SliceThickness"].InnerText = settings.SliceThickness.ToString();
                            node["Exposure"].InnerText = settings.Exposure.ToString();
                            node["PullOffAndInSteps"].InnerText = settings.PullOffAndInSteps ? "true" : "false";
                            node["SprewSide"].InnerText = settings.SprewSide.ToString();
                            break;
                        default:
                            break;
                    }
                }
                doc.Save(filePath);
            }
            catch (Exception ex)
            {
                throw new Exception(@"Invalid file", ex);
            }
        }

        public bool InitialLongPrint
        {
            get { return settings.InitialLongPrint; }
            set { settings.InitialLongPrint = value; }
        }

        public int InitialExposure
        {
            get { return settings.InitialExposure; }
            set { settings.InitialExposure = value; }
        }

        public int SprewSliceCount
        {
            get { return settings.SprewSliceCount; }
            set { settings.SprewSliceCount = value; }
        }

        public int SliceCount
        {
            get { return settings.SliceCount; }
            set { settings.SliceCount = value; }
        }

        public int SliceThickness
        {
            get { return settings.SliceThickness; }
            set { settings.SliceThickness = value; }
        }

        public int Exposure
        {
            get { return settings.Exposure; }
            set { settings.Exposure = value; }
        }

        public bool PullOffAndInSteps
        {
            get { return settings.PullOffAndInSteps; }
            set { settings.PullOffAndInSteps = value; }
        }

        public Char SprewSide
        {
            get { return settings.SprewSide; }
            set { settings.SprewSide = value; }
        }
    }
}
