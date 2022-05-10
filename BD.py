
#Sugestões gerais

tabelas = "sugiro guardar aqui os nomes das suas tabelas, para lhe facilitar e aumentar a segurança, tendo em vista que esse arquivo estará no .gitignore, ou seja, so você tera acesso"

servidor = "será o servidor onde ta o banco"
usuario = "usuario utilizado para a sua Api acessar o banco"
senha = "senha de acesso ao banco"
banco = "nome do banco"

#Caso esteja trabalhando com mssql, tambem conhecido como sql server
import pyodbc

Driver = "aqui você vai colocar a versão do ODBC driver que esta sendo utilizado na sua maquina apra ela se conectar com o banco MSSQL"

mssql = pyodbc.connect('DRIVER={'+(Driver)+'};SERVER='+servidor+';DATABASE='+banco+';UID='+usuario+';PWD='+senha)

#Caso vá utilizar mysql
import mysql.connector

mssql = mysql.connector.connect( host=servidor, user=usuario, password=senha, database=banco)