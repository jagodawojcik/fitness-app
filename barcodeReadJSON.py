from urllib.request import urlopen
import json


barcode = '5901550002955'
# store the URL in url as 
# parameter for urlopen
url = "https://world.openfoodfacts.org/api/v0/product/5901550002955.json"
  
# store the response of URL
response = urlopen(url)
  
# storing the JSON response 
# from url in data
product = json.loads(response.read())

pr = product['product']
prn = product['product']['nutriments']


def printVal(key, parent):
    key in parent
    print(parent[key])

#OR
#try:
#       value = value[key]
#     except TypeError:
#       print("Remember Kiddo: Eval is Evil!")
#       break
#   else:  # for: else: triggers only if no break was issued
#     print item, value

print('Product name, quantitiy and serving size:')
printVal('product_name_pl',pr)
'quantity' in pr
print(pr['quantity'])
'serving_size' in pr
print('Serving: ')



# print('Allergens:', pr['allergens'])
# print('Origin Country: ', pr['countries'])
# print('Nutritients lvl for 100g: \n', 'kcal:', prn['energy-kcal_100g'])




#try:
 #     value = value[key]
  #  except TypeError:
   #   print

