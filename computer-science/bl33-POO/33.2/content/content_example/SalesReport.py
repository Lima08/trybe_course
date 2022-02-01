# V1 --------------------------------------------------------
# import json


# class SalesReport():
#     def __init__(self, export_file):
#         self.export_file = export_file + '.json'

#     def build(self):
#         """ Aqui colocamos a lógica para a entidade 'se criar',
#         ou seja, criar um relatório imprimível. Por simplicidade,
#         vamos omitir essa lógica nos exemplos! """
#         return [{
#                 'Coluna 1': 'Dado 1',
#                 'Coluna 2': 'Dado 2',
#                 'Coluna 3': 'Dado 3'
#                 },
#                 {
#                 'Coluna 1': 'Dado A',
#                 'Coluna 2': 'Dado B',
#                 'Coluna 3': 'Dado C'
#                 }]

#     def serialize(self):
#         # Vamos gerar, aqui, o nosso relatório em formato JSON
#         with open(self.export_file, 'w') as file:
#             json.dump(self.build(), file)


# # Classe, crie (em outras palavras, instancie!) uma nova entidade
# 'Relatório de vendas' para eu usar!

# meu_relatorio_de_vendas = SalesReport('meu_relatorio')

# # Entidade 'meu_relatorio_de_vendas', que eu acabei de criar, imprima-se!

# meu_relatorio_de_vendas.serialize()

# Fim V1 ---------------------------------------------------------------------

# V2 - Classe abstrata X classe especializada --------------------------------
# from abc import ABC, abstractmethod
# import json


# class SalesReport(ABC):
#     def __init__(self, export_file):
#         self.export_file = export_file

#     def build(self):
#         return [{
#                 'Coluna 1': 'Dado 1',
#                 'Coluna 2': 'Dado 2',
#                 'Coluna 3': 'Dado 3'
#                 },
#                 {
#                 'Coluna 1': 'Dado A',
#                 'Coluna 2': 'Dado B',
#                 'Coluna 3': 'Dado C'
#                 }]

#     @abstractmethod
#     def serialize(self):
#         raise NotImplementedError


# class SalesReportJSON(SalesReport):
#     def serialize(self):
#         with open(self.export_file + '.json', 'w') as file:
#             json.dump(self.build(), file)

# Fim V2 ---------------------------------------------------------------

# V3 - Compress --------------------------------------------------------
# from abc import ABC, abstractmethod
# import gzip
# import json


# class SalesReport(ABC):
#     def __init__(self, export_file):
#         self.export_file = export_file

#     def build(self):
#         return [{
#                 'Coluna 1': 'Dado 1',
#                 'Coluna 2': 'Dado 2',
#                 'Coluna 3': 'Dado 3'
#                 },
#                 {
#                 'Coluna 1': 'Dado A',
#                 'Coluna 2': 'Dado B',
#                 'Coluna 3': 'Dado C'
#                 }]

#     def compress(self):
#         binary_content = json.dumps(self.build()).encode('utf-8')

#         with gzip.open(self.export_file + '.gz', 'wb') as compressed_file:
#             compressed_file.write(binary_content)

#     @abstractmethod
#     def serialize(self):
#         raise NotImplementedError


# class SalesReportJSON(SalesReport):
#     def serialize(self):
#         with open(self.export_file + '.json', 'w') as file:
#             json.dump(self.build(), file)

# class SalesReportCSV(SalesReport):
#     # Sua implementação vai aqui
#     pass

# Fim V3 ----------------------------------------------------------------

# V4 - Composição --------------------------------------------------------
from abc import ABC, abstractmethod
import gzip
import json
from zipfile import ZipFile


class ZipCompressor():
    ''' Nossos compressores terão fixado o local de salvamento
    do arquivo, então vamos defini-lo nos construtores'''
    def __init__(self, filepath='./'):
        self.filepath = filepath

    def compress(self, file_name):
        with ZipFile(file_name + '.zip', 'w') as zip_file:
            zip_file.write(file_name)


class GzCompressor():
    def __init__(self, filepath='./'):
        self.filepath = filepath

    def compress(self, file_name):
        with open(file_name, 'rb') as content:
            with gzip.open(file_name + '.gz', 'wb') as gzip_file:
                gzip_file.writelines(content)


class SalesReport(ABC):
    # Nossa classe agora espera *instâncias* de compressor como um parâmetro.
    # Temos um valor padrão para suportar o código que usava as SalesReport
    # sem parâmetros -- não precisa correr pra re-escrever nada ;)
    def __init__(self, export_file, compressor=GzCompressor()):
        self.export_file = export_file
        self.compressor = compressor

    def build(self):
        return [{
                'Coluna 1': 'Dado 1',
                'Coluna 2': 'Dado 2',
                'Coluna 3': 'Dado 3'
                },
                {
                'Coluna 1': 'Dado A',
                'Coluna 2': 'Dado B',
                'Coluna 3': 'Dado C'
                }]

    # Aqui temos um atributo de classe!
    FILE_EXTENSION = ''

    def get_export_file_name(self):
        # Aqui usamos o atributo de classe
        # Vai fazer mais sentido nas classes herdeiras!
        return self.export_file + self.FILE_EXTENSION

    def compress(self):
        self.serialize()
        self.compressor.compress(self.get_export_file_name())

    @abstractmethod
    def serialize(self):
        raise NotImplementedError


class SalesReportJSON(SalesReport):
    # Nós não reimplementamos o get_export_file_name
    # mas como ele usa um atributo de classe pra pegar a extensão
    # só de redefinir o atributo já vamos conseguir mudar o resultado!
    FILE_EXTENSION = '.json'

    def serialize(self):
        with open(self.get_export_file_name(), 'w') as file:
            json.dump(self.build(), file)


class SalesReportCSV(SalesReport):
    # Sua implementação vai aqui
    pass


# Para testar
relatorio_de_compras = SalesReportJSON('meu_relatorio_1')
relatorio_de_vendas = SalesReportJSON('meu_relatorio_2', ZipCompressor())

relatorio_de_compras.compress()
relatorio_de_vendas.compress()
