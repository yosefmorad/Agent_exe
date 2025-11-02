class Agent:
    '''
    class create agent
    '''
    def __init__(self ,code_name:str ,clearance_level:int):
        self.code_name = code_name
        self.__clearance_level = clearance_level
    def __get__(self):
        return  self.__clearance_level

    def __set__(self ,value:int):
        if 1 < value > 5:
            print("value error")
        else:
            self.__clearance_level += value

    def __str__(self):
        return f"Agent {self.code_name} reporting. Clearance Level: {self.__get__()}"


    @staticmethod
    def encrypt_message(msg:str):
        return msg[:: -1]

    @staticmethod
    def log_transmission(agent_name: str, message: str) :
        return f"{agent_name} send encrypted message:{message}"
    

