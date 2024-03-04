from fastapi import FastAPI, HTTPException, Query
from tortoise.models import Model
from tortoise import fields

class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)  

class Post(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    content = fields.TextField()
    author = fields.ForeignKeyField('models.User', related_name='posts')
    category = fields.CharField(max_length=50)
