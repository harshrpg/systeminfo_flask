from flask import render_template
from app import app
import sysinfo

@app.route('/')
def index():
    returnDict = {}
    returnDict['user'] = sysinfo.get_platform_info()
    returnDict['title'] = 'System Info'
    return render_template("index.html",**returnDict)