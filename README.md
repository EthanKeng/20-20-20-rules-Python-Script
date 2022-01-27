This repo is forked from @rainnic and used to be a bunch of python scripts. I deleted all other scripts and only remain "eye_strain_reducer". Also, I modified some lines to let it run on Windows system (originally only Linux OS can run).  

# eye_strain_reducer 
## eye_strain_reducer (a little program to respect the 20-20-20 rule and prevent eye strain)  
So what is 20-20-20 rule? As [this website](https://advancedeyecaremd.net/20-20-20-tipstopreventeyestrain/#:~:text=Try%20your%20best%20to%20remember,when%20your%20eyes%20feel%20dry.&text=Blink%20often%20to%20help%20replenish%20your%20eye's%20own%20tears) said: 
>Basically, every 20 minutes spent using a screen; you should try to look away at something that is 20 feet away from you for a total of 20 seconds.

## why doing this?

As a modern human living in a full of digital devices world, we staring at PC/laptop with multiple monitors while working and swiping our smart phones even in the toilet. I always can't stop move my eyes from the monitor when I am too fucus on the topic/work and could last couple hours even without drink a cup of water. 

Recently, bad result comes, my eyes getting drier and drier each year, and keeping twitching for more than couple weeks. Worstly, headache! So it is super important to find a way to force ourselfs resting our eyes. Then I found there is a rule called 20-20-20 which I think it can be a start point for me. 

Luckly, I found this repo with simple python script could let us forcely rest our eyes! So I made some changes to adapt [Windows OS with Task Scheduler to auto turn it on](https://www.jcchouinard.com/python-automation-using-task-scheduler/) everytime we turn the power on. Hope this can release my eyes pain. 

> In some situation of Task Scheduler, neigher .bat file does not work properly nor directly run python.exe (don't know why). But Powershell (.ps1) works.

In short, simply type the power shell command (python <python "C:\Users\yc.keng\<yourPath>\eye_strain_reducer.py">) and save as .ps1 file. Finally follow [the guide of this page](https://blog.netwrix.com/2018/07/03/how-to-automate-powershell-scripts-with-task-scheduler/). (Don't forget to uncheck the only on AC power, I have been struggling this point because I did not in charge) 

More info on his site:
[Python on Rainnic](https://rainnic.altervista.org/tag/python)


## Change log

- 2022/01/26: Added info for "Use powershell to run python Script by Task Scheduler"
- 2022/01/26: Changed the way of control screen from pygame to screen-brightness-control. Because pygame.display.set_mode is not working when not focus on the terminal window (maybe belongs to Windows OS feature)

