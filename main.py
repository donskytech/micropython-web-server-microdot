from microdot_asyncio import Microdot, Response, send_file
from microdot_utemplate import render_template
from led_module import LEDModule

app = Microdot()
Response.default_content_type = 'text/html'

# Our LED Module
led_module = LEDModule(23)


@app.route('/')
async def index(request):
    return render_template('index.html', led_value=led_module.get_value())


@app.route('/toggle')
async def toggle_led(request):
    print("Receive Toggle Request!")
    led_module.toggle()
    return "OK"


@app.route('/shutdown')
async def shutdown(request):
    request.app.shutdown()
    return 'The server is shutting down...'


@app.route('/static/<path:path>')
def static(request, path):
    if '..' in path:
        # directory traversal is not allowed
        return 'Not found', 404
    return send_file('static/' + path)

app.run()