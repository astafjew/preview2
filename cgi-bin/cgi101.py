import cgi
import html

form = cgi.FieldStorage()
print('Content-Type: text/html\n')
print('<Title>Reply Page</title>')
if 'user' not in form:
    print('<h1>Who are you?</h1>')
else:
    print('<h1>Hello %s!' % html.escape(form['user'].value))
