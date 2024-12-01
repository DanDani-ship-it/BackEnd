from flask import Flask, render_template, request, redirect, url_for
import requests 
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def login():
    username = request.args.get('username', '')  
    password = request.args.get('password' '')  

    api = 'https://obpreprod.sidesoftcorp.com/comreivicpreprod/org.openbravo.service.json.jsonrest/MaterialMgmtStorageDetail?_startRow=0&_endRow=200'
    try:
        
        res =requests.get(api, auth=HTTPBasicAuth(username,password))
        res.raise_for_status()


        data = res.json()
        data = res.json()
        datafiltrada= []
        for i in data['response']['data']:
            datafiltrada.append({
                
                'idproducto': i.get('product'),
                'nombreproducto': i.get('product$_identifier'),
                'nombremedida': i.get('uOM$_identifier'),
                'cantidad': i.get('quantityOnHand')
            })

        return render_template('resultado.html', data=datafiltrada)
    except requests.exceptions.RequestException as e:
        return render_template('error.html', error=str(e))
    
if __name__ == '__main__':
    app.run(debug=True)

