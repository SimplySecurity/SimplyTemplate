import imp
import glob
import configparser
import os
import sys
import warnings
import time
import subprocess
import re
from Helpers import Helpers 


class Conducter:

    def __init__(self):
        self.version = "v0.1"
        # Create dictionaries of supported modules
        # empty until stuff loaded into them
        # stolen from Veil :)
        self.Modules = {}
        self.Dmodules = {}
        self.LoadModules()
        self.Commands = [   ("use","Select a template for use"),
                            ("list","List loaded Templates"),
                            ("info","Display metadata about a module"),
                            ("update","Update SimplyTemplate from Github"),
                            ("help","Display this menu"),
                            ("exit","Exit SimplyTemplate")]
        self.TemplateInfo =[   ("Name:"),
                                ("Author"),
                                ("Sophistication:"),
                                ("Info:")]
        
        # create required array
    
    def LoadModules(self):
        # loop and assign key and name
        warnings.filterwarnings('ignore', '.*Parent module*',)
        x = 1
        for name in glob.glob('Modules/*.py'):
            if name.endswith(".py") and ("__init__" not in name):
                loaded_modules = imp.load_source(
                    name.replace("/", ".").rstrip('.py'), name)
                self.Modules[name] = loaded_modules
                self.Dmodules[x] = loaded_modules
                x += 1
        #print self.Dmodules
        #print self.Modules

    def ListModules(self):
        self.TitleScreen()
        print Helpers.color(" [*] Available Modules are:\n", blue=True)
        lastBase = None
        x = 1
        for name in self.Modules:
            parts = name.split("/")
            if lastBase and parts[0] != lastBase:
                print ""
            lastBase = parts[0]
            print "\t%s)\t%s" % (x, '{0: <24}'.format(name))
            x += 1
        print ""

    def MainMenu(self):
        print " Main Selection Menu\n"
        print "\t"+str(len(self.Modules))+" Email Template Loaded\n"
        print " Commands:\n"
        for item in self.Commands:
            if item[0] == "update":
                print "\t[" + item[0] + "]\t" + item[1]
            else:
                print "\t[" + item[0] + "]\t\t" + item[1]

    def PromptSelection(self):
        # We also have to strip off and verfiy the number
        # make sure we strip when checking command
        p = " [>] "
        a = raw_input(Helpers.color(p,status=True))
        # Gives me a list of words of ints
        try:
            Split = Helpers.GetWords(a)
            if Split[0].lower() == "use" or Split[0].lower() == "u":
                # we will use this to select our module of choice
                # it will call a seprate function to handle the Int
                # of the requested module
                self.ModuleSelection(Split)
            if Split[0].lower() == "info" or Split[0].lower() == "i":
                self.ModuleInfo(Split)
        except Exception as e:
            print e 
            pass
        if a.lower() == "help" or a.lower() == "h" or a.lower() == "?":
            print "\tAvailiable Commands:"
            print "\t-----------------------------------------"
            for item in self.Commands:
                if item[0] == "update":
                    print "\t[" + item[0] + "]\t" + item[1]
                else:
                    print "\t[" + item[0] + "]\t\t" + item[1]
            self.PromptSelection()
        if a.lower() == "list" or a.lower() == "l":
            self.ListModules()
            self.PromptSelection()
        if a.lower() == "update" or a.lower() == "u":
            Helpers.SelfUpdate()
        if a.lower() == "exit":
            Helpers.Exit()
        else:
            self.PromptSelection()
        return a

    def ModuleSelection(self, selection):
        ModuleInt = int(selection[1])
        try:
            SelectedModule = self.Dmodules[ModuleInt]
            Task = SelectedModule.TemplateModule()
        except Exception as e:
            print e
            p = " [!] Please select a valid Module number"
            print Helpers.color(p, firewall=True)
            return

    def ModuleInfo(self, selection):
        ModuleInt = int(selection[1])
        try:
            SelectedModule = self.Dmodules[ModuleInt]
            Task = SelectedModule.TemplateModule()
            self.TitleScreen()
            print Helpers.color("\n Template Information:\n", status=True)
            for item in self.TemplateInfo:
                task = "Task." + str(item.rstrip(":"))
                if task == "Task.Sophistication":
                    print "\t" + item + "\t\t" + eval(task)
                else:
                    print "\t" + item + "\t\t\t" + eval(task)
        except Exception as e:
            p = " [!] Please select a valid Module number\n"
            print Helpers.color(p, firewall=True)
            return

    def TaskSelector(self):
        # This will be the main controller of the framework
        # and handle user selection
        self.TitleScreen()
        self.MainMenu()
        self.PromptSelection()

    def TitleScreen(self):
        os.system('clear')
        # stolen from Veil :)
        p = "[Twitter]"
        w = "[Web]"
        print " ============================================================"
        print " Current: " + self.version + " | SimplyTemplate | " + Helpers.color(w, status=True) + ": CyberSyndicates.com"
        print " ============================================================"
        print "   " + Helpers.color(p, status=True) + ": @real_slacker007 | " + Helpers.color(p, status=True) + ": @Killswitch_gui"
        print " ============================================================"
