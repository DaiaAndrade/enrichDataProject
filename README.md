# Enrich Data Project

**Projeto criado por: Daiane Focking Andrade**

Esse é um projeto de ETL implementado em Python 3.6 utilizando a [API de Geocoding gratuita MapQuest](https://developer.mapquest.com/).

Foram utilizados também as bibliotecas [Requests](http://docs.python-requests.org/en/master/), [JSON](https://docs.python.org/3/library/json.html) e [MySQLdb](https://mysqlclient.readthedocs.io/) para lidar, respectivamente com 
requisições URL, arquivos .json e banco de dados.

### Arquivos do Projeto:
    database.py: arquivo com a classe Database, classe reponsável por executar as atividades do banco
    extract.py: arquivo com a função para extrair as coordenadas do arquivo
    transform.py: arquivo com as funções responsável por enriquecer as informações sobre as coordenadas e tratar os dados para serem postos no banco
    run.py: arquivo runnable

### Execução
1. Pre-Requisitos:
    
        Python 3.6
        Ubuntu/Linux
        MySQL 14.14
        Terminal

2. Como executar:
    
        python3.6 run.py SERVIDOR USUARIO SENHA ARQUIVO KEY

### Entradas esperadas:
    SERVIDOR: Servidor a ser conectado
    USUARIO: Usuário do servidor
    SENHA: Senha do usuário
    ARQUIVO de coordenadas: Caminho do arquivo onde as coordenadas estão armazenadas
    KEY: Chave de acesso da API
** O nome do banco e da tabela foram previamente escolhidos

### Saída esperada:
Impressão dos dados do banco com as seguintes colunas:
    
        Latitude, Longitude , Rua, Cidade, Estado, Pais, CEP, Tipo_endereco, URL_Mapa, Interseccao, Unidade_Velocidade, Limite_Velocidade

### Comportamento:
O programa executará uma vez, perguntará se o usuário deseja ver o banco completo ou resumido, exibirá o desejado e terminará a operação

### Troubleshooting:
Por conta de falta de dados ou campos muito extenso, existem duas formas de visualização:
 - Completa: todos os dados.
 - Essencial: visualização que constam os dados de Latitude, Longitude , Rua, Cidade, Estado, Pais, CEP.
 
Os dados de `Interseccao, Unidade_Velocidade e Limite_Velocidade` estão apenas disponíveis para coordenadas no EUA.

`URL_Mapa` retorna uma url que mostra uma miniatura de mapa com a coordenada.

### Failsafes:
- Caso algum parâmetro esteja faltando ou ele esteja errado, o programa termina.
- Caso alguma dado de login no server esteja errado, o programa termina.
- Caso já exista um banco com o nome previamente escolhido, ele será utilizado
- Caso o arquivo com as coordenadas não exista, o programa termina apagando a tabela.
- Caso ocorra algum erro com a API, o programa termina apagando a tabela.
As interações com o usuário ficam no aguardo das respostas certas por tempo indeterminado

### Utilidade dos dados:
Dados geográficos enriquecidos podem ajudar, naturalmente, na localização de pessoas.
Não só isso, mas são úteis para marketing direcionado tanto para interesses próximos ao da localização quanto para `awareness` do cliente (em potencial ou não). Pode-se utilizar um raio `n` ao redor do ponto para que quando um potencial cliente estiver nesse raio receba uma mensagem, anúncio ou notificação sobre o estabelecimento/serviço. Isso se aplica para concorrentes também: quando o cliente está próximo ao estabelecimento do concorrente, ele recebe algum tipo de sinalização.
