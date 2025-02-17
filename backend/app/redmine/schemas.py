from pydantic import BaseModel, Field
from datetime import datetime, date
from typing import List, Optional, Any

class RedmineCustomField(BaseModel):
    id: int
    name: str
    value: Optional[Any]

class RedmineIssue(BaseModel):
    id: int
    subject: str
    description: Optional[str]
    start_date: Optional[date]
    due_date: Optional[date]
    created_on : datetime
    updated_on: datetime
    custom_fields : List[RedmineCustomField] = []

    class Config:
        orm_mode = True

class RedmineIssueFilter(BaseModel):
    id: Optional[int]
    subject: Optional[str]
    start_date: Optional[date]
    due_date: Optional[date]
    status_id: Optional[int]
    project_id: Optional[int]  
    tracker_id: Optional[int]
    author_id: Optional[int]
    assigned_to_id: Optional[int]
    include_subprojects: Optional[bool] = True
    sort: Optional[str] = "created_on:desc"
    limit: Optional[int] = 100
    offset: Optional[int] = 0
    custom_fields: Optional[List[int]] = []
    
    class Config:
        orm_mode = True

class DeviceFromRedmine(BaseModel):
    redmine_issue_id: int  # Идентификатор issue из Redmine
    serial_number: str
    production_date: Optional[date]
    device_type: str
    execution: Optional[int] = None

    class Config:
        orm_mode = True

    @classmethod
    def from_redmine_issue(cls, issue: RedmineIssue):
        """
        Метод для создания объекта DeviceFromRedmine на основе данных RedmineIssue.
        Предполагается, что нужные значения передаются через custom_fields.
        """
        # Преобразуем список кастомных полей в словарь для удобного доступа
        custom_fields = {field.name: field.value for field in issue.custom_fields}
        
        return cls(
            redmine_issue_id=issue.id,
            serial_number=custom_fields.get("serial_number", ""),
            production_date=custom_fields.get("production_date"),
            device_type=custom_fields.get("device_type", "unknown"),
            execution=custom_fields.get("execution")
        )
