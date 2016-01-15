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
    self.OutputName = "FoxNews.Html"
    self.CoreOptions = "[Text, Link]"
    # Required for each class:
    self.Name = "Fox News Basic Link"
    self.Author = "Killswitch-GUI"
    self.Type = "Text"
    self.Info = """A very simple email template using a standard link from a user
                   Asking them to open a news article."""
    self.Sophistication = "Low" 
    self.SampleImage = str('''Modules/Sample/FoxNews.png''')
    self.TemplatePath = str('''Modules/EmailTemplates/FoxNewsBasicTemplate.email''')
    # Required options for itself:
    self.RequiredOptions = {
                              "FromFullName" : ["Jim Bob", "Full Name of sender"],
                              "FromEmail" : ["noreply@agency.com", "From Email"],
                              "FromFirstName" : ["Jim", "Contacts First Name"],
                              "SubjectTitle" : ["Interesting News Article", "Contacts Full Title"],
                            }
  def Generate(self, filename, location, Verbose=False):
    # Gen will get 
    # Filename = the name of the output
    # Location = Where do you want to place the output
    # Verbose = Print all help data
    # adapted from Andy
    replaceDict = {
      'FROM_FULL_NAME'    : self.RequiredOptions["FromFullName"][0],
      'FROM_EMAIL'    : self.RequiredOptions["FromEmail"][0],
      'FROM_FIRST_NAME'   : self.RequiredOptions["FromFirstName"][0],
      'SUBJECT_TITLE'    : self.RequiredOptions["SubjectTitle"][0]
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
      'FROM_EMAIL'    : self.RequiredOptions["FromEmail"][0],
      'FROM_FIRST_NAME'   : self.RequiredOptions["FromFirstName"][0],
      'SUBJECT_TITLE'    : self.RequiredOptions["SubjectTitle"][0]
      }

    with open(self.TemplatePath, 'r') as templateEmail:
      outputEmail = templateEmail.read()

    for dummy, value in replaceDict.iteritems():
        outputEmail = outputEmail.replace(dummy, value)

    return outputEmail
