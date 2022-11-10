public class Caneta {
    // Caracteristicas da caneta que criamos, no caso, os atributos:
    String modelo; // string - texto
    String cor;
    double ponta; // numero com ponto
    int carga; // numero inteiro
    final int CARGA_MAXIMA = 100; // acabando a carga - não escreve mais
    boolean tampa; // verdadeiro ou falso - com tampa não escreve

    // Comportamento da caneta - métodos:
    void escrever(String texto) {
        for (int i = 0; i < texto.length(); i++) { // chaves para abrir funções
            if (tampa == false) { // "=" atribui "==" compara - sem tampa ele escre
                if (carga > 0) {
                    System.out.print(texto.charAt(i));//tirar o ln para não pular para linha de baixo
                    carga -= 1;
                } else {
                    System.out.println("\n CANETA SEM CARGA");
                    break; // aqui para o for
                }
            } else {
                System.out.println("CANETA TAMPADA bobu :P");
            }
        }
    }

    public Caneta (String modelo, String cor, double ponta, boolean tampa) {
        this.modelo = modelo;
        this.cor = cor;
        this.ponta = ponta;
        this.carga = CARGA_MAXIMA;
        this.tampa = tampa;
    }
}
