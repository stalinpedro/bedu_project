DROP DATABASE IF EXISTS Banco;
CREATE DATABASE Banco;

GRANT ALL PRIVILEGES ON Banco.* TO Banco@'%' IDENTIFIED BY 'Banco';

GRANT ALL PRIVILEGES ON Banco.* TO Banco@'localhost' IDENTIFIED BY 'Banco';




docker exec -i pythonsql mysql -hlocalhost -uBiblioteca -pBiblioteca Biblioteca < sql/tabla-libro.sql