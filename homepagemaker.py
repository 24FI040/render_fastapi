from fastapi.responses import HTMLResponse

def get_homepage():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
            <h2>kadaimuzui</h2>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)