# Projeto Python Recommendation 


**Elaborar uma API em Python para um exemplo de app de recomendações.**

Projeto desenvolvido com o FastAPI do Python

Rodando em ```http://localhost:8000```

## Configurações

Se preferir utilizar um banco de dados externo, como exemplo do MongoDB, basta definir o arquivo ```backend/src/.env``` e setar a variável `MONGO_DETAILS` contendo a string de definição do MongoDB, como exemplo: ```MONGO_DETAILS=mongodb+srv://userdb:senhadb@cluster.fwqwh.mongodb.net/recommendations?retryWrites=true&w=majority```

Porém ao rodar a aplicação via Docker, ela já vem pronta para ser usada com o back, front e um banco de dados MongoDB dockerizado.


## Rodando a aplicação

Bastar correr o comando na raíz do projeto ```docker-compose up -d --build```

O back funciona no ```http://localhost:8000/recommendation```

O front funciona no ```http://localhost:3000```

## API Doc

``` http://localhost:8000/docs ```

![image](https://user-images.githubusercontent.com/8227278/166521260-babf1587-eb7c-4816-9cc2-30cc3549c35a.png)

## APIs requisições

### ```GET::http://localhost:8000/recommendation```
Ex. Response:
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
Ex. Response: 
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
Ex. Request:
```
{
  "name": "Carlos",
  "knows": ["627168b10dd98dbb3a5050c0"] //Id do friend
}
```
Ex. Response:
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
Ex. Request:
```
{
  "knows": [
    "627175c60dd98dbb3a5050c2"
  ]
}
```
Ex. Response:
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
Ex. Response:
```
{
	"data": [
		"Recommendation with ID: 627175c60dd98dbb3a5050c2 removed"
	],
	"code": 200,
	"message": "Recommendation deleted successfully"
}
```
### ```GET::http://localhost:8000/recommendation/{id}/kl1```
Ex. Response:
```
{
	"data": [
		[
			{
				"id": "627175fb0dd98dbb3a5050c3",
				"name": "Carlos",
				"knows": [
					"627168b10dd98dbb3a5050c0"
				]
			},
			{
				"id": "6271798e0dd98dbb3a5050c4",
				"name": "João",
				"knows": [
					"627168b10dd98dbb3a5050c0"
				]
			},
			{
				"id": "627179930dd98dbb3a5050c5",
				"name": "Maria",
				"knows": [
					"627168b10dd98dbb3a5050c0"
				]
			},
			{
				"id": "6271799d0dd98dbb3a5050c6",
				"name": "Vinícius",
				"knows": [
					"627168b10dd98dbb3a5050c0"
				]
			}
		]
	],
	"code": 200,
	"message": "Knows data retrieved successfully"
}
```
### ```GET::http://localhost:8000/recommendation/{id}/kl2```
Ex. Response:
```
{
	"data": [
		[
			{
				"id": "6271897dcfeb88d5996a489f",
				"name": "Napoleão",
				"knows": [
					"627175fb0dd98dbb3a5050c3"
				]
			},
			{
				"id": "627182a6cfeb88d5996a489e",
				"name": "Sebastião",
				"knows": [
					"6271799d0dd98dbb3a5050c6"
				]
			}
		]
	],
	"code": 200,
	"message": "Knows data retrieved successfully"
}
```



