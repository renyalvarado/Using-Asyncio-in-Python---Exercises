import sanic

# https://sanicframework.org/en/guide/getting-started.html#install

app = sanic.Sanic("My Hello World")


@app.get("/")
async def helloworld(request):
    return sanic.response.text("Hello World!")
