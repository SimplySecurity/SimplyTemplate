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
    self.OutputName = "AppleEncryptionFBI.Html"
    self.CoreOptions = "[Text, Html, Link]"
    # Required for each class:
    self.Name = "Apple FBI Encryption stance from leadership"
    self.Author = "Killswitch-GUI"
    self.Type = "Text"
    self.Info = """This broad email explains Apples current issues faced with Encryption,
                    while providing leadership insight into the issue. This will work well
                    with Gov agency's as well as IT corps."""
    self.Sophistication = "Low" 
    self.SampleImage = str('''Modules/Sample/AppleEncryptionFBI.png''')
    self.TemplatePath = str('''Modules/EmailTemplates/AppleEncryptionFBI.email''')
    # Required options for itself:
    self.RequiredOptions = {
                              "TargetCompany" : ["IRS", "Set the Target Company Full Name" ],
                              "TargetLink" : ["http://Target.com/site.pdf", "Set the target link" ],
                              "FromName" : ["Jeff Manny", "Set the from name" ],
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
      'TARGET_LINK' : self.RequiredOptions["TargetLink"][0],
      'FROM_NAME' : self.RequiredOptions["FromName"][0],
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
      'TARGET_LINK' : self.RequiredOptions["TargetLink"][0],
      'FROM_NAME' : self.RequiredOptions["FromName"][0],
      }

    with open(self.TemplatePath, 'r') as templateEmail:
      outputEmail = templateEmail.read()

    for dummy, value in replaceDict.iteritems():
        outputEmail = outputEmail.replace(dummy, value)
    return outputEmail
