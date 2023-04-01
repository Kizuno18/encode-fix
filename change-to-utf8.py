import os
import codecs
import chardet

def converte_arquivos(path):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            converte_arquivos(item_path)
        else:
            if item.endswith('.lua'):
                with open(item_path, 'rb') as f:
                    conteudo = f.read()
                    encoding = chardet.detect(conteudo)['encoding']
                    if encoding is None:
                        encoding = 'utf-8'
                with codecs.open(item_path, 'w', encoding=encoding) as f:
                    f.write(conteudo.decode(encoding))
                    
# exemplo de uso
converte_arquivos('/caminho/da/pasta')
