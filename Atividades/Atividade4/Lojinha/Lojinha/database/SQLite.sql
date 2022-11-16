CREATE TABLE usuario (
	idUsuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(45),
    email VARCHAR(45),
    senha VARCHAR(45)
);

CREATE TABLE produto(
	idProduto INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(45),
    preco DOUBLE,
    descricao VARCHAR(45)
);

CREATE TABLE carrinho(
	idCarrinho INTEGER  PRIMARY KEY AUTOINCREMENT,
    fkUsuario INT,
    fkProduto INT,
    FOREIGN KEY(fkUsuario) REFERENCES usuario(idUsuario),
    FOREIGN KEY(fkProduto) REFERENCES produto(idProduto)
);

INSERT INTO usuario(nome, email, senha) VALUES('Yuzo', 'yuzo@email.com', '123');
INSERT INTO	 produto(nome, preco, descricao) VALUES('Pokebola', 10.0, 'Pokebola inicial');
INSERT INTO carrinho(fkUsuario, fkproduto) VALUES(1, 1);

SELECT * FROM usuario;
SELECT * FROM produto;
SELECT * FROM carrinho;
SELECT c.idcarrinho, u.nome 'Comprador', p.nome 'Produto' 
	FROM carrinho c 
	JOIN usuario u ON c.fkusuario = u.idusuario 
	JOIN produto p ON c.fkproduto = p.idproduto;

