from typing import TypedDict


class GuidDict(TypedDict):
    rendered: str  # uri


class TitleDict(TypedDict):
    rendered: str


class ContentDict(TypedDict):
    rendered: str
    protected: bool


class MaterialsDict(TypedDict):
    rendered: str
