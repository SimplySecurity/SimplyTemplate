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
    self.OutputName = "LinkedinGroup.mht"
    self.CoreOptions = "[Text, Html, Link]"
    # Required for each class:
    self.Name = "Linkedin Group Invite"
    self.Author = "Killswitch-GUI"
    self.Type = "HTML/Text"
    self.Info = """Linkedin uses a very common setup for group and user invites. This template 
                   takes advantage of this and uses the Rich HTML from a real email. Places your data 
                   into the template and generates a Html/Text Template for you."""
    self.Sophistication = "Medium" 
    self.SampleImage = str('''Modules/Sample/LinkedinGroup.png''')
    self.TemplatePath = str('''Modules/EmailTemplates/LinkedinGroupTemplate.email''')
    # Required options for itself:
    self.RequiredOptions = {
                              "FromFullName" : ["Jim Bob", "Contacts Full Name"],
                              "FromFirstName" : ["Jim", "Contacts First Name"],
                              "FromProfileUrl" : ["http://k.com", "Linkedin Full Profile URL"],
                              "FromTitle" : ["CEO, ATD", "Contacts Full Title"],
                              "FromOrg" : ["Veris Group, LLC", "Contacts Company"],
                              "GroupName" : ["Cyber Cyber Cyber", "Requested Group to Join"],
                              "GroupUrl" : ["""%URL%""", "Custom GroupURL or CS URL"],
                              "ProfilePic" : ["http://tinyurl.com/oewvyo7", "Custom GroupURL or CS URL"],
                            }
  def Generate(self, filename, location, Verbose=False):
    # Gen will get 
    # Filename = the name of the output
    # Location = Where do you want to place the output
    # Verbose = Print all help data
    # adapted from Andy
    replaceDict = {
      'FROM_FULL_NAME'    : self.RequiredOptions["FromFullName"][0],
      'FROM_FIRST_NAME'   : self.RequiredOptions["FromFirstName"][0],
      'FROM_PROFILE_URL'    : self.RequiredOptions["FromProfileUrl"][0],
      'FROM_TITLE'    : self.RequiredOptions["FromTitle"][0],
      'FROM_ORGANIZATION'   : self.RequiredOptions["FromOrg"][0],
      'GROUP_NAME'    : self.RequiredOptions["GroupName"][0],
      'GROUP_URL'     : self.RequiredOptions["GroupUrl"][0],
      'PROFILE_PIC_URL'   : self.RequiredOptions["ProfilePic"][0]
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
      'FROM_FULL_NAME'    : self.RequiredOptions["FromFullName"][0],
      'FROM_FIRST_NAME'   : self.RequiredOptions["FromFirstName"][0],
      'FROM_PROFILE_URL'    : self.RequiredOptions["FromProfileUrl"][0],
      'FROM_TITLE'    : self.RequiredOptions["FromTitle"][0],
      'FROM_ORGANIZATION'   : self.RequiredOptions["FromOrg"][0],
      'GROUP_NAME'    : self.RequiredOptions["GroupName"][0],
      'GROUP_URL'     : self.RequiredOptions["GroupUrl"][0],
      'PROFILE_PIC_URL'   : self.RequiredOptions["ProfilePic"][0]
      }

    with open(self.TemplatePath, 'r') as templateEmail:
      outputEmail = templateEmail.read()

    for dummy, value in replaceDict.iteritems():
        outputEmail = outputEmail.replace(dummy, value)

    return outputEmail
