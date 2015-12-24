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
    # Required for each class:
    self.Name = "Linkedin Group Invite"
    self.Author = "Killswitch-GUI"
    self.Info = """Linkedin uses a very common setup for group and user invites. This template 
                   takes advantage of this and uses the Rich HTML from a real email. Places your data 
                   into the template and generates a Html/Text Template for you."""
    self.Sophistication = "Medium" 
    self.SampleImage = str('''Modules/Sample/LinkedinGroup.png''')
    # Required options for itself:
    self.RequiredOptions = {
                              "FromFullName" : ["Jim Bob", "Contacts Full Name"],
                              "FromFirstName" : ["Jim", "Contacts First Name"],
                              "FromProfileUrl" : ["http://k.com", "Linkedin Full Profile URL"],
                              "FromTitle" : ["CEO, ATD", "Contacts Full Title"],
                              "FromOrg" : ["Veris Group, LLC", "Contacts Company"],
                              "GroupName" : ["Cyber Cyber Cyber", "Requested Group to Join"],
                              "GroupUrl" : ["""%URL%""", "Custom GroupURL or CS URL"],
                              "ProfilePic" : ["http://pic.com", "Custom GroupURL or CS URL"],
                            }
  def Generate(self, Verbose=False):
    print "hi"