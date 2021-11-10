////////////////////////////
/// @power_by pãodequeijo///
////////////////////////////

public class M3_EX1 {
     class A {
          /// Agradecia tambem que me revisa-se a classe A, caso tenha algum erro, ou algo
          /// que não
          //// seja pedido no exercício
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

     /// Class B{ *inicio aqui?*
     public static void main(String[] args) {
          /// class B { *ou inicio aqui?*

          System.out.println(A.full_nome("Lucas", "Costa"));
          System.out.println("Data de Nascimento: " + A.data_nasci(29, 04, 1994));
          System.out.println("Local de Nascimento: " + A.local_nasci);
          System.out.println("Numero desejado de filhos: " + A.filhos_fut);

     }
     //// A minha duvida é se tenho de declarar a class B dentro do main, ou se tenho
     //// de declarar a
     /// class B fora da main e inclui-la dentro..//
}
