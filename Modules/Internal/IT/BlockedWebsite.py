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
    self.RequiredText = {
                          "TextBlock1" : ["It has been determined that your workstation is attempting to browse multiple blocked websites and we need your verification.", "Notice Statment"],
                          "TextBlock2" : ["If you did not make these requests, it is possible that your system has been compromised. Starting TODAYS_DATE, the Client Services Implementation Team will be reviewing your answers to the verification poll below. If you did not make these requests, the TARGET_COMP_NAME Security Operations Center (SOC) will need to remotely review your system for anomalies. If you were the one attempting to access these sites, no action will be taken and you are only asked to respect IT security policies in the future.", "Subject Statment"],
                          "TextBlock3" : ["Please click the following link to answer a few simple questions:", "Remediation"],
                          "TextBlock4" : ["Please contact your TARGET_COMP_NAME Information Security Officer through the contact link at the website listed above.", "Contact"]
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
    replaceTextDict = {
      'TEXT_BLOCK_1' : self.RequiredText["TextBlock1"][0],
      'TEXT_BLOCK_2' : self.RequiredText["TextBlock2"][0],
      'TEXT_BLOCK_3' : self.RequiredText["TextBlock3"][0],
      'TEXT_BLOCK_4' : self.RequiredText["TextBlock4"][0],
      }
    WritePath =  str(filename) + str(location)

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
      'FROM_EMAIL'    : self.RequiredOptions["FromEmail"][0],
      'TODAYS_DATE' : self.RequiredOptions["TodaysDate"][0],
      'TARGET_COMP_NAME' : self.RequiredOptions["TargetCompany"][0],
      'TARGET_LINK' : self.RequiredOptions["TargetLink"][0],
      'TARGET_PHONE' : self.RequiredOptions["TargetPhone"][0],
      }
    replaceTextDict = {
      'TEXT_BLOCK_1' : self.RequiredText["TextBlock1"][0],
      'TEXT_BLOCK_2' : self.RequiredText["TextBlock2"][0],
      'TEXT_BLOCK_3' : self.RequiredText["TextBlock3"][0],
      'TEXT_BLOCK_4' : self.RequiredText["TextBlock4"][0],
      }

    with open(self.TemplatePath, 'r') as templateEmail:
      outputEmail = templateEmail.read()

    for dummy, value in replaceTextDict.iteritems():
        outputEmail = outputEmail.replace(dummy, value)

    for dummy, value in replaceDict.iteritems():
        outputEmail = outputEmail.replace(dummy, value)
    return outputEmail
