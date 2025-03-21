import sys
from bottle import error, route, request, run, static_file

### Default settings ###
@error(404)
def go_default(error):
     return {"info": 'notmyproblem .!.'}

### Real sh1t ###
@route('/')
def landing():
     print("i'm world |m|," flush=True)
     print(f'addr: {request.remote_addr} and route: {request.remote_route} in bottle :D', flush=True)
     return static_file('index.html', root='.')

if __name__ == '__main__':
     if len(sys.argv) != 3: raise Exception('EXPLODE')
     print(f'Running in {sys.argv[1]} mode on port {sys.argv[2]}...')
     if sys.argv[1] == 'dev':
          run(host='0.0.0.0', port=int(sys.argv[2]), debug=True, reloader=True)
     if sys.argv[1] == 'FTW':
          run(host='0.0.0.0', port=int(sys.argv[2]))

#ned
