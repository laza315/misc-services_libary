from fastapi import HTTPException

class BadInputParsed(HTTPException):
    """Input is valid as long as it receives alphabetic strings"""
    
    def __init__(self, detail: str = "Invalid input. Only alphabetic strings are allowed"):
        super().__init__(status_code=400, detail=detail)


class NoResultsException(HTTPException):
    """There were no results for searched criteria"""
    
    def __init__(self, detail: str = "No results. Your searching criteria have no associated nodes"):
        super().__init__(status_code=400, detail=detail)
