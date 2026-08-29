from db_connection import DBConnection

db = DBConnection()
client = db.get_client()

try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)