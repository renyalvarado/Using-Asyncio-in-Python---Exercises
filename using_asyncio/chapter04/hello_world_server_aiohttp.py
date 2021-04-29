from aiohttp import web


async def hello(request):
    return web.Response(text="Hello World")


app = web.Application()
app.router.add_get("/", hello)
web.run_app(app, port=8080)
