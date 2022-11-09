import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        System.out.println("Hello Word :)");
        System.out.println("Mi");
        Scanner scan = new Scanner(System.in);
        // primeiro eu chamo o scan - para poder colocar informações - uma caixa de
        // texto por exemplo
        System.out.println("Informe dois números: ");
        double n1, n2;
        // double é uma variavel de número não inteiro
        n1 = scan.nextDouble();
        n2 = scan.nextDouble();
        System.out.println("A soma dos dois números é: " + (n1 + n2));

    }

}