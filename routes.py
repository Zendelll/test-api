from handlers.pills import get_info
from handlers.pills import set_pills
from handlers.pills import add_pills
from handlers.pills import pills_count
from handlers.pills import pills_safe_count

def setup_routes(app):
    app.router.add_get('/pills/get_me', get_info)
    app.router.add_get('/pills/pills_count', pills_count)
    app.router.add_get('/pills/pills_safe_count', pills_safe_count)
    app.router.add_post('/pills/add_pills', add_pills)
    app.router.add_post('/pills/set_pill', set_pills)
    