from databases import Database

db = Database('sqlite:cars-db.db')

async def get(query, values={}):
    rows = await db.fetch_all(query=query, values=values)
    dicts = []
    for row in rows:
        dicts.append(dict(row))
    return dicts


async def run(query, values={}):
    return await db.execute(query=query, values=values)


async def getCars():
    return await get('SELECT * FROM cars')


async def deleteCarById(id):
    return await run('DELETE FROM cars WHERE id = :id', {"id": id})


async def createCar(car):
    query = 'INSERT INTO cars(brand, model, image) VALUES(:brand, :model, :image)'
    return await run(query, {
      "brand": car['brand'], 
      "model": car['model'], 
      "image": car['image']
    })
