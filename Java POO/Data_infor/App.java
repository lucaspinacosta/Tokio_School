package Data_infor;

/* Desenvolver 3 classes (A, B e C) definindo em cada uma delas, pelo menos, 3 tipos de variáveis com
3 modificadores de acesso diferentes.
Desde uma quarta classe principal, aceder a cada uma das variáveis das classes anteriores (A, B e
C) de maneira correta em função do modificador definido.
Pelo duas delas devem ser pai e filha.*/

public class App{
    public static void mostrar_data(C_1 nome_info,String nomes, String last_name,String morada,int idade, int num_agreg) {
        System.out.println("\nNomes:\s"+ C_1.nome_info(nomes, last_name, morada, idade, num_agreg));       
    }

    public static void mostrar_data(A_1 nome_info, String nomes, String last_name, String morada, int idade, int num_agreg) {
        System.out.println("\nNome:\s"+A_1.nome_info(nomes, last_name, morada));
    }

    public static void mostrar_data(B_1 nome_info, String nomes, String last_name,String morada, int idade, int num_agreg){
        System.out.println("\nNome:\s"+B_1.nome_info(nomes, last_name, morada, idade, num_agreg));
    }

    public static void dados_gerais(A_1 dados_gerais,int idade, int num_agreg){
        System.out.println("\nIdade:\s"+A_1.dados_gerais(idade, num_agreg));
    }

    private static void private_info(A_1 private_info, String nomes, String last_name) {
        System.out.println("\nNome:\s"+A_1.private_info(nomes, last_name));
        
    }

    
    public static void main(String[] args) {

        App.mostrar_data(new C_1() ,"Dona","Irene", "Brasil", 50, 2);
        App.mostrar_data(new A_1() {}, "Huji", "Maga","Portugal",23,0);
        App.mostrar_data(new B_1() {}, "Julia", "Maga","Norway",29,0);
        App.dados_gerais(new A_1() {}, 23, 2);
        
    }
}