import datetime
import re

class TimeObject:

    def __init__(self, start, end, name, descripton : str = None,
                 milestone : str = None, section : str = None):
        self.start = start
        self.end = end
        self.name = name
        self.descripton = descripton
        self.milestone = milestone
        self.section = section

    def __transform_date(self,orgdate):
        if isinstance( orgdate, datetime.date ):
            return orgdate
        elif isinstance( orgdate, datetime.datetime ):
            return datetime.date( orgdate.year, orgdate.month, orgdate.day)
        elif isinstance( orgdate, int ):
            return datetime.date.fromtimestamp( orgdate )
        elif isinstance( orgdate, str ):
            if re.fullmatch( r'\d{4}-[01]\d-[0-3]\d', orgdate ) or \
               re.fullmatch( r'\d{4}[01]\d[0-3]\d', orgdate ) or \
               re.fullmatch( r'\d{4}[01]-W[0-5]\d-\d', orgdate ):
               return datetime.time.fromisoformat( orgdate )
        elif isinstance( orgdate, tuple ) and len(orgdate) == 3:
            resCheck = True
            for ii in orgdate:
                if not isinstance( ii, int ):
                    resCheck = False
                    break
            if resCheck:
                return date.fromisocalendar( *orgdate )
        return None






class Timeline:

    def __init__(self):
        pass
