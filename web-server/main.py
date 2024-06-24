import store 
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list(): 
    return [1,2,3]
    
@app.get('/contact', response_class = HTMLResponse)
def get_list():
    # return {'name': 'Platzi'}
    return """
    <h1>Título de una página</h1>
    <p>Párrafo</p>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()