import hashlib
import requests 
import json
import sqlite3



def main_api():
    public = '6a3b626e6bbf32dda50a097d1534ab50'
    private = 'f09beff6e9f14778215b131ca6b637e79d2cf9ff'
    ts = '1'
    hash = hashlib.md5((ts + private + public).encode()) .hexdigest()

    base='https://gateway.marvel.com:443/v1/public/'
    caracter=requests.get(base + 'characters',params={'apikey':public,'ts':ts,'hash':hash,'name':'Cyclops'}) .json()
     
    nombre = (caracter ['data'] ['results'] [0] ['name'])
    descripcion = (caracter['data'] ['results'] [0] ['description'])
    con = sqlite3.connect("C:/Users/Jean Roodny Ostema/Desktop/MARVEL/db")
    cursor = con.cursor()
    cursor.execute(''' CREATE TABLE IF NOT EXISTS MARVEL
                       (NOMBRE         TEXT NOT NULL,
                       DESCRIPCION TEXT NOT NULL)''')

    cursor.execute(''' INSERT INTO MARVEL (NOMBRE , DESCRIPCION) VALUES (?,?)''', (nombre, descripcion))
    con.commit()
    cursor.execute('''  SELECT * FROM MARVEL''')
    print (cursor.fetchall())
    con.close()
   
if __name__ == '__main__' :
        main_api() 




