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
    self.OutputName = "OPMSalaryGuidelines.Html"
    self.CoreOptions = "[Html, Link]"
    # Required for each class:
    self.Name = "Salary guidelines for the fiscal year."
    self.Author = "Killswitch-GUI"
    self.Type = "Html"
    self.Info = """A small template with salary updates from OPM, this will work great at the end of the
                    fiscal year within GOV agencies."""
    self.Sophistication = "Medium" 
    self.SampleImage = str('''Modules/Sample/OPMSalaryGuidelines.png''')
    self.TemplatePath = str('''Modules/EmailTemplates/OPMSalaryGuidelines.email''')
    # Required options for itself:
    self.RequiredOptions = {
                              "FromEmail" : ["noreply@agency.com", "From Email"],
                              "FromName" : ["Alex Jason", "From Full Name"],
                              "CurrentYear" : ["2016", "Current Year"],
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
      'FROM_NAME'    : self.RequiredOptions["FromName"][0],
      'TARGET_LINK'    : self.RequiredOptions["TargetLink"][0],
      'TARGET_COMP_NAME' : self.RequiredOptions["TargetCompany"][0],
      'CUR_YEAR'   : self.RequiredOptions["CurrentYear"][0],
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
      'FROM_NAME'    : self.RequiredOptions["FromName"][0],
      'TARGET_LINK'    : self.RequiredOptions["TargetLink"][0],
      'TARGET_COMP_NAME' : self.RequiredOptions["TargetCompany"][0],
      'CUR_YEAR'   : self.RequiredOptions["CurrentYear"][0],
      }

    with open(self.TemplatePath, 'r') as templateEmail:
      outputEmail = templateEmail.read()

    for dummy, value in replaceDict.iteritems():
        outputEmail = outputEmail.replace(dummy, value)
    return outputEmail
