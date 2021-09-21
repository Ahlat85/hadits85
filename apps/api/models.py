import re

import requests
import pyarabic.araby as araby

class Hadits:
  def __init__(self):
    self.github = 'https://raw.githubusercontent.com/Ahlat85/data85/master/hadits'
    self.kitab = {
      'sutanlab': ['abu-daud', 'ahmad', 'bukhari', 'darimi', 'ibnu-majah', 'malik', 'muslim', 'nasai', 'tirmidzi']
    }
  
  def get_kitab(self): 
    return self.kitab
  
  def fetch(self, github=None, owner=None, kitab=None):
    result = {}
    if owner and kitab:
      if github:
        url = f'{github}/{owner}/{kitab}.json'
      else:
        url = f'{self.github}/{owner}/{kitab}.json'
      data = requests.get(url).json()
      result[owner] = {}
      result[owner][kitab] = data
    else:
      for key, value in self.kitab.items():
        result[key] = {}
        for kitab in value:
          if github:
            url = f'{github}/{key}/{kitab}.json'
          else:
            url = f'{self.github}/{key}/{kitab}.json'
          data = requests.get(url).json()
          result[key][kitab] = data
    return result

  def search(self, owner, kitab, id_hadits):
    id_hadits = int(id_hadits)
    result = requests.get(f'{self.github}/{owner}/{kitab}.json').json()
    for e in result:
      if e["number"] == id_hadits:
        data = {}
        data[owner] = {}
        data[owner][kitab] = [e]
        return data
    return None

  def search_q(self, owner=None, kitab=None, keyword=None):
    result = {}
 
    if (owner and kitab):
      data = self.fetch(owner=owner, kitab=kitab)
      result = data
    else:
      data = self.fetch()
      result = data
    
    if data and keyword:
      result = {}
      for owner in data:
        result[owner] = {}
        for kitab in data[owner]:
          result[owner][kitab] = []
          for element in data[owner][kitab]:
            if keyword.lower() in element['id'].lower() or araby.strip_diacritics(keyword) in araby.strip_diacritics(element['arab']):
              
              result_hadits = {}
              result_hadits['number'] = element['number']
              result_hadits['arab'] = re.sub(araby.strip_diacritics(keyword), self.hadits_contain_word, araby.strip_diacritics(element['arab']))
              result_hadits['id'] = re.sub(keyword, self.hadits_contain_word, element['id'], flags=re.IGNORECASE)
              
              result[owner][kitab].append(result_hadits)
          if len(result[owner][kitab]) == 0:
            del result[owner][kitab]
        if not result[owner]:
          del result[owner]
          
    if not result:
      result = None
    return result
  
  def hadits_contain_word(self, data):
    print(data)
    return f'<span class="text-info fw-bold fs-2">{data.group()}</span>'