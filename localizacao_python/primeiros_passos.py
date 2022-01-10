from pygeocoder import Geocoder

endereco = 'avenida paulista, 100 São Paulo, SP'

resultado = Geocoder('AIzaSyDUAD9AHsTT9WePFfnCl7DNV0yvHaG_T_A').geocode(endereco).coordinates
print(resultado)

