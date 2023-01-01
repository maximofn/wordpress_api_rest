import requests
from datetime import date, datetime, timedelta
import time

def timedate(hours_delta = 5, time_delta = 0):
    today = date.today()
    now = datetime.now() - timedelta(hours=hours_delta)
    if now.hour + hours_delta > 23:
        today = today - timedelta(days=1)
    page_date = f'{today}T{now.hour:02d}:{now.minute:02d}:{now.second:02d}'
    time.sleep(time_delta)
    now = datetime.now()
    page_date_modified = f'{today}T{now.hour:02d}:{now.minute:02d}:{now.second:02d}'
    time.sleep(time_delta)
    now = datetime.now()
    page_date_modified_gmt = f'{today}T{now.hour:02d}:{now.minute:02d}:{now.second:02d}'
    return {
      'page_date': page_date, 
      'page_date_modified': page_date_modified, 
      'page_date_modified_gmt': page_date_modified_gmt
    }

def compare_dicts(dict1, dict2):
  # Obtener la lista de claves que están en el primer diccionario pero no en el segundo
  keys_only_in_dict1 = set(dict1.keys()) - set(dict2.keys())
  # Imprimir las claves y valores que solo están en el primer diccionario
  if len(keys_only_in_dict1) > 0:
    print("Claves y valores solo en el primer diccionario:")
    for key in keys_only_in_dict1:
      print(f"{key}: {dict1[key]}")
  # Obtener la lista de claves que están en el segundo diccionario pero no en el primero
  keys_only_in_dict2 = set(dict2.keys()) - set(dict1.keys())
  # Imprimir las claves y valores que solo están en el segundo diccionario
  if len(keys_only_in_dict2) > 0:
    print("Claves y valores solo en el segundo diccionario:")
    for key in keys_only_in_dict2:
      print(f"{key}: {dict2[key]}")
  # Obtener la lista de claves que están en ambos diccionarios
  common_keys = set(dict1.keys()) & set(dict2.keys())
  # Imprimir las claves y valores que están en ambos diccionarios, pero con valores diferentes
  if len(common_keys) > 0:
    print("Claves en ambos diccionarios, con valores diferentes:")
    for key in common_keys:
      if dict1[key] != dict2[key]:
        print(f"{key}: {dict1[key]} (dict1), {dict2[key]} (dict2)")

