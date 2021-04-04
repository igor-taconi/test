# Web Crawler Elo7

Um Crawler do site [Elo7](https://www.elo7.com.br/) para obter o nome, preço, detalhes, categoria, subcategoria e o link da página, de todos os produtos do site.

## Pré-requisitos
Para você rodar o projeto é necessário tem instalado em sua máquina o `Python3.6+`.

## Como rodar esse projeto
-   Clone esse repositório.
```
git clone https://github.com/taconi/web-crawling-elo7.git
```
-   Crie um virtualenv com Python 3.
```
cd web-crawling-elo7
python -m venv .venv
```
-   Ative o virtualenv.
```
source .venv/bin/activate
```
-   Instale as dependências.
```
pip install -r requirements.txt
```
-   Rode o prjeto.
```
scrapy crawl elo7
```

## Dados
Após o script terminar sua execução aparecerá um arquivo _products.db_.  
Você pode entrar no site [SQL Online IDE](https://sqliteonline.com/) para visualizar o arquivo ou baixar o [DB Browser for SQLite](https://sqlitebrowser.org/dl/) em sua máquina, ou usar da forma que quiser.

## Contribuindo
Sinta-se à vontade para enviar pull requests.
