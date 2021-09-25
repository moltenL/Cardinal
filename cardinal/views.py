from django.http import HttpResponse


def index(_):
    page = """<div>
    <h1>Cardinal 🐦</h1>
    <h4>Source: <a href=https://github.com/jakeroggenbuck/Cardinal>Github</a></h4>
    </div>"""
    return HttpResponse(page)
