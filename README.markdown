# Instruções para Configuração e Execução do Script de Geração de Grafo

Este projeto contém um script Python (`generate_graph.py`) que baixa um grafo de ruas do bairro "Todos os Santos, Teresina, Piauí, Brazil" usando a biblioteca OSMnx, salva os dados em um arquivo JSON e gera uma imagem PNG do grafo. Este README fornece instruções para configurar um ambiente virtual (`venv`), instalar dependências e executar o script.

## Pré-requisitos

- **Python 3.8 ou superior** instalado. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).
- Um terminal (Prompt de Comando no Windows, Terminal no Linux/macOS).
- Conexão com a internet para baixar as dependências.

## Configuração do Ambiente Virtual

Um ambiente virtual (`venv`) isola as dependências do projeto, evitando conflitos com outros projetos. Siga os passos abaixo para criar e configurar o ambiente.

### 1. Criar o Ambiente Virtual

No diretório do projeto, abra um terminal e execute:

```bash
python -m venv venv
```

Isso criará uma pasta chamada `venv` no diretório do projeto, contendo o ambiente virtual.

### 2. Ativar o Ambiente Virtual

Ative o ambiente virtual antes de instalar dependências ou executar o script. Os comandos variam por sistema operacional:

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```

- **Linux/macOS**:
  ```bash
  source venv/bin/activate
  ```

Após ativar, você verá `(venv)` no início da linha de comando, indicando que o ambiente virtual está ativo.

### 3. Instalar Dependências

Com o ambiente virtual ativado, instale as bibliotecas necessárias listadas no projeto:

```bash
pip install osmnx matplotlib
```

Observações:
- As bibliotecas `json`, `re` e `os` são parte da biblioteca padrão do Python e não precisam ser instaladas.
- A biblioteca `osmnx` pode exigir dependências adicionais (como `geopandas`). O comando acima instalará tudo automaticamente.

### 4. Desativar o Ambiente Virtual

Quando terminar de usar o ambiente virtual, desative-o com:

```bash
deactivate
```

Isso funciona em todos os sistemas operacionais (Windows, Linux, macOS).

## Executando o Script

1. Certifique-se de que o ambiente virtual está ativado (veja o passo 2).
2. Execute o script `generate_graph.py` com:

   ```bash
   python generate_graph.py
   ```

3. **Saídas do script**:
   - Um arquivo JSON contendo os dados do grafo será salvo em `cache/Todos_os_Santos_Teresina_Piauí_Brazil/Todos_os_Santos_Teresina_Piauí_Brazil.json`.
   - Uma imagem PNG do grafo será salva em `cache/Todos_os_Santos_Teresina_Piauí_Brazil/Todos_os_Santos_Teresina_Piauí_Brazil.png`.

## Estrutura de Arquivos Gerados

Após executar o script, a seguinte estrutura será criada:

```
cache/
└── Todos_os_Santos_Teresina_Piauí_Brazil/
    ├── Todos_os_Santos_Teresina_Piauí_Brazil.json
    └── Todos_os_Santos_Teresina_Piauí_Brazil.png
```

- **JSON**: Contém os nós (interseções) e arestas (ruas) do grafo.
- **PNG**: Uma visualização gráfica do grafo, onde as linhas azuis representam ruas e os pontos representam interseções.

## Solução de Problemas

- **Erro de permissão ao criar a pasta `cache`**: Verifique se você tem permissão para escrever no diretório do projeto. Tente executar o terminal como administrador (Windows) ou usar `sudo` (Linux/macOS), ou altere o `cache_dir` no script para uma pasta onde você tenha permissão (ex.: `~/Documentos/cache`).
- **Erro ao baixar o grafo**: Se o bairro "Todos os Santos" não for encontrado, verifique a conexão com a internet ou ajuste o `place_name` no script.
- **Bibliotecas não instaladas**: Certifique-se de que o ambiente virtual está ativado antes de executar `pip install`. Se houver erros, tente atualizar o `pip`:
  ```bash
  pip install --upgrade pip
  ```

## Personalização

- **Alterar o endereço**: Modifique a variável `place_name` no script para outro endereço (ex.: `"Outro Bairro, Cidade, Estado, País"`).
- **Alterar o diretório de saída**: Edite a variável `cache_dir` no script para outro caminho (ex.: `"outros_dados"` ou um caminho absoluto como `"C:/Users/SeuNome/cache"`).

Se precisar de ajuda adicional, consulte a documentação do [OSMnx](https://osmnx.readthedocs.io/) ou entre em contato.