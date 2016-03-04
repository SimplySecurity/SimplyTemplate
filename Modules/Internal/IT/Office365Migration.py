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
    self.OutputName = "Office365Migration.mht"
    self.RenderName = "Office365Migration.mht"
    self.CoreOptions = "[Text, Html, Link]"
    # Required for each class:
    self.Name = "Office 365 Migration email from IT"
    self.Author = "Killswitch-GUI"
    self.Type = "Text"
    self.Info = """This Targeted email works great with the correct Domain Name, 
                  and primary research to ensure that the target is using Office365 MX
                  Records of SPF TXT Records."""
    self.Sophistication = "High" 
    self.SampleImage = str('''Modules/Sample/Office365Migration.png''')
    self.TemplatePath = str('''Modules/EmailTemplates/Office365Migration.email''')
    # Required options for itself:
    self.RequiredOptions = {
                              "TargetCompany" : ["Cyber Power", "Set the Target Company Full Name" ],
                              "TargetLocation" : ["Las Vegas", "Set the Target Company State" ],
                              "TargetPhone" : ["1-800-CD-FOUR", "Set the Target Toll Free line" ],
                              "TargetLogo" : ["http://Target.com/logo.png", "Set the Target Logo" ],
                              "TargetLink" : ["%URL%", "The full path link"],
                              "FromEmail" : ["noreply@agency.com", "From Email"],
                            }
  def Generate(self, filename, location, Verbose=False):
    # Gen will get 
    # Filename = the name of the output
    # Location = Where do you want to place the output
    # Verbose = Print all help data
    # adapted from Andy
    replaceDict = {
      'FROM_EMAIL'    : self.RequiredOptions["FromEmail"][0],
      'TARGET_COMP_NAME' : self.RequiredOptions["TargetCompany"][0],
      'TARGET_LOGO' : self.RequiredOptions["TargetLogo"][0],
      'TARGET_LINK' : self.RequiredOptions["TargetLink"][0],
      'TARGET_PHONE' : self.RequiredOptions["TargetPhone"][0],
      'TARGET_LOCATION' : self.RequiredOptions["TargetLocation"][0],
      }
    WritePath =  str(filename) + str(location)

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
      'FROM_EMAIL'    : self.RequiredOptions["FromEmail"][0],
      'TARGET_COMP_NAME' : self.RequiredOptions["TargetCompany"][0],
      'TARGET_LOGO' : self.RequiredOptions["TargetLogo"][0],
      'TARGET_LINK' : self.RequiredOptions["TargetLink"][0],
      'TARGET_PHONE' : self.RequiredOptions["TargetPhone"][0],
      'TARGET_LOCATION' : self.RequiredOptions["TargetLocation"][0],
      }

    with open(self.TemplatePath, 'r') as templateEmail:
      outputEmail = templateEmail.read()

    for dummy, value in replaceDict.iteritems():
        outputEmail = outputEmail.replace(dummy, value)
    return outputEmail
