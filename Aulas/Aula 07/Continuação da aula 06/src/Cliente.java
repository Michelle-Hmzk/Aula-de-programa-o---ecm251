public class Cliente {
    private String cpf; //private por ser algo que não queremos mostrar
    private String nome;
    private String email;

    //conta do cliente 
    public Cliente(String nome, String cpf, String email){
        this.nome = nome;
        this.cpf = cpf;
        this.email = email;
    }

    //dados do cliente que irão aparecer na tela
    public void visualizarCliente(){
        System.out.println("Dados do cliente:");
        System.out.println("Nome:" +nome);
        System.out.println("CPF:" +cpf);
        System.out.println("email:" +email);
    }
    public String getNome(){
        return nome;
    }
    
    public void setNome(String nome){
        this.nome=nome;
    }

    public String getCpf(){
        return cpf;
    }
    public String getEmail(){
        return email;
    }
    
    public void setEmail(String email){
        this.email = email;
    }
   
}
