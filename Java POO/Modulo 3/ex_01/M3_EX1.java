////////////////////////////
/// @power_by pãodequeijo///
////////////////////////////
class A {

     static String data_nasci(int dia, int mes, int ano) {
          return (dia + "/" + mes + "/" + ano);
     }

     static String full_nome(String pr_nome, String ult_nome) {
          return (pr_nome + "\s" + ult_nome);
     }

     private static int num_filhos(int quant_filhos) {
          return (0);
     }

     private static int filhos_des = 1;

     static int filhos_fut = num_filhos(0) + filhos_des;
     static final String local_nasci = "Minas Gerais";

     protected String loca_atual = "Guimarães";
}

class B {

     public static void main(String[] args) {

          System.out.println(A.full_nome("Lucas", "Costa"));
          System.out.println("Data de Nascimento: " + A.data_nasci(29, 04, 1994));
          System.out.println("Local de Nascimento: " + A.local_nasci);
          System.out.println("Numero desejado de filhos: " + A.filhos_fut);

     }
}
