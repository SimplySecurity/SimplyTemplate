import os

class TemplateModule:

    def __init__(self):
        self.OutputName = 'McAfeeThreatIntell.mht' 
        self.RenderName = 'McAfeeThreatIntell.mht'
        self.CoreOptions = '[Text, Html, Link]'
        self.Name = 'McAfee Threat Intelligence Inside Feed.'
        self.Author = 'Killswitch-GUI'
        self.Type = 'Html'
        self.Info = 'A semi targeted email that pretends to be McAfee GTI notice for third party partners.'
        self.Sophistication = 'Medium'
        self.SampleImage = str('Modules/Sample/McAfeeThreatIntell.png')
        self.TemplatePath = str('Modules/EmailTemplates/McAfeeThreatIntell.email')
        self.RequiredOptions = {'FromEmail': ['noreply@agency.com', 'From Email'],
         'FromName': ['Alex Jason', 'From Full Name'],
         'TargetCompany': ['Cyber Power', 'Set the Target Company Full Name'],
         'TargetLink': ['%URL%', 'The full path link'],
         'CurrentDate': ['Sep 01, 2016', 'The current date'],
         'CveNumber': ['CVE-2015-2456', 'CVE number for vuln'],
         'VulnName': ['Adobe Flash Player RCE', 'CVE number for vuln'],
         'VulnSoftware': ['Adobe Flash Player RCE', 'CVE number for vuln']}

    def Generate(self, filename, location, Verbose = False):
        replaceDict = {'FROM_EMAIL': self.RequiredOptions['FromEmail'][0],
         'FROM_NAME': self.RequiredOptions['FromName'][0],
         'TARGET_COMPANY': self.RequiredOptions['TargetCompany'][0],
         'TARGET_LINK': self.RequiredOptions['TargetLink'][0],
         'CUR_DATE': self.RequiredOptions['CurrentDate'][0],
         'CVE_NUMBER': self.RequiredOptions['CveNumber'][0],
         'VULN_SOFTWARE': self.RequiredOptions['VulnSoftware'][0],
         'EXPLOIT_NAME': self.RequiredOptions['VulnName'][0]}
        WritePath = str(filename) + str(location)
        with open(self.TemplatePath, 'r') as templateEmail:
            outputEmail = templateEmail.read()
        for dummy, value in replaceDict.iteritems():
            outputEmail = outputEmail.replace(dummy, value)

        try:
            f = open(WritePath, 'w')
            f.write(outputEmail)
            f.close
        except Exception as e:
            print e

    def Render(self, Verbose = False):
        replaceDict = {'FROM_EMAIL': self.RequiredOptions['FromEmail'][0],
         'FROM_NAME': self.RequiredOptions['FromName'][0],
         'TARGET_COMPANY': self.RequiredOptions['TargetCompany'][0],
         'TARGET_LINK': self.RequiredOptions['TargetLink'][0],
         'CUR_DATE': self.RequiredOptions['CurrentDate'][0],
         'CVE_NUMBER': self.RequiredOptions['CveNumber'][0],
         'VULN_SOFTWARE': self.RequiredOptions['VulnSoftware'][0],
         'EXPLOIT_NAME': self.RequiredOptions['VulnName'][0]}
        with open(self.TemplatePath, 'r') as templateEmail:
            outputEmail = templateEmail.read()
        for dummy, value in replaceDict.iteritems():
            outputEmail = outputEmail.replace(dummy, value)

        return outputEmail
