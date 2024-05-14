from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime
from typing import Optional


class License(BaseModel):
    key: str = Field(..., description="The unique identifier for the license.", alias="spdx_id")
    name: str = Field(..., description="The name of the license.")
    url: Optional[HttpUrl] = Field(..., description="The URL of the license.")


class Owner(BaseModel):
    username: str = Field(..., description="The username of the owner of the repository", alias="login")
    repos_url: HttpUrl = Field(..., description="The URL of the owner's repositories.")
    html_url: HttpUrl = Field(..., description="The URL of the owner's GitHub profile.")
    api_url: Optional[HttpUrl] = Field(..., description="The API URL of the owner's GitHub profile.", alias="url")


class RepoSchema(BaseModel):
    class Config:
        fields = {
            'username': 'owner.username'
        }
        
    id: int = Field(..., description="The unique identifier for the repository")
    clone_url: HttpUrl = Field(..., description="The URL used to clone the repository.")
    created_at: datetime = Field(..., description="The date and time when the repository was created.")
    description: Optional[str] = Field(..., description="The description of the repository.")
    forks_count: int = Field(..., description="The number of forks for the repository.")
    name: str = Field(..., description="The name of the repository.")
    full_name: str = Field(..., description="The full name of the repository.")
    license: Optional[License] = Field(..., description="The license information for the repository.")
    open_issues: int = Field(..., description="The number of open issues for the repository.")
    api_url: Optional[HttpUrl] = Field(..., description="The API URL of the repository", alias="url")
    html_url: HttpUrl = Field(..., description="The URL of the repository.")
    watchers: int = Field(..., description="The number of watchers for the repository.")
    updated_at: datetime = Field(..., description="The date and time when the repository was last updated.")
    owner: Owner = Field(..., description="The owner of the repository")
