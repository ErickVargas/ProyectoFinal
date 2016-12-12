import web
# @
db = web.database(dbn='mysql', db='coches', user='root', pw='1234')
#result = db.select('contactos')
#for row in result:
   # print row
#db.insert('contactos',nombre='aldo', telefono=12345, email='al@hot')

#db.update('contactos',where='id_contacto=3',email='ric@hot')

#db.delete('contactos',where='id_contacto=6')
user=raw_input("ingrese su usuario\n")
passw=raw_input("ingrese la contrasena\n")
result=db.select("usuarios")
dbuser=""
dbPass=""
for row in result:
    dbuser=row.nombre
    dbPass=row.passw

if dbuser==user and dbPass==passw:
    print "ya la hiciste"
else:
    print "ya valio "
