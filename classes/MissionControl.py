from classes.Report import Report
class MissionControl:
    @staticmethod
    def aclearance_level(r:Report):
        if r.urgency_level >= 4:
            print("Immediate response required")
        elif r.urgency_level == 3:
            print("High priority. Monitor closely")
        else:
            print("Routine analysis")
