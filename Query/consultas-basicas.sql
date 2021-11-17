/* Criar base de dados */
create database dbLojaSaulo



/* #################### Inicio Consullta Produtos  #################### */
-- Criar tabela
create table tb_Produtos(
	cdProduto INT PRIMARY KEY IDENTITY(1,1),
	nmProduto VARCHAR(50) not null, 
	vlProduto DECIMAL(6,2) not null,
)
-- Inserir dados de tabelas
INSERT INTO tb_Produtos VALUES ('Suco de Laranja', 4.5);
INSERT INTO tb_Produtos (vlProduto, nmProduto) VALUES (1.5, 'Suco de Manga');
INSERT INTO tb_Produtos (vlProduto, nmProduto) VALUES (1.5, 'Suco de Manga');
-- Selecionar dados de tabelas
select cdProduto, nmProduto, vlProduto from tb_Produtos
/* #################### Fim Consullta Produtos   #################### */



/* #################### Inicio Consullta Clientes  #################### */
create table tb_Clientes(
	cdCliente INT PRIMARY KEY IDENTITY(1,1),
	nmCliente VARCHAR(50) not null,
	dtNascimentoCliente DATE,
	inSexo VARCHAR(1) not null,
	nmEndereco VARCHAR(50),
	nmCidade VARCHAR(50),
	nmEstado VARCHAR(30),
	nmTelefone1 VARCHAR(15),
	nmTelefone2 VARCHAR(15),
)
-- Inserir dados de tabelas
INSERT INTO tb_Clientes VALUES ('Paulo Guina', '1980-05-01', 'M', 'Rua da Mecanicaa, 400', 'Campinas', 'Sao Paulo', '11 1234-5678', '11 912345678')
-- Selecionar dados de tabelas
select * from tb_Clientes
/* #################### Fim Consullta Clientes  #################### */




/* #################### Inicio Consullta Vendas  #################### */
create table tb_Vendas(
	cdVenda INT PRIMARY KEY IDENTITY(1,1),
	cdCliente INT not null FOREIGN KEY REFERENCES tb_Clientes (cdCliente),
	dtVenda DATETIME not null
);
-- Inserir dados de tabelas
insert into tb_Vendas values (6, 3.2) -- Testar Constraint
insert into tb_Vendas values (4, 3.2) -- Inserir Dados na Constraint
insert into tb_Vendas values (1, GETDATE()); -- Inserir Dados na Tabela
-- Selecionar dados de tabelas
select * from tb_Vendas
-- Remover a tabela 
drop table tb_Vendas
/* #################### Fim Consullta Vendas  #################### */




/* #################### Inicio Consullta Produtos Vendas  #################### */
create table tb_ProdutoVendas (
	cdProdutoVenda INT PRIMARY KEY IDENTITY(1,1),
	cdVenda INT FOREIGN KEY REFERENCES tb_Vendas (cdVenda) not null,
	cdProduto INT FOREIGN KEY REFERENCES tb_Produtos (cdProduto) not null,
	qtProduto int not null
)
-- Inserir dados de tabelas
insert into tb_ProdutoVendas values (1,1,3);
insert into tb_ProdutoVendas values (1,2,1);
insert into tb_ProdutoVendas values (1,4,4);
-- Selecionar dados de tabelas
select * from tb_ProdutoVendas


/* #################### Fim Consullta Produtos Vendas  #################### */



-- CONSTRAINT 
ALTER TABLE tb_Vendas
ADD CONSTRAINT FK_Produto_Vendas -- FOREIGN KEY
FOREIGN KEY (cdProduto)
REFERENCES tb_Produtos(cdProduto)


/* #################### Outras Consultas  #################### */
select * from tb_ProdutoVendas
select * from tb_Produtos


/* #################### INNER JOIN  #################### */
-- MODELO I
select * from tb_ProdutoVendas P Inner join tb_Produtos PV
on p.cdProduto = PV.cdProduto
-- MODELO II
select P.cdProduto, PV.qtProduto, vlProduto 
from tb_Produtos P Inner join tb_ProdutoVendas PV
on p.cdProduto = PV.cdProduto