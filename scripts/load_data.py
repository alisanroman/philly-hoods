import json
import psycopg2

conn = psycopg2.connect('dbname=philly_hoods user=vagrant')

cur = conn.cursor()

f = open('../data/geo-data/Neighborhoods_Philadelphia/Neighborhoods_Philadelphia.geojson').read()

hoods = json.loads(f)

for hood in hoods['features']:
	alias = hood['properties']['name']
	name = hood['properties']['mapname']
	geometry = json.dumps(hood['geometry'])
	cur.execute(
		"""	INSERT INTO hoods (name, alias, dataset, geom)
			VALUES (%s, %s, %s, ST_GeomFromGeoJSON(%s));""",
		(name, alias, 'azavea', geometry))
	conn.commit()
	print name + ' added to the table!'
cur.close()
conn.close()