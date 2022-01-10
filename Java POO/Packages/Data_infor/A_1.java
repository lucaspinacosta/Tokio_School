package Packages.Data_infor;


public class A_1 {

    protected String nomes, last_name, morada;
    public int idade, num_agreg;

    
    protected static String nome_info(String nomes, String last_name,String morada) {
        return nomes+"\s"+last_name+"\nMorada:\s"+morada+"!";
    }

    public static String dados_gerais(int idade, int num_agreg){
        return idade + "\s"+ num_agreg;
    }

    static String private_info(String nomes, String last_name) {
        return "\nNome:\s"+nomes+"\s"+last_name;   
    }
    

    
}