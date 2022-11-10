import java.time.LocalDate;
import javax.swing.AbstractAction;
//classe no sistema 
public class Sistema {
    public void run(){
        //infos do cliente
        Cliente cliente = new Cliente("Midoria", "123456", "allmight_wannbe@gmail.com");
        //infos da conta do cliente
        Conta conta = new Conta(cliente, 1234);
        //aqui se faz o "print" do que se quer mostrar
        System.out.println(conta);

        Titulo steam = new Titulo( 200 , LocalDate.of(2022,03,30) , 5);
        conta.depositar(300);    
        
    }

    boolean pagarTitulo(Titulo titulo, Conta conta) {
        double valorPagar;
        LocalDate dataTitulo = titulo.getData();
        LocalDate hoje = LocalDate.now();
        if (dataTitulo.compareTo(hoje) > 0) {
            valorPagar = titulo.getValor();
        } else {
            //TO-DO - terminar imprementação
        }
        return true;
    }
}