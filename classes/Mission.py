class Mission:
    def __init__(self ,mission_name :str, target_location:str ,assigned_agent):
        self.mission_name = mission_name
        self.target_location = target_location
        self.assigned_agent = assigned_agent
    def brief(self ):
        return f"Mission: {self.mission_name}, Target: {self.target_location}, Agent: {self.assigned_agent.code_name}"


