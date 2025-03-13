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
    cluster_id: str = Field(default="")
# The identifier of the schedule (in Guid format).
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
    schedule_id: str = Field(default="")
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

# The actual backups in this list
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
# The identifier of the cluster (in Guid format).
# This is a required field.
    cluster_id: str = Field(default="")
# The identifier of the backup (in Guid format).
# This is a required field.
    backup_id: str = Field(default="")

class RestoreBackupResponse(BaseModel):#  Empty
    """
     RestoreBackupResponse is the response from the RestoreBackup function.
    """
