# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.0.3](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.29.3 
# Pydantic Version: 2.10.6 
from datetime import datetime
from datetime import timedelta
from google.protobuf.message import Message  # type: ignore
from protobuf_to_pydantic.util import Timedelta
from pydantic import BaseModel
from pydantic import BeforeValidator
from pydantic import Field
from typing_extensions import Annotated
import typing


class ListBackupsRequest(BaseModel):
    """
     ListBackupsRequest is the request for the ListBackups function
    """

# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# The identifier of the cluster (in Guid format).
# When this field is set, only backups that belong to the cluster are returned.
    cluster_id: typing.Optional[str] = Field(default="")
# The identifier of the schedule (in Guid format).
# When this field is set, only backups triggered by the backup schedule are returned.
    schedule_id: typing.Optional[str] = Field(default="")# TODO: ListOptions

class Backup(BaseModel):
    """
     A Backup represents a backup of a Qdrant database.
    """

# Unique identifier for the backup (in Guid format).
# This is a read-only field and will be available after a backup is created.
    id: str = Field(default="")
# The timestamp when the backup was created.
# This is a read-only field and will be available after a backup is created.
    created_at: datetime = Field(default_factory=datetime.now)
# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# The identifier of the cluster (in Guid format).
# This is a required field.
    cluster_id: str = Field(default="")
# The name of the backup.
# This is a read-only field and will be available after a backup is created.
    name: str = Field(default="")
# The identifier of the schedule that triggered the creation of the backup.
# If there isn't value, that means the backup was created manually.
# This is a read-only field and will be available after a backup is created.
# TODO we don't have this field at this moment (we used to store only `short_id`).
# Once we have it, we can enable it here.
# string schedule_id = 6;
# The current status of the backup.
# This is a read-only field and will be set after CreateBackup is called.
    status: str = Field(default="")
# The timestamp when the backup was deleted (or when deletion started).
# This is a read-only field and will be set after DeleteBackup is called.
    deleted_at: datetime = Field(default_factory=datetime.now)
# The total time taken to create the backup.
# This is a read-only field and will be available after a backup is created.
    creation_duration: Annotated[timedelta, BeforeValidator(Timedelta.validate)] = Field(default_factory=timedelta)

class ListBackupsResponse(BaseModel):
    """
     ListBackupsResponse is the response from the ListBackups function
    """

# The actual backups in this list.
    items: typing.List[Backup] = Field(default_factory=list)# TODO: Add an operation timestamp the ListBackups is started, to support the `since` in ListOptions

class CreateBackupRequest(BaseModel):
    """
     CreateBackupRequest is the request for the CreateBackup function.
    """

# The actual backup.
    backup: Backup = Field()

class CreateBackupResponse(BaseModel):
    """
     CreateBackupResponse is the response from the CreateBackup function.
    """

# The actual backup.
    backup: Backup = Field()

class DeleteBackupRequest(BaseModel):
    """
     DeleteBackupRequest is the request for the DeleteBackup function.
    """

# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# The identifier of the backup (in Guid format).
# This is a required field.
    backup_id: str = Field(default="")

class DeleteBackupResponse(BaseModel):#  Empty
    """
     DeleteBackupResponse is the response from the DeleteBackup function.
    """

class RestoreBackupRequest(BaseModel):
    """
     RestoreBackupRequest is the request for the RestoreBackup function.
    """

# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# The identifier of the backup (in Guid format).
# This is a required field.
    backup_id: str = Field(default="")

class RestoreBackupResponse(BaseModel):#  Empty
    """
     RestoreBackupResponse is the response from the RestoreBackup function.
    """

class ListBackupSchedulesRequest(BaseModel):
    """
     ListBackupSchedulesRequest is the request for the ListBackupSchedules function
    """

# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# The identifier of the cluster (in Guid format).
# When this field is set, only backup schedules that belong to the cluster are returned.
    cluster_id: typing.Optional[str] = Field(default="")# TODO: ListOptions

class BackupSchedule(BaseModel):
    """
     A BackupSchedule represents a recurring schedule for creating backups.
    """

# Unique identifier for the backup schedule (in Guid format).
# This is a read-only field and will be available after a backup schedule is created.
    id: str = Field(default="")
# The timestamp when the backup schedule was created.
# This is a read-only field and will be available after a backup schedule is created.
    created_at: datetime = Field(default_factory=datetime.now)
# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# The identifier of the cluster (in Guid format).
# This is a required field.
    cluster_id: str = Field(default="")
# The schedule that determines when the backup will be created.
# This field follows the standard crontab format: https://en.wikipedia.org/wiki/Cron#Overview
# This is a required field.
    schedule: str = Field(default="")
# The duration after the backups generated by this backup schedule will be automatically deleted after the specified retention period.
# If this value is unset, backups will be retained indefinitely.
    retention_period: Annotated[timedelta, BeforeValidator(Timedelta.validate)] = Field(default_factory=timedelta)
# The timestamp when the backup schedule was deleted (or when deletion started).
# This is a read-only field and will be set after DeleteBackupSchedule is called.
    deleted_at: datetime = Field(default_factory=datetime.now)
# The current status of the backup schedule.
# This is a read-only field and will be set after CreateBackupSchedule is called.
# The possible values are:
# - Active: The backup schedule is active and functioning correctly.
# - FailedToSync: There was an error syncing the backup schedule in the cluster's region.
# - NotFound: The backup schedule isn't present in the cluster's region.
# - Unknown: The system didn't receive status information about the backup schedule from the cluster's region.
    status: str = Field(default="")

class ListBackupSchedulesResponse(BaseModel):
    """
     ListBackupsResponse is the response from the ListBackups function.
    """

# The actual backup schedules in this list.
    items: typing.List[BackupSchedule] = Field(default_factory=list)# TODO: Add an operation timestamp the ListBackups is started, to support the `since` in ListOptions

class GetBackupScheduleRequest(BaseModel):
    """
     GetBackupScheduleRequest is the request for the GetBackupSchedule function.
    """

# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# The identifier for the cluster (in Guid format).
# This cluster should be part of the provided account.
# This is a required field.
    cluster_id: str = Field(default="")
# The identifier for the backup schedule (in Guid format).
# This backup schedule should be part of the provided cluster and account.
# This is a required field.
    backup_schedule_id: str = Field(default="")

class GetBackupScheduleResponse(BaseModel):
    """
     GetBackupScheduleResponse is the response from the GetBackupSchedule function.
    """

# The actual cluster
    backup_schedule: BackupSchedule = Field()

class CreateBackupScheduleRequest(BaseModel):
    """
     CreateBackupScheduleRequest is the request for the CreateBackupSchedule function.
    """

# The actual backup schedule.
    backup_schedule: BackupSchedule = Field()

class CreateBackupScheduleResponse(BaseModel):
    """
     CreateBackupScheduleResponse is the response from the CreateBackupSchedule function.
    """

# The actual backup schedule.
    backup_schedule: BackupSchedule = Field()

class UpdateBackupScheduleRequest(BaseModel):
    """
     UpdateBackupScheduleRequest is the request for the UpdateBackupSchedule function.
    """

# The actual backup schedule.
    backup_schedule: BackupSchedule = Field()

class UpdateBackupScheduleResponse(BaseModel):
    """
     UpdateBackupScheduleResponse is the response from the UpdateBackupSchedule function.
    """

# The actual backup schedule.
    cluster: BackupSchedule = Field()

class DeleteBackupScheduleRequest(BaseModel):
    """
     DeleteBackupScheduleRequest is the request for the DeleteBackupSchedule function
    """

# The identifier of the account (in Guid format).
# This is a required field.
    account_id: str = Field(default="")
# The identifier for the backup schedule (in Guid format).
# This backup schedule should be part of the provided account.
# This is a required field.
    backup_schedule_id: str = Field(default="")
# If set, the backups generated by this backup schedule will be deleted as well.
    delete_backups: typing.Optional[bool] = Field(default=False)

class DeleteBackupScheduleResponse(BaseModel):#  Empty
    """
     DeleteBackupScheduleResponse is the response from the DeleteBackupSchedule function.
    """
