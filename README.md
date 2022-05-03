# Projeto Python Recommendation 


**Elaborar uma API em Python para um exemplo de app de recomendações.**

Projeto desenvolvido com o FastAPI do Python

Rodando em ```http://localhost:8000```

Postam para os testes da API


## Configurações

Se preferir utilizar um banco de dados externo, como exemplo do MongoDB, basta definir o arquivo ```backend/src/.env``` e setar a variável `MONGO_DETAILS` contendo a string de definição do MongoDB, como exemplo: ```MONGO_DETAILS=mongodb+srv://userdb:senhadb@cluster.fwqwh.mongodb.net/recommendations?retryWrites=true&w=majority```

Porém ao rodar a aplicação via Docker, ela já vem pronta para ser usada com o back, front e um banco de dados MongoDB dockerizado.


## Rodando a aplicação

Bastar correr o comando na raíz do projeto ```docker-compose up --buil```

O back funciona no ```http://localhost:8000/recommendation```

O front funciona no ```http://localhost:3000```

