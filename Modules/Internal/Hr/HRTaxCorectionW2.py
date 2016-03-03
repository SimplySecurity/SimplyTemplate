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
    self.OutputName = "HRTaxCorrectionW2.Html"
    self.CoreOptions = "[Text, Html, Link]"
    # Required for each class:
    self.Name = "HR request for target to use link or download file to view"
    self.Author = "Killswitch-GUI"
    self.Type = "Html"
    self.Info = """A moderate template that is used to entice users 
                  to either download a file or click a link."""
    self.Sophistication = "Medium" 
    self.SampleImage = str('''Modules/Sample/HRTaxCorrectionW2.png''')
    self.TemplatePath = str('''Modules/EmailTemplates/HRTaxCorrectionW2.email''')
    # Required options for itself:
    self.RequiredOptions = {
                              "FromEmail" : ["noreply@agency.com", "From Email"],
                              "TargetCompany" : ["Cyber Power", "Set the Target Company Full Name" ],
                              "TargetLink" : ["%URL%", "The full path link"],
                            }
  def Generate(self, filename, location, Verbose=False):
    # Gen will get 
    # Filename = the name of the output
    # Location = Where do you want to place the output
    # Verbose = Print all help data
    # adapted from Andy
    replaceDict = {
      'FROM_EMAIL' : self.RequiredOptions["FromEmail"][0],
      'TARGET_LINK'    : self.RequiredOptions["TargetLink"][0],
      'TARGET_COMP_NAME' : self.RequiredOptions["TargetCompany"][0],
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
      'FROM_EMAIL' : self.RequiredOptions["FromEmail"][0],
      'TARGET_LINK'    : self.RequiredOptions["TargetLink"][0],
      'TARGET_COMP_NAME' : self.RequiredOptions["TargetCompany"][0],
      }

    with open(self.TemplatePath, 'r') as templateEmail:
      outputEmail = templateEmail.read()

    for dummy, value in replaceDict.iteritems():
        outputEmail = outputEmail.replace(dummy, value)
    return outputEmail
