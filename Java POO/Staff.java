
public class Staff {
     static String pessoas1(String name, int idade) {
          return (name + "\s" + idade);
     }

     static String pessoas2(String name, int idade) {
          return (name + "\s" + idade);
     }

     static String pessoas3(String name, int idade) {
          return (name + "\s" + idade);
     }

     static String boss2(String name, int idade) {
          return (name + "\s" + idade);
     }

     static String boss3(String name, int idade) {
          return (name + "\s" + idade);
     }

}

class All {
     private static String boss1(String name, int idade) {
          return (name + "\s" + idade);
     }

     static String pessoas1 = Staff.pessoas1("Irene", 32);
     static String pessoas2 = Staff.pessoas2("Geraldo", 30);
     static String pessoas3 = Staff.pessoas3("Lucas", 27);
     static String boss2 = Staff.boss2("Teresa", 38);
     static String boss3 = Staff.boss3("Pedro", 52);

     public static void main(String[] args) {
          System.out.println("Caixa: " + pessoas1);
          System.out.println("Armazem: " + pessoas2);
          System.out.println("Gestão: " + pessoas3);
          System.out.println("Entrega: " + boss2);
          System.out.println("Tesouraria: " + boss3);
          System.out.println("CEO: " + boss1("Julia", 46));

     }

}