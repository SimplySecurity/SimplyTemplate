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
        self.OutputName = "FoxNews.html"
        self.RenderName = "FoxNews.html"
        self.CoreOptions = "[Text, Link]"
        # Required for each class:
        self.Name = "Fox News Basic Link"
        self.Author = "Killswitch-GUI"
        self.Type = "Text"
        self.Info = """A very simple email template using a standard link from a user Asking them to open a news article."""
        self.Sophistication = "Low"
        self.SampleImage = str('''Modules/Sample/FoxNews.png''')
        self.TemplatePath = str(
            '''Modules/EmailTemplates/FoxNewsBasicTemplate.email''')
        # Required options for itself:
        self.RequiredOptions = {
            "FromFullName": ["Jim Bob", "Full Name of sender"],
            "FromEmail": ["noreply@agency.com", "From Email"],
            "FromFirstName": ["Jim", "Contacts First Name"],
            "SubjectTitle": ["Interesting News Article", "Contacts Full Title"],
        }
        self.RequiredText = {
            "TextBlock1": ["Hey,", "Open Statment"],
            "TextBlock2": ["Check out this article from FoxNews...",  "Main Body"],
            "TextBlock3": ["Article",  "Secondary Paragraph"],
            "TextBlock4": ["Thanks,", "Closing Statment"],
        }

    def Generate(self, filename, location, Verbose=False):
        # Gen will get
        # Filename = the name of the output
        # Location = Where do you want to place the output
        # Verbose = Print all help data
        # adapted from Andy
        replaceDict = {
            'FROM_FULL_NAME': self.RequiredOptions["FromFullName"][0],
            'FROM_EMAIL': self.RequiredOptions["FromEmail"][0],
            'FROM_FIRST_NAME': self.RequiredOptions["FromFirstName"][0],
            'SUBJECT_TITLE': self.RequiredOptions["SubjectTitle"][0]
        }

        replaceTextDict = {
            'TEXT_BLOCK_1': self.RequiredText["TextBlock1"][0],
            'TEXT_BLOCK_2': self.RequiredText["TextBlock2"][0],
            'TEXT_BLOCK_3': self.RequiredText["TextBlock3"][0],
            'TEXT_BLOCK_4': self.RequiredText["TextBlock4"][0],
        }
        WritePath = str(filename) + str(location)

        with open(self.TemplatePath, 'r') as templateEmail:
            outputEmail = templateEmail.read()

        for dummy, value in replaceTextDict.iteritems():
            outputEmail = outputEmail.replace(dummy, value)

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
            'FROM_FULL_NAME': self.RequiredOptions["FromFullName"][0],
            'FROM_EMAIL': self.RequiredOptions["FromEmail"][0],
            'FROM_FIRST_NAME': self.RequiredOptions["FromFirstName"][0],
            'SUBJECT_TITLE': self.RequiredOptions["SubjectTitle"][0]
        }

        replaceTextDict = {
            'TEXT_BLOCK_1': self.RequiredText["TextBlock1"][0],
            'TEXT_BLOCK_2': self.RequiredText["TextBlock2"][0],
            'TEXT_BLOCK_3': self.RequiredText["TextBlock3"][0],
            'TEXT_BLOCK_4': self.RequiredText["TextBlock4"][0],
        }

        with open(self.TemplatePath, 'r') as templateEmail:
            outputEmail = templateEmail.read()

        for dummy, value in replaceTextDict.iteritems():
            outputEmail = outputEmail.replace(dummy, value)

        for dummy, value in replaceDict.iteritems():
            outputEmail = outputEmail.replace(dummy, value)

        return outputEmail
