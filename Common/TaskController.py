import imp
import glob
import glob2
import configparser
import os
import sys
import warnings
import time
import subprocess
import re
import collections
from os.path import expanduser
from Helpers import TemplateEdit
from Helpers import CmdLoop
from Helpers import Helpers


class Conducter:

    def __init__(self):
        self.version = "v0.1"
        # Create dictionaries of supported modules
        # empty until stuff loaded into them
        # stolen from Veil :)
        # Create a ordered dict: or the state isnt postive
        self.Modules = collections.OrderedDict()
        self.Dmodules = collections.OrderedDict()
        self.LoadModules()
        self.Commands = [   ("use", "Select a template for use"),
                            ("list", "List loaded Templates"),
                            ("info", "Display meta data about a module"),
                            ("search", "Search by Core Options / Sophistication"),
                            ("update", "Update SimplyTemplate from Git-hub"),
                            ("help", "Display this menu"),
                            ("exit", "Exit SimplyTemplate")]
        self.TemplateInfo =[   ("Name:"),
                                ("Author"),
                                ("Type:"),
                                ("Sophistication:"),
                                ("SampleImage:"),
                                ("Info:")]
        self.TemplateCommands = [   ("set", "Set a option for the Template"),
                                    ("edit", "Edit a large chunk of template"),
                                    ("info", "Info about loaded Templates"),
                                    ("gen", "Generate Template"),
                                    ("view", "View Sample Template"),
                                    ("print", "Print to Console Sample Template"),
                                    ("render", "Render Html of Email"),
                                    ("back", "Go back to main Menu"),
                                    ("exit", "Exit SimplyTemplate")]
        
        # create required array
    
    def LoadModules(self):
        # loop and assign key and name
        warnings.filterwarnings('ignore', '.*Parent module*',)
        x = 1
        for name in glob2.glob('Modules/**/*.py'):
            if name.endswith(".py") and ("__init__" not in name):
                loaded_modules = imp.load_source(
                    name.replace("/", ".").rstrip('.py'), name)
                self.Modules[name] = loaded_modules
                self.Dmodules[x] = loaded_modules
                x += 1
        # print self.Dmodules
        # print self.Modules

    def ListModules(self):
        self.TitleScreen()
        print Helpers.color("\n  [*] Available Modules are:\t\t\t\t Core Options:\t\t\tSophistication:", blue=True)
        print "  -------------------------\t\t\t\t -------------\t\t\t---------------"

        lastBase = None
        x = 1
        for name in self.Modules:
            parts = name.split("/")
            if lastBase and parts[0] != lastBase:
                print ""
            lastBase = parts[0]
            SelectedModule = self.Modules[name]
            Task = SelectedModule.TemplateModule()
            if x < 10:
                print "  %s)   %s" % (str(x).ljust(1), '{0: <24}'.format(name).ljust(50)) + Task.CoreOptions.ljust(32) + "[" + Task.Sophistication + "]"
            if x >= 10:
                print "  %s)  %s" % (str(x).ljust(1), '{0: <24}'.format(name).ljust(50)) + Task.CoreOptions.ljust(32) + "[" + Task.Sophistication + "]"
            x += 1
        print ""

    def MainMenu(self):
        print " Main Selection Menu\n"
        print "\t"+str(len(self.Modules))+" Email Templates Loaded\n"
        print " Commands:\n"
        for item in self.Commands:
            if item[0] == "search":
                # print "\t[" + item[0] + "]\t" + item[1]
                print "\t[{0}]\t{1}".format(item[0],item[1])
            elif item[0] == "update":
                # print "\t[" + item[0] + "]\t" + item[1]
                print "\t[{0}]\t{1}".format(item[0],item[1])
            else:
                # print "\t[" + item[0] + "]\t\t" + item[1]
                print "\t[{0}]\t\t{1}".format(item[0],item[1])

    def ModuleSearch(self, SearchTerm):
        '''
        Takes in a array of strings and searched by them
        '''
        SophisticationList = []
        CoreOptionsList = []
        NameList = [] 
        # check for less than 2x items
        if len(SearchTerm) <= 1:
            # make sure they are using the correct items to search
            p = " [!] Please search by one of the options (sophistication)-(options)-(name) HINT-use tab"
            print Helpers.color(p, firewall=True)
            return
        # check for no search value
        if len(SearchTerm) <= 2:
            # make sure they are using the correct items to search
            p = " [!] Please use a search term!"
            print Helpers.color(p, firewall=True)
            return
        # search SophisticationList
        if SearchTerm[1] in 'sophistication':
            try:
                for name in self.Modules:
                    try:
                        SelectedModule = self.Modules[name]
                        Task = SelectedModule.TemplateModule()
                        Sophistication = Task.Sophistication
                        if SearchTerm[2].lower() in Sophistication.lower():
                            # add in the matching Result
                            SophisticationList.append(str(name))
                    except:
                        pass
            except Exception as e:
                print e
        if SearchTerm[1] in 'options':
            try:
                for name in self.Modules:
                    try:
                        SelectedModule = self.Modules[name]
                        Task = SelectedModule.TemplateModule()
                        CoreOptions = Task.CoreOptions
                        if SearchTerm[2] in CoreOptions.lower():
                            # add in the matching Result
                            CoreOptionsList.append(str(name))
                    except:
                        pass
            except Exception as e:
                print e
        if SearchTerm[1] in 'name':
            try:
                for name in self.Modules:
                    try:
                        if SearchTerm[2].lower() in name.lower():
                            # add in the matching Result
                            NameList.append(str(name))
                    except:
                        pass
            except Exception as e:
                print e

        self.ListSearchModules(CoreOptionsList, SophisticationList, NameList)

    def ListSearchModules(self, ModuleList, ModuleList2, ModuleList3):
        '''
        Takes an array of Modules to print rather than all modules.
        '''
        self.TitleScreen()
        if ModuleList:
            print Helpers.color("\n  [*] Core Options Search Results are:\t\t\tCore Options:\t\tSophistication:", blue=True)
            print "      --------------------------------\t\t\t-------------\t\t---------------"
            x = 1
            for name in ModuleList:
                SelectedModule = self.Modules[name]
                Task = SelectedModule.TemplateModule()
                print "\n  %s" % (Helpers.color('{0: <24}'.format(name).ljust(50), status=True)) + Helpers.color(Task.CoreOptions.ljust(33), status=True) + "[" + Helpers.color(Task.Sophistication, status=True) + "]\n"
                print Helpers.FormatLong("Module Info:",Task.Info, spacing=16)
                x += 1
            print ""
        if ModuleList2:
            print Helpers.color("\n  [*] Sophistication Search Results are:\t\tCore Options:\t\tSophistication:", blue=True)
            print "     ----------------------------------\t\t\t-------------\t\t---------------"
            x = 1
            for name in ModuleList2:
                SelectedModule = self.Modules[name]
                Task = SelectedModule.TemplateModule()
                print "\n  %s" % (Helpers.color('{0: <24}'.format(name).ljust(50), status=True)) + Helpers.color(Task.CoreOptions.ljust(33), status=True) + "[" + Helpers.color(Task.Sophistication, status=True) + "]\n"
                print Helpers.FormatLong("Module Info:",Task.Info, spacing=16)
                x += 1
            print ""
        if ModuleList3:
            print Helpers.color("\n  [*] Name Search Results are:\t\tCore Options:\t\tSophistication:", blue=True)
            print "     ----------------------------------\t\t\t-------------\t\t---------------"
            x = 1
            for name in ModuleList3:
                SelectedModule = self.Modules[name]
                Task = SelectedModule.TemplateModule()
                print "\n  %s" % (Helpers.color('{0: <24}'.format(name).ljust(50), status=True)) + Helpers.color(Task.CoreOptions.ljust(33), status=True) + "[" + Helpers.color(Task.Sophistication, status=True) + "]\n"
                print Helpers.FormatLong("Module Info:",Task.Info, spacing=16)
                x += 1
            print ""

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
                    if eval(task).lower() == "high":
                        print "\t{0}\t\t{1}".format(item, Helpers.color(eval(task), green=True))
                    if eval(task).lower() == "medium":
                        print "\t{0}\t\t{1}".format(item, Helpers.color(eval(task), firewall=True))
                    if eval(task).lower() == "low":
                        print "\t" + item + "\t\t" + Helpers.color(eval(task), warning=True)
                elif task == "Task.SampleImage":
                    print "\t" + item + "\t\t" + eval(task)
                elif task == "Task.Info":
                    print Helpers.FormatLong("Info:", Task.Info, spacing=24)
                else:
                    print "\t" + item + "\t\t\t" + eval(task)
            # https://github.com/Veil-Framework/Veil-Evasion/blob/master/modules/common/controller.py
            # Taken from line 246
            print Helpers.color("\n Template Required Options:\n", status=True)
            print " Setting\t\tValue Set\t\t\tDescription of Setting"
            print " -------\t\t---------\t\t\t----------------------"
            for key in sorted(Task.RequiredOptions.iterkeys()):
                # print " %s\t%s\t\t%s" % ('{0: <16}'.format(key), '{0: <8}'.format(Task.RequiredOptions[key][0]), Task.RequiredOptions[key][1])
                print " %s%s%s" % ('{0: <16}'.format(key).ljust(23), '{0: <8}'.format(Task.RequiredOptions[key][0]).ljust(32), Task.RequiredOptions[key][1])
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
                    if eval(task).lower() == "high":
                        print "\t" + item + "\t\t" + Helpers.color(eval(task), green=True)
                    if eval(task).lower() == "medium":
                        print "\t" + item + "\t\t" + Helpers.color(eval(task), firewall=True)
                    if eval(task).lower() == "low":
                        print "\t" + item + "\t\t" + Helpers.color(eval(task), warning=True)
                elif task == "Task.SampleImage":
                    print "\t" + item + "\t\t" + eval(task)
                elif task == "Task.Info":
                    print Helpers.FormatLong("Info:",Task.Info, spacing=24)
                else:
                    print "\t" + item + "\t\t\t" + eval(task)
            # https://github.com/Veil-Framework/Veil-Evasion/blob/master/modules/common/controller.py
            # Taken from line 246
            print Helpers.color("\n Template Required Options:\n", status=True)
            print " Setting\t\tValue Set\t\t\tDescription of Setting"
            print " -------\t\t---------\t\t\t----------------------"
            for key in sorted(Task.RequiredOptions.iterkeys()):
                print " %s%s%s" % ('{0: <16}'.format(key).ljust(23), '{0: <8}'.format(Task.RequiredOptions[key][0]).ljust(32), Task.RequiredOptions[key][1])
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
                print " %s%s%s" % ('{0: <16}'.format(key).ljust(10), '{0: <8}'.format(Task.RequiredOptions[key][0]).ljust(30), Task.RequiredOptions[key][1])
        except Exception as e:
            print e
            p = " [!] Please select a valid Module number\n"
            print Helpers.color(p, firewall=True)
            return

    def ModuleHelp(self):
            print "\tAvailable Commands:"
            print "\t-----------------------------------------"
            for item in self.Commands:
                if item[0] == "update":
                    print "\t[" + item[0] + "]\t" + item[1]
                else:
                    print "\t[" + item[0] + "]\t\t" + item[1]
            print "\n\tAvailable Template Commands:"
            print "\t-----------------------------------------"
            for item in self.TemplateCommands:
                print "\t[" + item[0] + "]\t\t" + item[1]
            return

    def ModuleCommands(self):
        print Helpers.color("\n Available Template Commands:\n", status=True)
        print "\tCommand\t\tDescription"
        print "\t-------\t\t-----------"
        for item in self.TemplateCommands:
            print "\t%s%s" % ('{0: <16}'.format("["+item[0]+"]").ljust(5), '{0: <16}'.format(item[1]))

    def TemplateView(self, Task):
        FileName = Task.SampleImage
        try:
            subprocess.check_call(["xdg-open", FileName])
        except Exception as e:
            s = "status 4"
            if s in str(e):
                print Helpers.color(" [!] Sorry no image submitted yet!")
            else:
                print Helpers.color(" [!] Is a default image viewer installed?")

    def TemplateSet(self, Task, Value, Raw):     
        try:
            option = Value[1]
            if Value[1] not in Task.RequiredOptions:
                print Helpers.color(" [!] Invalid option specified.", firewall=True)  

            else:
                Raw = Raw.strip(Value[0])
                Raw = Raw.lstrip(' ')
                Raw = Raw.lstrip(Value[1])
                Raw = Raw.lstrip(' ')
                Task.RequiredOptions[option][0] = Raw
                return
        except Exception as e:
            print e
            print Helpers.color(" [!] Error in setting option, likely invalid option name.", firewall=True)

    def TemplateEdit(self, Task, Value, Raw):
        try:
            try:
                if Task.RequiredText:
                    EditValue = True
            except:
                EditValue = False
                print Helpers.color(" [!] Template does not support edit yet!")
            if EditValue:
                if Value[1] not in Task.RequiredText:
                    print Helpers.color(" [!] Invalid option specified.", firewall=True)
                else:
                     Text = Task.RequiredText[Value[1]][0]
                     raw = TemplateEdit.root(Text)
                     if raw:
                        Task.RequiredText[Value[1]][0] = raw
                     return
                # raw = TemplateEdit.root(str(self.RequiredText["TextBlock1"][0]))
        except Exception as e:
            print e

    def TemplateLocation(self):
        '''
        This function will return the location output
        This will default to the ~/Desktop/ folder
        '''
        while True:
            try:
                p = " [>] Output Location (Default ~/Desktop/):"
                a = raw_input(Helpers.color(p,status=True))
                if a:
                    return a
                else:
                    home = expanduser("~")
                    a = str(home) + "/Desktop/"
                    return a
            except Exception as e:
                print e

    def TemplateName(self, Task):
        '''
        This function will return the location output
        This will default to the ~/Desktop/ folder
        '''
        while True:
            try:
                name = Task.OutputName
                p = " [>] Output Name (Default: " + name + "):"
                a = raw_input(Helpers.color(p,status=True))
                if a:
                    return a
                else:
                    a = name
                    return a
            except Exception as e:
                print e

    def TemplatePrint(self, Task):
        '''
        This function will print 
        to the console the output of the email.
        '''
        try:
            EmailRender = Task.Render()
            RenderName = Task.RenderName
            with open(RenderName, "w+") as myfile:
                myfile.write(EmailRender)
            try:
                # time.sleep(0)
                temp = "\n"
                temp += subprocess.check_output(["w3m", "-dump", "-T", "text/html", RenderName])
                print Helpers.Reindent(temp, 1)
                #time.sleep(5)
            except Exception as e:
                print Helpers.color(" [!] Is w3m installed (run Setup.sh)?")
                print e
            # now remove temp file
            # time.sleep(2)
            os.remove(RenderName)
        except Exception as e:
            print e

    def TemplateRender(self, Task):
        '''
        This function will return the location output
        This will default to the ~/Desktop/ folder
        '''
        try:
            EmailRender = Task.Render()
            # print EmailRender
            RenderName = Task.RenderName
            with open(RenderName, "w+") as myfile:
                myfile.write(EmailRender)
            try:
                # time.sleep(0)
                if ".eml" in RenderName:
                    subprocess.check_call(["icedove", RenderName])
                else:
                    temp = subprocess.check_call(["iceweasel", RenderName])
                #time.sleep(5)
            except Exception as e:
                print Helpers.color(" [!] Is a default browser installed?")
            # now remove temp file
            # time.sleep(2)
            os.remove(RenderName)
        except Exception as e:
            print e

    def TemplateFinalRender(self, FilePath, FileName, Task):
        '''
        This function will open the 
        Produced .MHT file
        '''
        try:
            # print EmailRender
            Path = str(FilePath) + str(FileName)
            try:
                time.sleep(1)
                if ".eml" in Path:
                    subprocess.check_call(["icedove", "-File", Path])
                else:
                    subprocess.check_call(["iceweasel", Path])
                #time.sleep(5)
            except Exception as e:
                print Helpers.color(" [!] Is a Iceweasel browser installed? (Run Setup)")
        except Exception as e:
            print e

    def TemplateRequiredOptions(self, Task):
        '''
        Function for required option for "only" a template.
        '''
        try:
            # https://github.com/Veil-Framework/Veil-Evasion/blob/master/modules/common/controller.py
            # Taken from line 246
            print Helpers.color("\n Template Required Options:\n", status=True)
            print " Setting\t\tValue Set\t\t\tDescription of Setting"
            print " -------\t\t---------\t\t\t----------------------"
            for key in sorted(Task.RequiredOptions.iterkeys()):
                print " %s%s%s" % ('{0: <16}'.format(key).ljust(23), '{0: <8}'.format(Task.RequiredOptions[key][0]).ljust(32), Task.RequiredOptions[key][1])
            try:
                if Task.RequiredText:
                    print Helpers.color("\n Template TextEdit Options:\n", status=True)  
                    print " Setting\t\tValue Set\t\t\tDescription of Setting"
                    print " -------\t\t---------\t\t\t----------------------"
                    for key in sorted(Task.RequiredText.iterkeys()):
                        print " %s%s%s" % ('{0: <16}'.format(key).ljust(23), '{0: <8}'.format(Task.RequiredText[key][0].replace("\n", "")[0:25] + str('..')).ljust(32), Task.RequiredText[key][1])
            except Exception as e:
                pass
        except Exception as e:
            print e
            p = " [!] Please select a valid Module number\n"
            print Helpers.color(p, firewall=True)
            return

    def TemplateGen(self, Task, ModuleInt):
        '''
        This Function takes in the template Task Object
        It will run the pre-defined Class Call
        '''
        try:
            FileLocation = self.TemplateLocation()
            Name = self.TemplateName(Task)
            Task.Generate(FileLocation, Name, Verbose=False)
            self.TemplateCompleteScreen(Task, FileLocation, Name, ModuleInt)
        except Exception as e:
            p = " [!] Major issue with template gen: " + str(e)
            print Helpers.color(p, warning=True)

    def TemplateCompleteScreen(self, Task, FileLocation, FileName, ModuleInt):
        '''
        Function takes in output data and presents it to user.
        '''
        self.TitleScreen()
        p = " [*] Email Template Generation has been completed:\n"
        line = """{0}
           Task Performed:\t\t{1}
           File Location: \t\t{2}
           Email File:\t\t\t{3}
        """.format(Helpers.color(p, green=True), Task.Name, FileLocation, FileName)
        print line 
        # Now check if they want to open the file
        p = Helpers.color(" [>] ", status=True) + "Would you like to view the generated template? (y) or (n): "
        while True:
            a = raw_input(p)
            if a.lower() == "y":
                self.TemplateFinalRender(FileLocation, FileName, Task)
                break
            if a.lower() == "n":
                break
        p = Helpers.color(" [>] ", status=True) + "Would you like to return to Current Module? (y) or (n): "
        while True:
            a = raw_input(p)
            if a.lower() == "y":
                self.TemplateMenu(Task, ModuleInt)
                break
            if a.lower() == "n":
                self.TaskSelector()
        print line 

    ######################################
    #                                    #
    #  Main Command Loop setup           #
    #                                    #
    ######################################

    def MainCmdLoopCommands(self):
        '''
        Takes in Task/Module grabs the 
        required options and builds a 
        tab complete list for the
        command loop.
        '''
        try:
            cmddict = {}
            modulelist = []
            # add in set commands
            # for key in self.Modules:
            #   modulelist.append(str(key))
            # cmddict['use']= modulelist
            cmddict['use'] = ""
            # add list command
            cmddict['list'] = ""
            # add info command 
            cmddict['info'] = ""
            # add search command 
            search = ['sophistication', 'options', 'name']
            cmddict['search'] = search
            # add update command
            cmddict['update'] = ""
            # add help command
            cmddict['help'] = ""
            # add exit command 
            cmddict['exit'] = ""
            return cmddict
        except Exception as e:
            p = ""
            print e

    def PromptSelection(self):
        # setup module commands and required lists 
        cmddict = self.MainCmdLoopCommands()
        # now call cmd loop
        CmdLoop.start_loop(cmddict)
        # We also have to strip off and verfiy the number
        # make sure we strip when checking command
        # p = " [>] "
        # a = raw_input(Helpers.color(p,status=True))
        a = CmdLoop.input_loop()
        # Gives me a list of words of ints
        try:
            Split = Helpers.GetWords(a)
            if Split[0].lower() == "use" or Split[0].lower() == "u":
                # we will use this to select our module of choice
                # it will call a separate function to handle the Int
                # of the requested module

                Task = self.ModuleSelection(Split)
                self.TemplateMenu(Task, Split)
            if Split[0].lower() == "info" or Split[0].lower() == "i":
                self.ModuleInfo(Split)
        except Exception as e:
            pass
        if a.lower() == "help" or a.lower() == "h" or a.lower() == "?":
            self.ModuleHelp()
        try:
            if Split[0].lower() == "search" or Split[0].lower() == "s":
                self.ModuleSearch(Split)
        except Exception as e:
            pass
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

    ######################################
    #                                    #
    # Template Command Loop setup        #
    #                                    #
    ######################################

    def TemplateCmdLoopCommands(self, Task):
        '''
        Takes in Task/Module grabs the
        required options and builds a
        tab complete set list for the
        command loop.
        '''
        try:
            cmddict = {}
            setlist = []
            editlist = []
            # add in set commands
            for key in sorted(Task.RequiredOptions.iterkeys()):
                setlist.append(key)
            cmddict['set']= setlist
            # add in edit command
            try:
                for key in sorted(Task.RequiredText.iterkeys()):
                    editlist.append(key)
                cmddict['edit']= editlist
            except:
                # edit is not a required command
                pass
            # add info command
            cmddict['info'] = ""
            # add gen command
            cmddict['gen'] = ""
            # add view command
            cmddict['view'] = ""
            # add print command
            cmddict['print'] = ""
            # add render command
            cmddict['render'] = ""
            # add back command
            cmddict['back'] = ""
            # add exit command
            cmddict['exit'] = ""
            return cmddict
        except Exception as e:
            p = ""
            print e

    def TemplateMenu(self, Task, ModuleInt):

        # start with Template menu and printing out the modules
        self.TitleScreen()
        p = "\n Template Loaded: " + Helpers.color(Task.Name, status=True)
        print p + "\n\n"
        self.TemplateRequiredOptions(Task)
        self.ModuleCommands()
        # setup module commands and required lists
        cmddict = self.TemplateCmdLoopCommands(Task)
        # now call cmd loop
        CmdLoop.start_loop(cmddict)
        while True:
            try:
                a = CmdLoop.input_loop()
                # a = raw_input(Helpers.color(p,status=True))
                if a.startswith("set") or a.startswith("s"):
                    try:
                        Split = Helpers.GetWords(a)
                        if Split[0].lower() == "set" or Split[0].lower() == "s":
                            self.TemplateSet(Task, Split, a)
                    except Exception as e:
                        print e
                        print Helpers.color(" [!] You must use [set] with Value", firewall=True)
                if a.startswith("edit") or a.startswith("e"):
                    try:
                        Split = Helpers.GetWords(a)
                        if Split[0].lower() == "edit" or Split[0].lower() == "e":
                            self.TemplateEdit(Task, Split, a)
                    except Exception as e:
                        print Helpers.color(" [!] You must use [edit] with Value", firewall=True)
                if a.lower() == "gen" or a.lower() == "g" or a.lower() == "run":
                    self.TemplateGen(Task, ModuleInt)
                if a.lower() == "info" or a.lower() == "i":
                    self.Template_Info(Task)
                if a.lower() == "view" or a.lower() == "v":
                    self.TemplateView(Task)
                if a.lower() == "print" or a.lower() == "p":
                    self.TemplatePrint(Task)
                if a.lower() == "render" or a.lower() == "r":
                    self.TemplateRender(Task)
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
        print "   " + Helpers.color(p, status=True) + ": @CyberSyndicates  | " + Helpers.color(p, status=True) + ": @Killswitch_gui"
        print " ============================================================"
