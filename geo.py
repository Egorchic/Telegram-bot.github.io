from geopy import Nominatim
import datab

geolocator = Nominatim(user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36')

def get_region(lat, lon):
    cords = [lat, lon]
    loc = geolocator.reverse(cords)

    inf = loc.raw
    ad = inf['display_name']
    ad.replace(',', '')
    m = ad.split(',')

    for el in m:
        if 'район' in el:
            el = el.replace('район', '')
            return el.strip()

def get_cords(address):
    location = geolocator.geocode(address)
    latitude = location.latitude
    longitude = location.longitude

    return (latitude, longitude)

def distance(lng1, lat1, categ):
    res = []

    for el in datab.sql.execute('select * from restorans where category = ?', (categ,)):
        title = el[2]
        address = el[3]
        lat2 = el[6]
        lng2 = el[5]
        dist = ((lat1 - lat2)**2 + (lng1 - lng2)**2)**0.5
        dist *= 111
        res.append((title, address, dist))

    res = sorted(res, key = lambda x: x[2])

    return res


