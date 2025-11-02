class Agent:
    def __init__(self ,code_name:str ,clearance_level:int):
        self.code_name = code_name
        self.clearance_level = clearance_level

    def __str__(self):
        return f"Agent {self.code_name} reporting. Clearance Level: {self.clearance_level}"