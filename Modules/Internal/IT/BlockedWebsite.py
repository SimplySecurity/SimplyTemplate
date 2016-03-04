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
    self.OutputName = "BlockedWebsite.html"
    self.RenderName = "BlockedWebsite.html"
    self.CoreOptions = "[Html, Link]"
    # Required for each class:
    self.Name = "=IT SOC Alert that you have visted a BlockedWebsite"
    self.Author = "Killswitch-GUI"
    self.Type = "Text"
    self.Info = """This targeted email informs the user that the requested site was blocked by the SOC. Than asking the user to answer a few simple questions"""
    self.Sophistication = "Medium" 
    self.SampleImage = str('''Modules/Sample/BlockedWebsite.png''')
    self.TemplatePath = str('''Modules/EmailTemplates/BlockedWebsite.email''')
    # Required options for itself:
    self.RequiredOptions = {
                              "TargetCompany" : ["IRS", "Set the Target Company Full Name" ],
                              "TargetLink" : ["http://Target.com/site.pdf", "Set the target link" ],
                              "TargetPhone" : ["1-800-CD-FOUR", "Set the Target Toll Free line" ],
                              "TodaysDate" : ["Jan 1, 2016", "Set the proper phish date" ],
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
      'TODAYS_DATE' : self.RequiredOptions["TodaysDate"][0],
      'TARGET_COMP_NAME' : self.RequiredOptions["TargetCompany"][0],
      'TARGET_LINK' : self.RequiredOptions["TargetLink"][0],
      'TARGET_PHONE' : self.RequiredOptions["TargetPhone"][0],
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
      'TODAYS_DATE' : self.RequiredOptions["TodaysDate"][0],
      'TARGET_COMP_NAME' : self.RequiredOptions["TargetCompany"][0],
      'TARGET_LINK' : self.RequiredOptions["TargetLink"][0],
      'TARGET_PHONE' : self.RequiredOptions["TargetPhone"][0],
      }

    with open(self.TemplatePath, 'r') as templateEmail:
      outputEmail = templateEmail.read()

    for dummy, value in replaceDict.iteritems():
        outputEmail = outputEmail.replace(dummy, value)
    return outputEmail
