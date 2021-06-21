import psycopg2
conn = psycopg2.connect(database="postgres",user="dboper"
                        ,password="abcd@123",host="123.60.69.255"
                        ,post="26000")
cursor = conn.cursor()

data=[]

type2pic = {}

type2pic['2']['type'] = "commic"
type2pic['1']['type'] = "game"
type2pic['']['type'] = "commic"
type2pic['2']['type'] = "commic"
type2pic['2']['type'] = "commic"