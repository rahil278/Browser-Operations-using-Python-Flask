from flask import Flask,request,render_template
import webbrowser
import os
import sqlite3
app = Flask(_name_)
webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))

@app.route('/')
def hello_world():
   return 'Hello World!!'

@app.route('/start')
def start():
   browser = request.args.get('browser')
   url = request.args.get('url')
   xyz = webbrowser.get(browser).open_new(url)
   if xyz:
      return "Opening the url:"+url
   else:
      return "Something went wrong"

@app.route('/stop')
def stop():
   browser = request.args.get('browser')
   if os.system(f"taskkill /im {browser}.exe /f".format(browser=browser)):
      return "Task Successful"
   else:
      return "Something went wrong"

@app.route('/cleanup')
def cleanup():
   browser = request.args.get('browser')
   if(browser=='chrome'):
      con = sqlite3.connect('C:/Users/rahil.shah/AppData/Local/Google/Chrome/User Data/Default/History')
      c = con.cursor()
      c.execute("select url from urls")  # Change this to your prefered query
      results = c.fetchall()
      # c.execute("SELECT sql FROM sqlite_master WHERE name = 'urls';")
      # print(c.fetchall())
      # return render_template("current_tabs.html",data=results)
   elif(browser=='firefox'):
      con = sqlite3.connect('C:/Users/rahil.shah/AppData/Roaming/Mozilla/Firefox/Profiles/nc4ky4w3.default-release/places.sqlite')
      c = con.cursor()
      c.execute("Delete from moz_places")  # Change this to your prefered query
      c.execute("Delete from moz_historyvisits")
      c.execute("Delete from moz_inputhistory")
      con.commit()
      # results = c.fetchall()
      # print(results)
      # return render_template("current_tabs.html", data=results)
      return "Success"

   # return 'here'

@app.route('/geturl')
def geturl():
   browser = request.args.get('browser')


if _name_ == '_main_':
   app.run()
