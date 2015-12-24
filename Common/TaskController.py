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
                                ("SampleImage:"),
                                ("Info:")]
        self.TemplateCommands = [   ("set","Set a option for the Template"),
                                    ("info","Info about loaded Templates"),
                                    ("gen","Generate Template"),
                                    ("view","View Sample Template"),
                                    ("back","Go back to main Menu"),
                                    ("exit","Exit SimplyTemplate")]
        
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

                Task = self.ModuleSelection(Split)
                self.TemplateMenu(Task, Split)
            if Split[0].lower() == "info" or Split[0].lower() == "i":
                self.ModuleInfo(Split)
        except Exception as e:
            print e 
            pass
        if a.lower() == "help" or a.lower() == "h" or a.lower() == "?":
            self.ModuleHelp()
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
            return Task
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
                elif task == "Task.SampleImage":
                    print "\t" + item + "\t\t" + eval(task)
                elif task == "Task.Info":
                    print Helpers.FormatLong("Info:",Task.Info, spacing=24)
                else:
                    print "\t" + item + "\t\t\t" + eval(task)
            # https://github.com/Veil-Framework/Veil-Evasion/blob/master/modules/common/controller.py
            # Taken from line 246
            print Helpers.color("\n Template Required Options:\n", status=True)
            print " Setting\t\tValue Set\t\tDescription of Setting"
            print " -------\t\t---------\t\t----------------------"
            for key in sorted(Task.RequiredOptions.iterkeys()):
                print " %s\t%s\t\t%s" % ('{0: <16}'.format(key), '{0: <8}'.format(Task.RequiredOptions[key][0]), Task.RequiredOptions[key][1])
        except Exception as e:
            print e
            p = " [!] Please select a valid Module number\n"
            print Helpers.color(p, firewall=True)
            return

    def Template_Info(self, Task):
        try:
            self.TitleScreen()
            print Helpers.color("\n Template Information:\n", status=True)
            for item in self.TemplateInfo:
                task = "Task." + str(item.rstrip(":"))
                if task == "Task.Sophistication":
                    print "\t" + item + "\t\t" + eval(task)
                elif task == "Task.SampleImage":
                    print "\t" + item + "\t\t" + eval(task)
                elif task == "Task.Info":
                    print Helpers.FormatLong("Info:",Task.Info, spacing=24)
                else:
                    print "\t" + item + "\t\t\t" + eval(task)
            # https://github.com/Veil-Framework/Veil-Evasion/blob/master/modules/common/controller.py
            # Taken from line 246
            print Helpers.color("\n Template Required Options:\n", status=True)
            print " Setting\t\tValue Set\t\tDescription of Setting"
            print " -------\t\t---------\t\t----------------------"
            for key in sorted(Task.RequiredOptions.iterkeys()):
                print " %s\t%s\t\t%s" % ('{0: <16}'.format(key), '{0: <8}'.format(Task.RequiredOptions[key][0]), Task.RequiredOptions[key][1])
        except Exception as e:
            print e
            p = " [!] Please select a valid Module number\n"
            print Helpers.color(p, firewall=True)
            return

    def ModuleRequiredOptions(self, selection):
        ModuleInt = int(selection[1])
        try:
            SelectedModule = self.Dmodules[ModuleInt]
            Task = SelectedModule.TemplateModule()
            # https://github.com/Veil-Framework/Veil-Evasion/blob/master/modules/common/controller.py
            # Taken from line 246
            print Helpers.color("\n Template Required Options:\n", status=True)
            print " Setting\t\tValue Set\t\tDescription of Setting"
            print " -------\t\t---------\t\t----------------------"
            for key in sorted(Task.RequiredOptions.iterkeys()):
                print " %s\t%s\t\t%s" % ('{0: <16}'.format(key), '{0: <8}'.format(Task.RequiredOptions[key][0]), Task.RequiredOptions[key][1])
        except Exception as e:
            print e
            p = " [!] Please select a valid Module number\n"
            print Helpers.color(p, firewall=True)
            return

    def ModuleHelp(self):
            print "\tAvailiable Commands:"
            print "\t-----------------------------------------"
            for item in self.Commands:
                if item[0] == "update":
                    print "\t[" + item[0] + "]\t" + item[1]
                else:
                    print "\t[" + item[0] + "]\t\t" + item[1]
            print "\n\tAvailiable Template Commands:"
            print "\t-----------------------------------------"
            for item in self.TemplateCommands:
                print "\t[" + item[0] + "]\t\t" + item[1]
            return

    def ModuleCommands(self):
        print Helpers.color("\n Availiable Template Commands:\n", status=True)
        print "\tCommand\t\tDescription"
        print "\t-------\t\t-----------"
        for item in self.TemplateCommands:
            print "\t[" + item[0] + "]\t\t" + item[1]

    def TemplateView(self, Task):
        FileName = Task.SampleImage
        try:
            subprocess.check_call(["xdg-open", FileName])
        except Exception as e:
            print Helpers.color(" [!] Is a default image viewer installed?")

    def TemplateSet(self, Task, Value, Raw):     
        try:
            option = Value[1]
            if Value[1] not in Task.RequiredOptions:
                print Helpers.color(" [!] Invalid option specified.", firewall=True)   

            else:
                Raw = Raw.strip(Value[0])
                Raw = Raw.lstrip(' ')
                Raw = Raw.strip(Value[1])
                Raw = Raw.lstrip(' ')
                Task.RequiredOptions[option][0] = Raw
                return
        except Exception as e:
            print e
            print Helpers.color(" [!] Error in setting option, likely invalid option name.", firewall=True)

    def TemplateGen(self, Task):
        '''
        This Function takes in the template Task Object
        It will run the pre-defined Class Call
        '''
        Task.Generate(Verbose=False)


    def TemplateMenu(self, Task, ModuleInt):
        # start with Template menu and printing out the modules
        self.TitleScreen()
        p = "\n Template Loaded: " + Helpers.color(Task.Name, status=True)
        print p + "\n\n"
        self.ModuleRequiredOptions(ModuleInt)
        self.ModuleCommands()
        while True:
            try:
                p = " [>] "
                a = raw_input(Helpers.color(p,status=True))
                if a.startswith("set") or a.startswith("s"):
                    try:
                        Split = Helpers.GetWords(a)
                        if Split[0].lower() == "set" or Split[0].lower() == "s":
                            self.TemplateSet(Task, Split, a)
                    except Exception as e:
                        print e
                        print Helpers.color(" [!] You must use [set] with Value", firewall=True)
                if a.lower() == "gen" or a.lower() == "g" or a.lower() == "run":
                    self.TemplateGen(Task)
                if a.lower() == "info" or a.lower() == "i":
                    print "here"
                    self.Template_Info(Task)
                if a.lower() == "view" or a.lower() == "v":
                    self.TemplateView(Task)
                if a.lower() == "back" or a.lower() == "b":
                    self.TaskSelector()
                if a.lower() == "help" or a.lower() == "h" or a.lower() == "?":
                    self.ModuleHelp()
                if a.lower() == "exit":
                    Helpers.Exit()
            except Exception as e:
                print a

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
