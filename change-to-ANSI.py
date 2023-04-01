import os
import codecs
import chardet

def converte_arquivos(path):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            converte_arquivos(item_path)
        else:
            if item.endswith('.lua') or item.endswith('.xml'):
                with open(item_path, 'rb') as f:
                    conteudo = f.read()
                    encoding = chardet.detect(conteudo)['encoding']
                    if encoding is None:
                        encoding = 'utf-8'
                conteudo_str = conteudo.decode(encoding)
                conteudo_codificado = conteudo_str.encode('ANSI', errors='ignore')
                with open(item_path, 'wb') as f:
                    f.write(conteudo_codificado)

# exemplo de uso
converte_arquivos('/caminho/da/pasta')
