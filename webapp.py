import web
# @
from web import form
db = web.database(dbn='mysql', db='coches', user='root', pw='1234')
render=web.template.render('templates')
urls = (
    '/', 'login'
    ,'/index','index',
    '/nuevo', 'nuevo',
    '/editar/(.+)','editar',
    '/ver/(.+)','ver',
    '/eliminar/(.+)','eliminar'
)

myformLogin = form.Form( 
    form.Textbox("usuario"), 
    form.Password("contrasena")
    )

myformAutos=form.Form(
    form.Textbox("Marca"), 
    form.Textbox("SubMarca"),
    form.Textbox("Modelo"), 
    form.Textarea("Descripcion"),
    form.Textbox("Imagen")
)
class login:
    def GET(self):
        form = myformLogin()
        
        return render.login(form)
    
    def POST(self): 
        form = myformLogin()
        if not form.validates(): 
            return render.login(form)
        else: 
            result=db.select("usuarios")
            dbuser=""
            dbPass=""
            for row in result:
                dbuser=row.nombre
                dbPass=row.passw

            if dbuser==form.d.usuario and dbPass==form.d.contrasena:
                raise web.seeother("/index")
            else:
                return render.loginerror(form)

            # form.d.boe and form['boe'].value are equivalent ways of
            # extracting the validated arguments from the form.

class index:
    def GET(self):
        
        result=db.select('autos')
        return render.index(result)
    def POST(self):           
        raise web.seeother("/nuevo")    
class nuevo:
    def GET(self):
        formNew=myformAutos()
        return render.nuevo(formNew)
    def POST(self): 
        formNew = myformAutos()
        if not formNew.validates(): 
            return render.nuevo(formNew)
        else:
            db.insert('autos', Marca=formNew.d.Marca,SubMarca=formNew.d.SubMarca,Modelo=formNew.d.Modelo,Descripcion=formNew.d.Descripcion,Imagen=formNew.d.Imagen)
            raise web.seeother('/index')
            
class editar:
    def GET(self,id_auto):
        formEdit=myformAutos()
        
        result=db.select('autos', where= "id_auto=%s"%(id_auto))
        
        for row in result:
            formEdit['Marca'].value=row.Marca
            formEdit['SubMarca'].value=row.SubMarca
            formEdit['Modelo'].value=row.Modelo
            formEdit['Descripcion'].value=row.Descripcion
            formEdit['Imagen'].value=row.Imagen
        return render.editar(formEdit)        
    def POST(self,id_auto):
        formEdit=myformAutos()
        if not formEdit.validates(): 
            return render.editar(formEdit)
        else:
            db.update('autos', where="id_auto=%s"%(id_auto), Marca=formEdit.d.Marca,
            SubMarca=formEdit.d.SubMarca,Modelo=formEdit.d.Modelo,Descripcion=formEdit.d.Descripcion,Imagen=formEdit.d.Imagen )
            
            raise web.seeother('/index')
class eliminar:
    def GET(self,id_auto):
        formEdit=myformAutos()
        
        result=db.select('autos', where= "id_auto=%s"%(id_auto))
        
        for row in result:
            formEdit['Marca'].value=row.Marca
            formEdit['SubMarca'].value=row.SubMarca
            formEdit['Modelo'].value=row.Modelo
            formEdit['Descripcion'].value=row.Descripcion
            formEdit['Imagen'].value=row.Imagen
        return render.eliminar(formEdit)        
    def POST(self,id_auto):
        formEdit=myformAutos()
        if not formEdit.validates(): 
            return render.eliminar(formEdit)
        else:
            db.delete('autos', where="id_auto=%s"%(id_auto))
            raise web.seeother('/index')
class ver:
    def GET(self,id_auto):
        
        result=db.select('autos', where="id_auto=%s"%(id_auto)) 
        return render.ver(result)

if __name__ == "__main__":
    
    app = web.application(urls, globals())
    app.run()