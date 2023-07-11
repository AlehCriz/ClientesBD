from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://Acceso_Base_restaurante:restaurante123@proyecto.uurcvmo.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client['restaurante']
    except ConnectionError:
        print("Error de conexión")
    return db