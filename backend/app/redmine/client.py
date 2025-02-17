from redminelib import Redmine

class RedmineClient:
    def __init__(self,api_key: str):
        self.redmine = Redmine('https://tasks.etecs.ru/', key=api_key)
    
    async def get_user_issue():
        ...