from fastapi import APIRouter, HTTPException, Query
from models import Post
from schemas import PostIn

router = APIRouter()

@router.get("/posts")
async def get_posts(author: str = None, category: str = None):
    query = Post.all().prefetch_related('author')
    if category:
        query = query.filter(category=category)
    if author:
        query = query.filter(author__username=author)
    
    posts = await query.values('id', 'title', 'content','category', 'author__username')
    return posts


@router.post("/posts")
async def create_post(post_in: PostIn):
    post = await Post.create(
        title=post_in.title,
        cofntent=post_in.content,
        category= post_in.category,
        author_id=post_in.author_id,
        )
    return post