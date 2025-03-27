import os
import json
import argparse
import requests
from enum import Enum
from typing import Union, List, Dict, Optional
from openapi_pydantic import parse_obj, OpenAPI, PathItem, Response

parser = argparse.ArgumentParser()

parser.add_argument("--from_url", type=str, default="http://127.0.0.1:8000/openapi.json")
parser.add_argument("--from_file", type=str, default=None)
parser.add_argument("--save_path", type=str, default="openapi.md")

args = parser.parse_args()


class HtmlTag(Enum):

    H1 = "h1"
    H2 = "h2"
    H3 = "h3"
    H4 = "h4"
    H5 = "h5"
    H6 = "h6"
    A = "a"


class HtmlObject:

    def __init__(self, content: str, tag: HtmlTag, id: Optional[str] = None):
        self.content = content
        self.tag = tag
        self.id = id

    def export(self) -> str:
        if self.id:
            return f"<{self.tag.value} id={self.id}>{self.content}</{self.tag.value}> \n"
        else:
            return f"<{self.tag.value}>{self.content}</{self.tag.value}> \n"


class MarkdownObject:

    def export(self) -> str:
        pass


class Header(MarkdownObject):

    def __init__(self, title: str, level: int):
        self.title = title
        self.level = level

    def export(self):
        return "#" * self.level + " " + self.title + "\n\n"


class Content(MarkdownObject):

    def __init__(self, content: str,
                 bold: bool = False,
                 italic: bool = False,
                 underline: bool = False,
                 link: Optional[str] = None,
                 end: str = "",
                 indent: int = 0,
                 blockquote_level: int = 0,
                 order: Optional[int] = None,
                 unordered: bool = False):
        self.content = content
        self.bold = bold
        self.italic = italic
        self.underline = underline
        self.link = link
        self.end = end
        self.indent = indent
        self.blockquote_level = blockquote_level
        self.order = order
        self.unordered = unordered

    def export(self):
        output = self.content
        if self.bold:
            output = f"**{output}**"
        if self.italic:
            output = f"*{output}*"
        if self.underline:
            output = f"__{output}__"
        if self.link:
            output = f"[{output}]({self.link})"
        blockquote = ">" * self.blockquote_level + " " if self.blockquote_level > 0 else ""
        content = blockquote + output + self.end
        if self.order is not None and self.unordered:
            raise ValueError("Cannot have both order and unordered set at the same time")
        if self.order is not None:
            content = f"{self.order}. " + content
        if self.unordered:
            content = "- " + content
        return " "*self.indent + content


class Code(MarkdownObject):

    def __init__(self, content: str, language: Optional[str] = None, block: bool = False, end: str = "\n\n"):
        self.content = content
        self.language = language
        self.block = block
        self.end = end

    def export(self):
        if self.block:
            return f"```{self.language}\n{self.content}\n```" + self.end
        return f"```{self.content}```" + self.end


class Table(MarkdownObject):

    def __init__(self, headers: List[str], rows: List[List[Union[any, Content]]]):
        self.headers = headers
        self.rows = rows
        super().__init__()

    def export(self):
        content = "|".join(self.headers) + "\n"
        content += "|".join(["---"] * len(self.headers)) + "\n"
        for row in self.rows:
            row_items = []
            for item in row:
                if isinstance(item, Content):
                    row_items.append(item.export())
                else:
                    row_items.append(str(item))
            content += "|".join(row_items) + "\n"
        return content


def save_md_doc(md_objs: List[Union[MarkdownObject, HtmlObject]], file_path: str):
    os.makedirs(os.path.dirname(os.path.realpath(file_path)), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        for obj in md_objs:
            f.write(obj.export())


def load_api(url_or_dict: Union[str, dict]) -> OpenAPI:
    if isinstance(url_or_dict, dict):
        return parse_obj(url_or_dict)
    else:
        response = requests.get(url_or_dict)
        return parse_obj(response.json())


class RequestFunc(Enum):

    GET = "get"
    POST = "post"
    PUT = "put"
    DELETE = "delete"


def get_request_func(path_item: PathItem) -> Optional[RequestFunc]:
    for func in RequestFunc:
        if getattr(path_item, func.value) is not None:
            return func
    return None


def create_md_summary(openapi: OpenAPI) -> List[MarkdownObject]:
    md_objs = []
    md_objs.append(Header("Summary", 1))
    md_objs.append(Content("Project Name:", end=" ", unordered=True))
    md_objs.append(Code(openapi.info.title, block=False, end="\n\n"))
    md_objs.append(Content("Version: ", end=" ", unordered=True))
    md_objs.append(Code(openapi.info.version, block=False, end="\n\n"))
    return md_objs
