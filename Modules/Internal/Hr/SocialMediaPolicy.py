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
    self.OutputName = "SocialMediaPolicy.Html"
    self.CoreOptions = "[Text, Html, Attachment]"
    # Required for each class:
    self.Name = "Social Media Policy Signature Request"
    self.Author = "Killswitch-GUI"
    self.Type = "Text"
    self.Info = """A very simple email template using a Attahment to deliver
                   Payload and asking them to sign the OLE PDF."""
    self.Sophistication = "Low" 
    self.SampleImage = str('''Modules/Sample/SocialMediaPolicy.png''')
    self.TemplatePath = str('''Modules/EmailTemplates/SocialMediaPolicy.email''')
    # Required options for itself:
    self.RequiredOptions = {
                              "HrDirector" : ["Ray Mongo", "The full name of the Director of HR"],
                              "FromEmail" : ["noreply@agency.com", "From Email"],
                              "TargetCompany" : ["Cyber Power", "Set the Target Company Full Name" ],
                            }
  def Generate(self, filename, location, Verbose=False):
    # Gen will get 
    # Filename = the name of the output
    # Location = Where do you want to place the output
    # Verbose = Print all help data
    # adapted from Andy
    replaceDict = {
      'TARGET_HR_DIR' : self.RequiredOptions["HrDirector"][0],
      'FROM_EMAIL'    : self.RequiredOptions["FromEmail"][0],
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
      'TARGET_HR_DIR' : self.RequiredOptions["HrDirector"][0],
      'FROM_EMAIL'    : self.RequiredOptions["FromEmail"][0],
      'TARGET_COMP_NAME' : self.RequiredOptions["TargetCompany"][0],
      }

    with open(self.TemplatePath, 'r') as templateEmail:
      outputEmail = templateEmail.read()

    for dummy, value in replaceDict.iteritems():
        outputEmail = outputEmail.replace(dummy, value)
    return outputEmail
