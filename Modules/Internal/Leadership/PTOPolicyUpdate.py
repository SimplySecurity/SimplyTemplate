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
        self.OutputName = "PTOPolicyUpdate.mht"
        self.RenderName = "PTOPolicyUpdate.mht"
        self.CoreOptions = "[Text, Html, Link]"
        # Required for each class:
        self.Name = "PTO Policy Update from manangment"
        self.Author = "Killswitch-GUI"
        self.Type = "Html"
        self.Info = """This Highly targted email asks for the user base to read the updated PTO guidelines attached."""
        self.Sophistication = "High"
        self.SampleImage = str('''Modules/Sample/PTOPolicyUpdate.png''')
        self.TemplatePath = str(
            '''Modules/EmailTemplates/PTOPolicyUpdate.email''')
        # Required options for itself:
        self.RequiredOptions = {
            "FromName": ["Jeff Manny", "Set the from name"],
            "FromEmail": ["noreply@agency.com", "From Email"],
            "FromTitle": ["CEO, ATD", "Contacts Full Title"],
            "FromRealEmail": ["alex@target.com", "The Target CFO real email"],
            "FutureDate": ["Sep 1, 2016", "Set the future date to complete document"],
            "TargetWebLink": ["Target.com", "Set the real target web link"],
            "TargetCompany": ["Cyber Power", "Set the Target Company Full Name"],
            "TargetAddress": ["123 Street Las Vegas, NV, 12345", "Set the Target Company Addr"],
            "TargetLocation": ["Las Vegas", "Set the Target Company State"],
            "TargetPhone": ["1-800-CD-FOUR", "Set the Target Toll Free line"],
            "TargetLogo": ["http://Target.com/logo.png", "Set the Target Logo"],
        }

    def Generate(self, filename, location, Verbose=False):
        # Gen will get
        # Filename = the name of the output
        # Location = Where do you want to place the output
        # Verbose = Print all help data
        # adapted from Andy
        replaceDict = {
            'FROM_EMAIL': self.RequiredOptions["FromEmail"][0],
            'FROM_NAME': self.RequiredOptions["FromName"][0],
            'FROM_TITLE': self.RequiredOptions["FromTitle"][0],
            'FROM_REAL_EMAIL': self.RequiredOptions["FromRealEmail"][0],
            'FUTURE_DATE': self.RequiredOptions["FutureDate"][0],
            'TARGET_COMP_NAME': self.RequiredOptions["TargetCompany"][0],
            'TARGET_ADDR': self.RequiredOptions["TargetAddress"][0],
            'TARGET_LOGO': self.RequiredOptions["TargetLogo"][0],
            'TARGET_PHONE': self.RequiredOptions["TargetPhone"][0],
            'TARGET_LOCATION': self.RequiredOptions["TargetLocation"][0],
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
            'FROM_NAME': self.RequiredOptions["FromName"][0],
            'FROM_TITLE': self.RequiredOptions["FromTitle"][0],
            'FROM_REAL_EMAIL': self.RequiredOptions["FromRealEmail"][0],
            'FUTURE_DATE': self.RequiredOptions["FutureDate"][0],
            'TARGET_COMP_NAME': self.RequiredOptions["TargetCompany"][0],
            'TARGET_ADDR': self.RequiredOptions["TargetAddress"][0],
            'TARGET_LOGO': self.RequiredOptions["TargetLogo"][0],
            'TARGET_PHONE': self.RequiredOptions["TargetPhone"][0],
            'TARGET_LOCATION': self.RequiredOptions["TargetLocation"][0],
            'TARGET_WEB_LINK': self.RequiredOptions["TargetWebLink"][0],
        }

        with open(self.TemplatePath, 'r') as templateEmail:
            outputEmail = templateEmail.read()

        for dummy, value in replaceDict.iteritems():
            outputEmail = outputEmail.replace(dummy, value)
        return outputEmail
