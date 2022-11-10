public class Cliente {
    // atributos da classe
    private String cpf;
    private String nome;
    private String email;

    //construtor
    public Cliente(String nome, String cpf, String email) {
        this.nome = nome;
        this.cpf = cpf;
        this.email = email;
    }

    // feito para visualizar as informações
    public void visualizarCliente() {
        System.out.println("Dados do Cliente:");
        System.out.println("Nome:" + nome);
        System.out.println("CPF:" + cpf);
        System.out.println("E-mail:" + email);
    }

    // retorna o nome
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }

    // retorna o cpf
    public String getCpf() {
        return cpf;
    }

    // retorna o email
    public String getEmail() {
        return email;
    }
    public void setEmail(String email) {
        this.email = email;
    }
}