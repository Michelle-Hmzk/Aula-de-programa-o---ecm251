public class Conta {
    // Atributos:
    int numero;
    String titular;
    double saldo;
    String cpf;

    // Métodos da classe:
    // visualizar o saldo que tem na conta:
    void visualizarSaldo() {
        System.out.println("Saldo atual da conta: " + numero + " R$" + this.saldo);
    }

    // depositar algum valor na conta, somar:
    boolean depositar(double valor) {
        // if(valor>0){
        // saldo = saldo + valor;
        // return true;

        // }
        // else{
        // return false;

        // }
        if (valor < 0)
            return false;
        this.saldo += valor;
        return true;
    }

    // sacar algum valor da conta, subtrair:
    boolean sacar(double valor) {
        // if(valor<=saldo){
        // saldo = saldo - valor;
        // }
        if (valor > saldo)
            return false;
        if (valor < 0)
            return false;
        this.saldo -= valor;
        return true;
    }

    // transferencia de money, subtrair:
    boolean transferirDinheiro(double valor, Conta destino) {
        if (!this.sacar(valor))
            return false;

        if (!destino.depositar(valor))
            return false;

        return true;
    }
}