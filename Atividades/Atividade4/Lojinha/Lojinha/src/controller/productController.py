from models.product import Product
# from dao.product import product

class productController():
    
    def __init__(self) -> None:
        self.produtos = product.getInstance().getAll()
        self.carrinho = []

        self.produtos = [
            Product("Poke Ball", "200,00", "Para pokemons no geral"),
            Product("Great Ball", "600,00", "Para pokemons no geral, só que um pouco mais forte"),
            Product("Ultra Ball", "1200,00", "Para pokemons no geral, mas mais forte ainda"),
            Product("Master Ball", "100000,00", "Para pokemons no geral, sem falha de captura"),
            Product("Potion", "200,00", "Para recuperar 20HP"),
            Product("Super Potion", "5000,00", "Para recuperar 50%HP"),
            Product("Hyper Potion", "10000,00", "Para recuperar 80%HP"),
            Product("Max Potion", "15000,00", "Para recuperar 100%HP"),
            Product("Revive", "5000,00", "Para reviver pokemons"),
            Product("Max Revive", "1000,00", "Para reviver pokemons com 100%HP")
        ]
        
    # def getAl():
    #     return product.getInstance().getAll()
    
    def getCarrinho(self):
        return self.carrinho  
        
    def addCarrinho(self, index):
        index = int(index)
        try:
            self.carrinho.append(self.produtos[index])
        except:
            a = Product("produto não existe ou esgotou",price="0,00")
            self.carrinho.append(a)

        print("tamanho carrinho")
        print(len(self.carrinho))
    
    
    def somaCarrinho(self):
        total = 0
        for item in self.carrinho:
            preco = item.getPreco()
            preco = float(preco)
            total += preco
        return total
    
    def listarCarrinho(self):
        texto = ""
        for produto in self.carrinho:
            print("Produto atual")
            print(produto)
            print("\n")
            p = str(produto)
            texto = texto + "\n \n \n " + p
        soma = self.somaCarrinho()
        soma = str(soma)
        texto = texto + "\n \n \n  -------- \n R$ " + soma
        print("resultado final :::::: \n\n\n\n")
        print(texto)
        return texto