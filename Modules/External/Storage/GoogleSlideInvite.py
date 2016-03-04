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
    self.OutputName = "GoogleSlidesInvite.eml"
    self.RenderName = "GoogleSlidesInvite.eml"
    self.CoreOptions = "[Text, Html, Link]"
    # Required for each class:
    self.Name = "Google Slides Invite to Edit."
    self.Author = "Killswitch-GUI"
    self.Type = "Html"
    self.Info = """A Google Slides invite to edit a presentation from a fellow Co-Worker."""
    self.Sophistication = "Medium" 
    self.SampleImage = str('''Modules/Sample/GoogleSlidesInvite.png''')
    self.TemplatePath = str('''Modules/EmailTemplates/GoogleSlidesInvite.email''')
    # Required options for itself:
    self.RequiredOptions = {
                              "FromEmail" : ["noreply@agency.com", "From Email"],
                              "FromName" : ["Alex Jason", "From Full Name"],
                              "TargetLink" : ["%URL%", "The full path link"],
                              "SlidesName" : ["HackTheWorld", "The name of the Google Slides shared"],
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
      'SHARE_DOCUMENT' : self.RequiredOptions["SlidesName"][0],
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
      'SHARE_DOCUMENT' : self.RequiredOptions["SlidesName"][0],
      }

    with open(self.TemplatePath, 'r') as templateEmail:
      outputEmail = templateEmail.read()

    for dummy, value in replaceDict.iteritems():
        outputEmail = outputEmail.replace(dummy, value)
    return outputEmail
