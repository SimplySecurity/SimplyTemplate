#!/usr/bin/python
import os
from Helpers import TemplateEdit
# Class funcs will have:
# -Name
# -Author
# -Sophistication
# -Info

# Required Options for the class

class TemplateModule:

  def __init__(self):
    # Meta Tags for file name and such:
    self.OutputName = "IRS-CorrectedW2.mht"
    self.RenderName = "IRS-CorrectedW2.mht"
    self.CoreOptions = "[Text, Html, Link]"
    # Required for each class:
    self.Name = "Simple IRS phish to inform user their W2 is wrong and the IRS has been reported a Corrected version"
    self.Author = "Killswitch-GUI"
    self.Type = "Html"
    self.Info = """A moderate template that is used to entice users to either download a file or click a link."""
    self.Sophistication = "Low" 
    self.SampleImage = str('''Modules/Sample/IRS-CorrectedW2.png''')
    self.TemplatePath = str('''Modules/EmailTemplates/IRS-CorrectedW2.email''')
    # Required options for itself:
    self.RequiredOptions = {
                              "FromEmail" : ["noreply@agency.com", "From Email"],
                              "FromAgency" : ["Internal Revenue Service", "From Agency"],
                              "TaxYear" : ["2015", "Previous year / Tax Seasson"],
                              "TargetLink" : ["%URL%", "The full path link"],

                            }
    self.RequiredText = {
                              "TextBlock1" : ["Dear User,", "Open Statment"],
                              "TextBlock2" : ["Sir / Madam, the IRS just received an electronic notice from your employer of a W-2c (W-2 Corrected). This email is in correspondence to inform you that (change / update) may be needed for your TAX_YEAR tax return. Please follow the link to be informed of your rights and instructions to refile your return.", "Main Paragraph"],
                              "TextBlock3" : ["Sorry for any inconvenience this has caused.", "Secondary Paragraph"],
                            }                          
  def Generate(self, filename, location, Verbose=False):
    # Gen will get 
    # Filename = the name of the output
    # Location = Where do you want to place the output
    # Verbose = Print all help data
    # adapted from Andy
    replaceDict = {
      'FROM_EMAIL' : self.RequiredOptions["FromEmail"][0],
      'FROM_AGENCY' : self.RequiredOptions["FromAgency"][0],
      'TARGET_LINK'    : self.RequiredOptions["TargetLink"][0],
      'TAX_YEAR'    : self.RequiredOptions["TaxYear"][0],
      }
    replaceTextDict = {
      'TEXT_BLOCK_1' : self.RequiredText["TextBlock1"][0],
      'TEXT_BLOCK_2' : self.RequiredText["TextBlock2"][0],
      'TEXT_BLOCK_3' : self.RequiredText["TextBlock3"][0],
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
      'FROM_EMAIL' : self.RequiredOptions["FromEmail"][0],
      'FROM_AGENCY' : self.RequiredOptions["FromAgency"][0],
      'TARGET_LINK'    : self.RequiredOptions["TargetLink"][0],
      'TAX_YEAR'    : self.RequiredOptions["TaxYear"][0],
      }
    replaceTextDict = {
      'TEXT_BLOCK_1' : self.RequiredText["TextBlock1"][0],
      'TEXT_BLOCK_2' : self.RequiredText["TextBlock2"][0],
      'TEXT_BLOCK_3' : self.RequiredText["TextBlock3"][0],
      }
    with open(self.TemplatePath, 'r') as templateEmail:
      outputEmail = templateEmail.read()

    for dummy, value in replaceTextDict.iteritems():
        outputEmail = outputEmail.replace(dummy, value)

    for dummy, value in replaceDict.iteritems():
        outputEmail = outputEmail.replace(dummy, value)
    return outputEmail
