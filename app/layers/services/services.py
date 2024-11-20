# capa de servicio/lógica de negocio
from ..persistence import repositories
from ..utilities import translator
from django.contrib.auth import get_user

def getAllImages(input=None):
    # obtiene un listado de datos "crudos" desde la API, usando a transport.py.
    json_collection = getAllImages(input) #NO ME SIRVE QUE ESTE VACIA, TENGO QUE VER COMO LA COMPLETO.. TRAIGO LAS IMAGENES DESDE LA FUNCION DEFINIDA EN TRANSPORT
    # recorre cada dato crudo de la colección anterior, lo convierte en una Card y lo agrega a images.
    images = []

    for obj in json_collection:
        try:
            image_data = obj['image']  
            card = {
                'image': image_data,
                'name': obj.get('name', 'Sin nombre'),  
                'status': obj['status']
            }
            images.append(card)
        except KeyError:
            print("[services.py]: Error al procesar un objeto sin imagen.")
            continue
    return images

# añadir favoritos (usado desde el template 'home.html')
def saveFavourite(request):
    fav = '' # transformamos un request del template en una Card.
    fav.user = '' # le asignamos el usuario correspondiente.

    return repositories.saveFavourite(fav) # lo guardamos en la base.

# usados desde el template 'favourites.html'
def getAllFavourites(request):
    if not request.user.is_authenticated:
        return []
    else:
        user = get_user(request)

        favourite_list = [] # buscamos desde el repositories.py TODOS los favoritos del usuario (variable 'user').
        mapped_favourites = []

        for favourite in favourite_list:
            card = '' # transformamos cada favorito en una Card, y lo almacenamos en card.
            mapped_favourites.append(card)

        return mapped_favourites

def deleteFavourite(request):
    favId = request.POST.get('id')
    return repositories.deleteFavourite(favId) # borramos un favorito por su ID.