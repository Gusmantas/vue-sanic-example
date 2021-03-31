from sanic import Sanic, response as res

app = Sanic(__name__)

@app.get('/rest/cars')
async def get_cars(req):
  from database import getCars
  return res.json(await getCars())


@app.post('/rest/cars')
async def post_car(req):
  from database import createCar

  car = req.json
  car['id'] = await createCar(car)
  return res.json(car)


@app.delete('/rest/cars/<car_id:int>')
async def delete_car_by_id(req, car_id):
  from database import deleteCarById

  await deleteCarById(car_id)
  return res.text('OK')


if __name__ == "__main__":
  app.run(port=8000)