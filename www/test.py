import www.orm
import asyncio
from www.models import User, Blog, Comment
import sys

@asyncio.coroutine
def test(loop):
    yield from www.orm.create_pool(loop=loop, user='weibo', password='weibo', db='weibo')
    u = User(name='Test1', email='test1@example.com', passwd='1234567890', image='about:blank')
    yield from u.save()


loop = asyncio.get_event_loop();
loop.run_until_complete(test(loop))
loop.close()


#TODO: how to close connection, cursor, and loop event properly