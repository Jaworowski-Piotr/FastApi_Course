from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel
from typing import Optional, List, Dict

from fastapi import Response, status

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


class Image(BaseModel):
    url: str
    alias: str


class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]
    tags: List[str] = []
    metadata: Dict[str, str] = {"key1": "val1"}
    image: Optional[Image] = None


@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        "id": id,
        "version": version,
        "data": blog
    }


@router.post('/new/{id}/comment')
def create_comment(
        blog: BlogModel, id: int,
        comment_title: int = Query(None,
                                   title='Title of a comment',
                                   description='Some description for comment',
                                   alias='commentTitle',
                                   deprecated=True),
        comment_id: int = Path(None, gt=5, le=10),
        content: str = Body(Ellipsis,
                            min_length=10,
                            max_length=100,
                            regex='^[a-z\s]*$'),
        v: Optional[List[str]] = Query(['1.0', '1.1', '1.2'])
):
    return {
        "blog": blog,
        "id": id,
        "comment_title": comment_title,
        "comment_id": comment_id,
        "content": content,
        "version": v
    }


def required_functionality():
    return {'message': "Learning FastAPI is important"}