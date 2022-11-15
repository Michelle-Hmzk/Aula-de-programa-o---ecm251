public class TestDrive {

    public static void executar(){
        System.out.println("Dado Generico: ");
        Dado d1 = new Dado("1234");

        //d4
        System.out.println("Dado Criado: "+ d1);
        System.out.println("Face Atual: "+ d1.faceAtual());
        // Sorteia uma nova face
        d1.rodar();
        System.out.println("Face Atual: "+ d1.faceAtual());
        System.out.println("\n");

        //d6
        System.out.println("Dado D6: ");
        Dado d2 = new DadoD6("5637");
        System.out.println("Dado Criado: "+ d2);
        System.out.println("Face Atual: "+ d2.faceAtual());
        // Sorteia uma nova face
        d2.rodar();
        System.out.println("Face Atual: "+ d2.faceAtual());
        System.out.println("\n");
     
        //d10
        System.out.println("Dado10: ");
        Dado d3 = new DadoD10("5555");
        System.out.println("Dado Criado: "+ d3);
        System.out.println("Face Atual: "+ d3.faceAtual());
        // Sorteia uma nova face
        d3.rodar();
        System.out.println("Face Atual: "+ d3.faceAtual());
        System.out.println("\n");

        //d20
        System.out.println("Dado20: ");
        Dado d4 = new DadoD20("888");
        System.out.println("Dado Criado: "+ d4);
        System.out.println("Face Atual: "+ d4.faceAtual());
        // Sorteia uma nova face
        d4.rodar();
        System.out.println("Face Atual: "+ d4.faceAtual());
    }

    
}