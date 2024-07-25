Car Rental Simulation System
Overview

This project is a simulation system for a car rental service. It includes functionality for viewing car details, services offered, and client testimonials. The system is built with Django and utilizes various templates for rendering pages, handling comments, and displaying dynamic content.
Features

    Home Page: Displays an introduction to the car rental service and highlights featured services.
    About Us Page: Provides information about the company and its history, along with a call-to-action for potential drivers.
    Services Page: Lists the different services offered by the rental company.
    Blog Section: Includes individual blog posts with comments and replies functionality.
    Comment System: Allows users to leave comments on blog posts and reply to existing comments.
    Car Listings: Displays a list of cars available for rental.

Installation

    Clone the Repository

    # bash

git clone https://github.com/yourusername/car-rental-simulation.git
cd car-rental-simulation

Create a Virtual Environment

# bash

python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

Install Dependencies

# bash

pip install -r requirements.txt

Apply Migrations

# bash

python manage.py migrate

Run the Development Server

# bash

    python manage.py runserver

    Access the Application

    Open your browser and go to http://127.0.0.1:8000/ to view the application.

Configuration

    Static Files: Ensure that all static files such as CSS, JavaScript, and images are correctly placed in the static directory.
    Database: The project uses Django’s default SQLite database. For production, consider configuring a different database such as PostgreSQL.

Code Structure

    views.py: Contains the views for handling requests and rendering templates.
        about(request): Fetches and displays car data on the "About Us" page.
        services(request): Renders the "Services" page.

    urls.py: Defines URL patterns and routes them to the appropriate views.

    Templates: HTML files for rendering various pages:
        base.html: Base template with common layout.
        about.html: Template for the "About Us" page.
        services.html: Template for the "Services" page.
        blog_single.html: Template for displaying individual blog posts and comments.

    Static Files: Includes CSS, JavaScript, and image files used for styling and functionality.

Contributing

Feel free to fork the repository and make pull requests. Ensure to follow coding standards and include tests for any new features.
License

This project is licensed under the MIT License. See the LICENSE file for details.
Sistema de Simulação de Locadora de Carros



# Em português



Visão Geral

Este projeto é um sistema de simulação para um serviço de locadora de carros. Inclui funcionalidades para visualizar detalhes dos carros, serviços oferecidos e depoimentos de clientes. O sistema é construído com Django e utiliza vários templates para renderizar páginas, lidar com comentários e exibir conteúdo dinâmico.
Funcionalidades

    Página Inicial: Exibe uma introdução ao serviço de locadora de carros e destaca os serviços em destaque.
    Página Sobre Nós: Fornece informações sobre a empresa e sua história, juntamente com uma chamada para ação para motoristas em potencial.
    Página de Serviços: Lista os diferentes serviços oferecidos pela locadora.
    Seção de Blog: Inclui postagens individuais do blog com funcionalidade de comentários e respostas.
    Sistema de Comentários: Permite aos usuários deixar comentários nas postagens do blog e responder a comentários existentes.
    Listagem de Carros: Exibe uma lista de carros disponíveis para locação.

Instalação

    Clone o Repositório

    # bash

git clone https://github.com/seuusuario/simulacao-locadora-carros.git
cd simulacao-locadora-carros

Crie um Ambiente Virtual

# bash

python -m venv env
source env/bin/activate  # No Windows use `env\Scripts\activate`

Instale as Dependências

# bash

 pip install -r requirements.txt

Aplique as Migrações

#bash

python manage.py migrate

Execute o Servidor de Desenvolvimento

# bash

    python manage.py runserver

    Acesse a Aplicação

    Abra seu navegador e vá para http://127.0.0.1:8000/ para visualizar a aplicação.

Configuração

    Arquivos Estáticos: Certifique-se de que todos os arquivos estáticos, como CSS, JavaScript e imagens, estão corretamente colocados no diretório static.
    Banco de Dados: O projeto utiliza o banco de dados SQLite padrão do Django. Para produção, considere configurar um banco de dados diferente, como PostgreSQL.

Estrutura do Código

    views.py: Contém as views para lidar com requisições e renderizar templates.
        about(request): Busca e exibe dados dos carros na página "Sobre Nós".
        services(request): Renderiza a página "Serviços".

    urls.py: Define os padrões de URL e os roteia para as views apropriadas.

    Templates: Arquivos HTML para renderizar várias páginas:
        base.html: Template base com layout comum.
        about.html: Template para a página "Sobre Nós".
        services.html: Template para a página "Serviços".
        blog_single.html: Template para exibir postagens individuais do blog e comentários.

    Arquivos Estáticos: Inclui arquivos CSS, JavaScript e imagens usados para estilização e funcionalidade.

Contribuindo

Sinta-se à vontade para fazer fork do repositório e enviar pull requests. Certifique-se de seguir os padrões de codificação e incluir testes para quaisquer novos recursos.
Licença

Este projeto é licenciado sob a Licença MIT. Veja o arquivo LICENSE para detalhes.
