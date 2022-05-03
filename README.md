# Projeto Python Recommendation 


**Elaborar uma API em Python para um exemplo de app de recomendações.**

Projeto desenvolvido com o FastAPI do Python

Rodando em ```http://localhost:8000```

![image](https://user-images.githubusercontent.com/8227278/166521260-babf1587-eb7c-4816-9cc2-30cc3549c35a.png)

Postam para os testes da API


## Configurações

Se preferir utilizar um banco de dados externo, como exemplo do MongoDB, basta definir o arquivo ```backend/src/.env``` e setar a variável `MONGO_DETAILS` contendo a string de definição do MongoDB, como exemplo: ```MONGO_DETAILS=mongodb+srv://userdb:senhadb@cluster.fwqwh.mongodb.net/recommendations?retryWrites=true&w=majority```

Porém ao rodar a aplicação via Docker, ela já vem pronta para ser usada com o back, front e um banco de dados MongoDB dockerizado.


## Rodando a aplicação

Bastar correr o comando na raíz do projeto ```docker-compose up --buil```

O back funciona no ```http://localhost:8000/recommendation```

O front funciona no ```http://localhost:3000```

## API Doc

``` http://localhost:8000/docs ```

## APIs requisições

### ```GET::http://localhost:8000/recommendation```
Response:
```
{
	"data": [
		[
			{
				"id": "627168b10dd98dbb3a5050c0",
				"name": "Ana",
				"knows": [
					"627175fb0dd98dbb3a5050c3"
				]
			},
			{
				"id": "627175fb0dd98dbb3a5050c3",
				"name": "Carlos",
				"knows": [
					"627168b10dd98dbb3a5050c0"
				]
			}
		]
	],
	"code": 200,
	"message": "Recommendations data retrieved successfully"
}
```
### ```GET::http://localhost:8000/recommendation/{id}```
Response: 
```
{
	"data": [
		{
			"id": "627175fb0dd98dbb3a5050c3",
			"name": "Carlos",
			"knows": [
				"627168b10dd98dbb3a5050c0"
			]
		}
	],
	"code": 200,
	"message": "Recommendation data retrieved successfully"
}
```
### ```POST::http://localhost:8000/recommendation```
Request:
```
{
  "name": "Carlos",
  "knows": ["627168b10dd98dbb3a5050c0"] //Id do friend
}
```
Response:
```
{
	"data": [
		{
			"id": "627175fb0dd98dbb3a5050c3",
			"name": "Carlos",
			"knows": [
				"627168b10dd98dbb3a5050c0"
			]
		}
	],
	"code": 200,
	"message": "Recommendation added successfully."
}
```
### ```PUT::http://localhost:8000/recommendation/{id}```
Request:
```
{
  "knows": [
    "627175c60dd98dbb3a5050c2"
  ]
}
```
Response:
```
{
	"data": [
		"Recommendation with ID: 627168b10dd98dbb3a5050c0 update is successful"
	],
	"code": 200,
	"message": "Recommendation updated successfully"
}
```
### ```DELETE::http://localhost:8000/recommendation/{id}```
Response:
```
{
	"data": [
		"Recommendation with ID: 627175c60dd98dbb3a5050c2 removed"
	],
	"code": 200,
	"message": "Recommendation deleted successfully"
}
```



