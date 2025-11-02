from classes.Agent import Agent
from classes.MissionControl import MissionControl
from classes.Report import Report
yosef = Agent("y" ,4)
r = Report("8200" ,4 ,yosef)
MissionControl.aclearance_level(r)
print(Agent.log_transmission(yosef.code_name , Agent.encrypt_message("there is boom")))