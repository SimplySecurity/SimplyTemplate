#!/usr/bin/python
import os

# Class funcs will have:
# -Name
# -Author
# -Sophistication
# -Info

# Required Options for the class


class TemplateModule:

    def __init__(self):
        # Meta Tags for file name and such:
        self.OutputName = "CFOBonusStructure.html"
        self.RenderName = "CFOBonusStructure.html"
        self.CoreOptions = "[Html, Attachment]"
        # Required for each class:
        self.Name = "CFO Policy update to bonus."
        self.Author = "Killswitch-GUI"
        self.Type = "Html"
        self.Info = """A very intergrated CFO bonus policy update to the target. This template requires a large ammount of data / OSINT to build."""
        self.Sophistication = "High"
        self.SampleImage = str('''Modules/Sample/CFOBonusStructure.png''')
        self.TemplatePath = str(
            '''Modules/EmailTemplates/CFOBonusStructure.email''')
        # Required options for itself:
        self.RequiredOptions = {
            "FromEmail": ["noreply@agency.com", "From Email"],
            "FromCFOName": ["Alex Jason", "The Target CFO Full Name"],
            "FromRealEmail": ["alex@target.com", "The Target CFO real email"],
            "FromTitle": ["Chief Financial Officer", "Set the OSINT name gathered title"],
            "TargetLogo": ["http://Target.com/logo.png", "Set the Target Logo"],
            "TargetWebLink": ["Target.com", "Set the real target web link"],
            "TargetPhone": ["1-800-CD-FOUR", "Set the Target Toll Free line"],
            "TargetCompany": ["Cyber Power", "Set the Target Company Full Name"],
            "TargetAddress": ["123 Street Las Vegas, NV, 12345", "Set the Target Company Addr"],
        }

    def Generate(self, filename, location, Verbose=False):
        # Gen will get
        # Filename = the name of the output
        # Location = Where do you want to place the output
        # Verbose = Print all help data
        # adapted from Andy
        replaceDict = {
            'FROM_EMAIL': self.RequiredOptions["FromEmail"][0],
            'FROM_CFO_NAME': self.RequiredOptions["FromCFOName"][0],
            'FROM_REAL_EMAIL': self.RequiredOptions["FromRealEmail"][0],
            'FROM_TITLE': self.RequiredOptions["FromTitle"][0],
            'TARGET_LOGO': self.RequiredOptions["TargetLogo"][0],
            'TARGET_PHONE': self.RequiredOptions["TargetPhone"][0],
            'TARGET_COMP_NAME': self.RequiredOptions["TargetCompany"][0],
            'TARGET_ADDR': self.RequiredOptions["TargetAddress"][0],
            'TARGET_WEB_LINK': self.RequiredOptions["TargetWebLink"][0],
        }
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

    def Render(self, Verbose=False):
        # Gen will get
        # Filename = the name of the output
        # Location = Where do you want to place the output
        # Verbose = Print all help data
        # adapted from Andy
        replaceDict = {
            'FROM_EMAIL': self.RequiredOptions["FromEmail"][0],
            'FROM_CFO_NAME': self.RequiredOptions["FromCFOName"][0],
            'FROM_REAL_EMAIL': self.RequiredOptions["FromRealEmail"][0],
            'FROM_TITLE': self.RequiredOptions["FromTitle"][0],
            'TARGET_LOGO': self.RequiredOptions["TargetLogo"][0],
            'TARGET_PHONE': self.RequiredOptions["TargetPhone"][0],
            'TARGET_COMP_NAME': self.RequiredOptions["TargetCompany"][0],
            'TARGET_ADDR': self.RequiredOptions["TargetAddress"][0],
            'TARGET_WEB_LINK': self.RequiredOptions["TargetWebLink"][0],
        }

        with open(self.TemplatePath, 'r') as templateEmail:
            outputEmail = templateEmail.read()

        for dummy, value in replaceDict.iteritems():
            outputEmail = outputEmail.replace(dummy, value)
        return outputEmail
