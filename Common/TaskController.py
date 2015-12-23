import imp
import glob
import configparser
import os
import sys
import warnings
import time
import subprocess
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
        print "\t[use]\t\tSelect a template for use"
        print "\t[list]\t\tList loaded Templates"
        print "\t[info]\t\tdisplay metadata about a module"
        print "\t[update]\tUpdate SimplyTemplate from Github"
        print "\t[help]\t\tDisplay this menu"
        print "\t[exit]\t\tExit SimplyTemplate\n"

    def PromptSelection(self):
        p = " [>] "
        a = raw_input(Helpers.color(p,status=True))
        if a.lower() == "help" or a.lower() == "h" or a.lower() == "?":
            print "\tAvailiable Commands:"
            print "\t-----------------------------------------"
            print "\t[use]\t\tSelect a template for use"
            print "\t[list]\t\tList loaded Templates"
            print "\t[info]\t\tdisplay metadata about a module"
            print "\t[update]\tUpdate SimplyTemplate from Github"
            print "\t[help]\t\tDisplay this menu"
            print "\t[exit]\t\tExit SimplyTemplate\n"
            self.PromptSelection()
        if a.lower() == "list" or a.lower() == "l":
            self.ListModules()
            self.PromptSelection()
        if a.lower() == "update" or a.lower() == "u":
            p = "[!] SimplyTemplate now Updating.."
            print Helpers.color(p,status=True)
        if a.lower() == "exit":
            Helpers.Exit()
        else:
            self.PromptSelection()
        return a

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
