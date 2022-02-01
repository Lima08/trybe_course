'''
nome da abstração = orders
atributos/estados= 
  total_value
  product_name
  itens
  
  finish_order
  remove_item
  add_item
'''


class orders:
    def __init__(self, total_value=0):
        self.total_value = total_value
        self.itens = []

    def add_item(self, item):
        self.itens.append(item)
        # print(f'{item['name']} foi adicionado!')

    def remove_item(self, id):
        self.itens.remove(id)


