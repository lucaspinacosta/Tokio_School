package Data_infor;

public class App{
    public static void mostrar_data(C_1 nome_info,String nomes, String last_name,String morada,int idade, int num_agreg) {
        System.out.println("\nNomes:\s"+ C_1.nome_info(nomes, last_name, morada, idade, num_agreg)); 
        System.out.println("\nMorada:\s"+C_1.nome_info(nomes, last_name, morada, idade, num_agreg));       
    }
    public static void mostrar_data(A_1 nome_info, String nomes, String last_name, String morada, int idade, int num_agreg) {
        System.out.println("\nNome:\s"+A_1.nome_info(nomes, last_name, morada, idade, num_agreg));
    }
    public static void mostrar_data(B_1 nome_info, String nomes, String last_name,String morada, int idade, int num_agreg){
        System.out.println("\nNome:\s"+B_1.nome_info(nomes, last_name, morada, idade, num_agreg));
    }
    
    public static void main(String[] args) {

        App.mostrar_data(new C_1(),"Dona","Irene", "Brasil", 50, 2);
        App.mostrar_data(new A_1() {}, "Huji", "Maga","Portugal",23,0);
        App.mostrar_data(new B_1() {}, "Julia", "Maga","Norway",29,0);
        
    }
}