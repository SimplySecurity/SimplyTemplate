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
        self.OutputName = "EducationalPartnership.mht"
        self.RenderName = "EducationalPartnership.mht"
        self.CoreOptions = "[Text, Html, Link]"
        # Required for each class:
        self.Name = "Educational Partnership with local school for free $$"
        self.Author = "Killswitch-GUI"
        self.Type = "Text"
        self.Info = """A very simple email template using a standard link from a user Asking them to sign up for Educational Partnership benfits."""
        self.Sophistication = "Medium"
        self.SampleImage = str('''Modules/Sample/EducationalPartnership.png''')
        self.TemplatePath = str(
            '''Modules/EmailTemplates/EducationalPartnership.email''')
        # Required options for itself:
        self.RequiredOptions = {
            "HrDirector": ["Ray Mongo", "The full name of the Director of HR"],
            "FromEmail": ["noreply@agency.com", "From Email"],
            "StartYear": ["2017", "Start year of paperwork"],
            "StartMonth": ["September", "Start month of paperwork"],
            "TargetCompany": ["Cyber Power", "Set the Target Company Full Name"],
            "Url" : ["""%URL%""", "Link to payload or stat collection"],
            "PartnerSchoolAck" : ["Penn State University", "3 Letter abr of school"],
            "PartnerSchool" : ["PSU", "Full name of the school"],
        }

    def Generate(self, filename, location, Verbose=False):
        # Gen will get
        # Filename = the name of the output
        # Location = Where do you want to place the output
        # Verbose = Print all help data
        # adapted from Andy
        replaceDict = {
            'TARGET_HR_DIR': self.RequiredOptions["HrDirector"][0],
            'FROM_EMAIL': self.RequiredOptions["FromEmail"][0],
            'START_YEAR': self.RequiredOptions["StartYear"][0],
            'START_MONTH': self.RequiredOptions["StartMonth"][0],
            'TARGET_COMP_NAME': self.RequiredOptions["TargetCompany"][0],
            'TARGET_LINK': self.RequiredOptions["Url"][0],
            'PARTNER_SCHOOL_ACK': self.RequiredOptions["PartnerSchoolAck"][0],
            'PARTNER_SCHOOL': self.RequiredOptions["PartnerSchool"][0],
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
            'TARGET_HR_DIR': self.RequiredOptions["HrDirector"][0],
            'FROM_EMAIL': self.RequiredOptions["FromEmail"][0],
            'START_YEAR': self.RequiredOptions["StartYear"][0],
            'START_MONTH': self.RequiredOptions["StartMonth"][0],
            'TARGET_COMP_NAME': self.RequiredOptions["TargetCompany"][0],
            'TARGET_LINK': self.RequiredOptions["Url"][0],
            'PARTNER_SCHOOL_ACK': self.RequiredOptions["PartnerSchoolAck"][0],
            'PARTNER_SCHOOL': self.RequiredOptions["PartnerSchool"][0],
        }

        with open(self.TemplatePath, 'r') as templateEmail:
            outputEmail = templateEmail.read()

        for dummy, value in replaceDict.iteritems():
            outputEmail = outputEmail.replace(dummy, value)

        return outputEmail
