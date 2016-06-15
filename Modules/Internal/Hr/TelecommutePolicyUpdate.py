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
        self.OutputName = "TelecommutePolicyUpdate.mht"
        self.RenderName = "TelecommutePolicyUpdate.mht"
        self.CoreOptions = "[Text, Html, Link]"
        # Required for each class:
        self.Name = "Policy Update for employees to telecommute."
        self.Author = "Killswitch-GUI"
        self.Type = "Html"
        self.Info = """A very targeted email to corps that would support Telecommute options in the first place. Telling users a Policy Update  has taken place for employees."""
        self.Sophistication = "High"
        self.SampleImage = str(
            '''Modules/Sample/TelecommutPolicyUpdate.png''')
        self.TemplatePath = str(
            '''Modules/EmailTemplates/TelecommutePolicyUpdate.email''')
        # Required options for itself:
        self.RequiredOptions = {
            "FromEmail": ["noreply@agency.com", "From Email"],
            "FromName": ["Alex Jason", "From Full Name"],
            "FromTitle": ["Really Important CEO", "From Name Title"],
            "SignaturePhone": ["215-215-0000", "Signature block phone #"],
            "SignatureEmail" : ["alex.jason@Jason.com ", "Signature email address"],
            "ParentOrg" : ["ORG", "Set the Target parent ORG or the target name"],
            "TargetCompany": ["Cyber Power", "Set the Target Company Full Name"],
            "TargetLink": ["%URL%", "The full path link"],
            "NextQuater": ["Q1", "Next Fiscal Quater"],
            "CurrentYear": ["2016", "Current Year"],
            "DueDate": ["Sep 01, 2016", "The Due Date of the Form"],

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
            'FROM_PHONE': self.RequiredOptions["SignaturePhone"][0],
            'SIG_EMAIL': self.RequiredOptions["SignatureEmail"][0],
            'PARRENT_COMP_NAME': self.RequiredOptions["ParentOrg"][0],
            'TARGET_COMP_NAME': self.RequiredOptions["TargetCompany"][0],
            'TARGET_LINK': self.RequiredOptions["TargetLink"][0],
            'NEXT_QUATER': self.RequiredOptions["NextQuater"][0],
            'CUR_YEAR': self.RequiredOptions["CurrentYear"][0],
            'DUE_DATE': self.RequiredOptions["DueDate"][0],
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
            'FROM_PHONE': self.RequiredOptions["SignaturePhone"][0],
            'SIG_EMAIL': self.RequiredOptions["SignatureEmail"][0],
            'PARRENT_COMP_NAME': self.RequiredOptions["ParentOrg"][0],
            'TARGET_COMP_NAME': self.RequiredOptions["TargetCompany"][0],
            'TARGET_LINK': self.RequiredOptions["TargetLink"][0],
            'NEXT_QUATER': self.RequiredOptions["NextQuater"][0],
            'CUR_YEAR': self.RequiredOptions["CurrentYear"][0],
            'DUE_DATE': self.RequiredOptions["DueDate"][0],
        }

        with open(self.TemplatePath, 'r') as templateEmail:
            outputEmail = templateEmail.read()

        for dummy, value in replaceDict.iteritems():
            outputEmail = outputEmail.replace(dummy, value)
        return outputEmail
