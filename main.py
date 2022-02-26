
from typing import List, Optional
from fastapi import FastAPI, Query, status
from pydantic import BaseModel, Field
import motor.motor_asyncio
from bson import ObjectId
from fastapi.responses import JSONResponse

    
    
app = FastAPI()
MONGODB_URL = "mongodb+srv://admin:admin@cluster0.jv4sq.mongodb.net/test?retryWrites=true&w=majority"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
db = client.bus_db

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)
    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class BusStop(BaseModel):
    id: PyObjectId = Field(..., alias="_id")
    name: str
    geo_code: List[str]
    
class Bus(BaseModel):
    _id: PyObjectId = Field(..., alias="_id")
    bus_type: str
    geo_code: List[float] 
    terminate_at: Optional[str] = None
  
        
@app.get("/")
def read_root():
    return {"Welcome to the bus app"}


@app.get("/bus_stops") 
async def read_bus_stops():
    bus_stops_list = []
    # async for bus_stop in db.bus_stop.find():
    #     bus_stops.append(bus_stop)
    bus_stops = db.bus_stop.find()
    for i in await bus_stops.to_list(40):
        temp = i
        print(temp)
        bus_stops_list.append({'name:':temp['name'], 'geocode':temp['geocode'], 'bus_types': temp['bus_types']})
    return bus_stops_list

@app.get("/drivers")
async def read_drivers():
    driver_list = []
    # async for bus_stop in db.bus_stop.find():
    #     bus_stops.append(bus_stop)
    drivers = db.driver.find()
    for i in await drivers.to_list(10):
        temp = i
        driver_list.append({'geocode':temp['geocode'],'terminate_at': temp['terminate_at'], 'bus_type': temp['bus_type']})
    return driver_list

@app.post("/register_bus")
async def register_bus(bus_type: str, geo_code: Optional[List[float]] = Query(...)):
    bus = Bus(bus_type = bus_type, geo_code=geo_code)
    bus_added = await db.bus.insert_one(bus.dict())
    bus_id = bus_added.inserted_id
    return {'bus_id': str(bus_id)}

@app.put("/update_geocode")
async def update_geocode(bus_id: str, geocode: Optional[List[float]] = Query(...)):
    try:
        bus_added = await db.bus.find_one_and_update(
            {'_id': ObjectId(bus_id)},
            { '$set': {'geocode': geocode}}
        )
        if str(bus_added['_id']) == bus_id:
            return {'msg': 'Update successful!'}
        else:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, 
                            content = {'msg': 'Update unsuccessful'})
    except Exception as e:
        print(e)
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, 
                            content = {'msg': 'Unexpected Error. Try again!'})
@app.delete("/delete_bus")
async def delete_bus(bus_id):
    result = await db.bus.delete_one({'_id': ObjectId(bus_id)})
    if result.deleted_count>0:
        return {'msg':'Delete successful'}
    else:
        return JSONResponse(status_code=status.HTTP_409_CONFLICT,
                            content = {'msg':'Delete unsuccessful'}
                            )

@app.get("/driver/{driver_pin}")
async def authenticate_driver(driver_pin):
    try:
        driver_list = []
        driver = db.driver.find({'pin':str(driver_pin)})
        print(driver)
        for i in await driver.to_list(1):
            temp = i 
            driver_list.append({
                'geo_code': temp['geo_code'],
                'terminate_at': temp['terminate_at'],
                'bus_type': temp['bus_type']
            })
        return driver_list[0]
    except:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, 
                            content = {
                                'Error': "Invalid PIN. Try again!"
                                }
                            )
        
@app.get("/businfo")
async def get_bus_info():
    bus_list = []
    # async for bus_stop in db.bus_stop.find():
    #     bus_stops.append(bus_stop)
    buses = db.bus.find()
    for i in await buses.to_list(10):
        temp = i
        bus_list.append({
            'bus_type:':temp['bus_type'], 
            'geocode':temp['geocode'],
            'terminate_at':temp['terminate_at']
        })
    return bus_list
