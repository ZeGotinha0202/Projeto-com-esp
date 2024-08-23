import os

def corrigir_arquivos_txt(folder_path):
    txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

    for txt_file in txt_files:
        txt_path = os.path.join(folder_path, txt_file)

        # Ler o arquivo existente
        with open(txt_path, 'r') as f:
            lines = f.readlines()

        # Reescrever o arquivo corrigido
        with open(txt_path, 'w') as f:
            for line in lines:
                # Corrigir apenas as linhas que começam com "0 0 0" e têm um formato incorreto
                if line.startswith('0 0 0 0 '):
                    # Substituir "0 0 0 " por "0,"
                    new_line = line.replace('0 0 0 0 ', '0,', 1)
                    f.write(new_line)
                else:
                    f.write(line)

    print("Correção dos arquivos concluída.")

folder_path = r'C:\Users\Felipe Almeida\Desktop\Tentativa 3162\pythonProject\Labels'
corrigir_arquivos_txt(folder_path)
