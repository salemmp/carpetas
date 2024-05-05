import  os


x=['jose','pedro','jorge','salem','luci','gemini','google','alexis','daniel']






def user_(lista):
    id=0
    ya_existe=0
    creado=0
    for i in lista:
        user= i+'_'+str(id)
        if os.path.exists(user):
            ya_existe=ya_existe+1
            
            id=id+1
        else:
            os.mkdir(user)
            creado=creado+1
           
            id=id+1

    print('ese usuario ya existe  (' + str(ya_existe)+')')
    print('usuario creado  ('+ str(creado)+')')



user_(x)