# SimplyTemplate

Phishing Template Generation Made Easy. The goal of this project was to hopefully speed up Phishing 
Template Gen as well as an easy way to ensure accuracy of your templates. Currently my standard Method
of delivering emails is the Spear Phish in Cobalt strike so you will see proper settings for that by default. 


Current Platforms Supported:
* Kali Linux 2.0
* Kali Linux 1.0

Work Conducted by:
----------------------------------------------
* Alexander Rymdeko-Harvey [Twitter] @Killswitch-GUI -- [Web] [CyberSydicates.com](http://cybersyndicates.com)
* Keelyn Roberts [Twitter] @real_slacker007 -- [Web] [CyberSydicates.com](http://cybersyndicates.com)

A few small benefits:
- Easy for you to write modules (All you need is 1 required Class option and you're up and running)
- Simple intergration of Email Templates
- Also the ability to change major settings fast without diving into the code (Coming)

## Get Started
Please RUN the simple Setup Bash script!!!
```Bash
root@kali:~/Desktop/SimplyTemplate# sh Setup.sh
or
root@kali:~/Desktop/Simplytemplate# ./Setup.sh
```

## Standard Startup
```
 ============================================================
 Current: v0.1 | SimplyTemplate | [Web]: CyberSyndicates.com
 ============================================================
   [Twitter]: @real_slacker007 | [Twitter]: @Killswitch_gui
 ============================================================
 Main Selection Menu

  2 Email Template Loaded

 Commands:

  [use]   Select a template for use
  [list]    List loaded Templates
  [info]    Display metadata about a module
  [update]  Update SimplyTemplate from Github
  [help]    Display this menu
  [exit]    Exit SimplyTemplate
 [>] 
```
## List Modules
```
 ============================================================
 Current: v0.1 | SimplyTemplate | [Web]: CyberSyndicates.com
 ============================================================
   [Twitter]: @real_slacker007 | [Twitter]: @Killswitch_gui
 ============================================================
 [*] Available Modules are:

  1)  Modules/CyberNews.py    
  2)  Modules/LinkedinGroup.py

 [>] list
```
## Display help Commands
```
 [>] help
  Availiable Commands:
  -----------------------------------------
  [use]   Select a template for use
  [list]    List loaded Templates
  [info]    Display metadata about a module
  [update]  Update SimplyTemplate from Github
  [help]    Display this menu
  [exit]    Exit SimplyTemplate

  Availiable Template Commands:
  -----------------------------------------
  [set]   Set a option for the Template
  [info]    Info about loaded Templates
  [gen]   Generate Template
  [view]    View Sample Template
  [back]    Go back to main Menu
  [exit]    Exit SimplyTemplate
 [>] 
```
## Use a module
```
 [>] use 2

 ============================================================
 Current: v0.1 | SimplyTemplate | [Web]: CyberSyndicates.com
 ============================================================
   [Twitter]: @real_slacker007 | [Twitter]: @Killswitch_gui
 ============================================================

 Template Loaded: Linkedin Group Invite



 Template Required Options:

 Setting    Value Set   Description of Setting
 -------    ---------   ----------------------
 FromFirstName    Jim         Contacts First Name
 FromFullName     Jim Bob     Contacts Full Name
 FromOrg          Veris Group, LLC    Contacts Company
 FromProfileUrl   http://k.com    Linkedin Full Profile URL
 FromTitle        CEO, ATD    Contacts Full Title
 GroupName        Cyber Cyber Cyber   Requested Group to Join
 GroupUrl         %URL%       Custom GroupURL or CS URL
 ProfilePic       http://pic.com    Custom GroupURL or CS URL

 Availiable Template Commands:

  Command   Description
  -------   -----------
  [set]   Set a option for the Template
  [info]    Info about loaded Templates
  [gen]   Generate Template
  [view]    View Sample Template
  [back]    Go back to main Menu
  [exit]    Exit SimplyTemplate
 [>]
 ```