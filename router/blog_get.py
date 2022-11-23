from fastapi import APIRouter
from enum import Enum
from typing import Optional, Dict
from .blog_post import required_functionality
from fastapi import Response, status, Depends

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


class BlogType(str, Enum):
    howto = 'howto'


@router.get(
    '/all',
    summary='Retrieve all blogs',
    description='This api call simulates fetching all blogs',
    response_description='The list of available blogs'
    )
def get_all_blogs(page=11, page_size: Optional[int] = 123,
                  req_parameter: Dict = Depends(required_functionality)):
    return {'message': f'All {page_size} blogs on page {page}',
            'req': req_parameter
            }


@router.get('/{id}')
def get_blog(id: int, response: Response):
    """
    Simulate retrieving a comment of a blog
    - **id** mandatory path parameter
    """
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'message': f'Page {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': 'Every things goes well '}


@router.get('/type/{type}')
def get_blog_type(type: BlogType):
    return {'message': f'Blog type {type}'}