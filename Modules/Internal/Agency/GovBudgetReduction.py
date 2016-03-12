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
    self.OutputName = "GovBudgetReduction.html"
    self.RenderName = "GovBudgetReduction.html"
    self.CoreOptions = "[Html, Link]"
    # Required for each class:
    self.Name = "Mangment email on sequestration of the Gov."
    self.Author = "Killswitch-GUI"
    self.Type = "Html"
    self.Info = """A template focusing on long term financial issues and how to avoid sequestration. This template will be a good fit for must State/Gov orgs."""
    self.Sophistication = "Medium" 
    self.SampleImage = str('''Modules/Sample/GovBudgetReduction.png''')
    self.TemplatePath = str('''Modules/EmailTemplates/GovBudgetReduction.email''')
    # Required options for itself:
    self.RequiredOptions = {
                              "FromEmail" : ["noreply@agency.com", "From Email"],
                              "FromName" : ["Alex Jason", "From Full Name"],
                              "TodaysDate" : ["Jan 1, 2016", "Set the proper phish date" ],
                              "TargetCompany" : ["Cyber Power", "Set the Target Company Full Name" ],
                              "TargetLink" : ["%URL%", "The full path link"],
                            }
    self.RequiredText = {
                          "TextBlock1" : ["""In the coming weeks our nations leadership will be working to draft a plan to prevent long term financial issues and how to avoid the "sequestration" that we have all heard about for the past few months. All departments within the US Government are being directed to draft plans to help meet the projected budget shortfalls and find ways to reducing spending within the US Government.""", "Paragraph one"],
                          "TextBlock2" : ["As a result the TARGET_COMP_NAME has developed a plan that will reduce the Information Technology budget by 25% over the next 18 months. This budget will include a reduction of current staff levels and also place a hiring freeze on new hires for the next 2 years. Current contractor staff will also be reduced by 20% to help drive a more lean workforce.", "Paragraph two"],
                          "TextBlock3" : ["The country has asked us all to learn to work more efficiently and do more with less. As a result many budgets and programs are also facing significant reductions. The senior management within TARGET_COMP_NAME will work with their teams to ensure a smooth transition process and will do all they can to help reduce the stress and uncertainties that come with any significant changes such as this.", "Paragraph three"],
                          "TextBlock4" : ["To read more about the budget plan for TODAYS_DATE please see the following page which outlines how this plan will be implemented and the projected time frames for the transitions.", "Ending Paragraph"],
                          "TextBlock5" : ["TARGET_COMP_NAME Management Team", "Signature Block"]
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
      'TODAYS_DATE' : self.RequiredOptions["TodaysDate"][0],
      }
    replaceTextDict = {
      'TEXT_BLOCK_1' : self.RequiredText["TextBlock1"][0],
      'TEXT_BLOCK_2' : self.RequiredText["TextBlock2"][0],
      'TEXT_BLOCK_3' : self.RequiredText["TextBlock3"][0],
      'TEXT_BLOCK_4' : self.RequiredText["TextBlock4"][0],
      'TEXT_BLOCK_5' : self.RequiredText["TextBlock5"][0],
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
      'FROM_NAME'    : self.RequiredOptions["FromName"][0],
      'TARGET_LINK'    : self.RequiredOptions["TargetLink"][0],
      'TARGET_COMP_NAME' : self.RequiredOptions["TargetCompany"][0],
      'TODAYS_DATE' : self.RequiredOptions["TodaysDate"][0],
      }
    replaceTextDict = {
      'TEXT_BLOCK_1' : self.RequiredText["TextBlock1"][0],
      'TEXT_BLOCK_2' : self.RequiredText["TextBlock2"][0],
      'TEXT_BLOCK_3' : self.RequiredText["TextBlock3"][0],
      'TEXT_BLOCK_4' : self.RequiredText["TextBlock4"][0],
      'TEXT_BLOCK_5' : self.RequiredText["TextBlock5"][0],
      }
    with open(self.TemplatePath, 'r') as templateEmail:
      outputEmail = templateEmail.read()

    for dummy, value in replaceTextDict.iteritems():
        outputEmail = outputEmail.replace(dummy, value)

    for dummy, value in replaceDict.iteritems():
        outputEmail = outputEmail.replace(dummy, value)
    return outputEmail
