def crear_familiares(request):
    familiar1 = Familiar(relacion='Madre', nombre='Sue', apellido='Storm', fechanacimiento='1961-01-01', segurosocial=12345678)
    familiar2 = Familiar(relacion='Padre', nombre='Reed', apellido='Richards', fechanacimiento='1966-08-19', segurosocial=23456789)
    familiar3 = Familiar(relacion='Tio', nombre='Johnny', apellido='Storm', fechanacimiento= '1975-05-12', segurosocial=56789012)
    familiar4 = Familiar(relacion='Hermana', nombre='Valeria', apellido='Richards', fechanacimiento= '19964-08-23', segurosocial=890123456)
    

    [familiar1.save](http://familiar1.save)()
    [familiar2.save](http://familiar2.save)()
    [familiar3.save](http://familiar3.save)()
    [familiar4.save](http://familiar4.save)()

    contexto = {
        'informacion': {
            'Madre': familiar1,
            'Padre': familiar2,
            'Tio': familiar3
            'Hermana': familiar4
        }
    }
    plantilla = loader.get_template('template001.html')
    documento_texto = plantilla.render(contexto)

    return HttpResponse(documento_texto)