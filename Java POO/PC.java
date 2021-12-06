import java.util.ArrayList;
import java.util.Scanner;

public class PC {

     private String marca, modelo;
     private int hdd, ram;

     public String getModelo() {
          return modelo;
     }

     public void setModelo(String modelo) {
          this.modelo = modelo;
     }

     public String getMarca() {
          return marca;
     }

     public int getRam() {
          return ram;
     }

     public int getHdd() {
          return hdd;
     }

     public void setMarca(String marca) {
          this.marca = marca;
     }

     public void setRam(int ram) {
          this.ram = ram;
     }

     public void setHdd(int hdd) {
          this.hdd = hdd;
     }

     public static void main(String[] args) {

          try (Scanner dados = new Scanner(System.in)) {
               ArrayList<PC> lista = new ArrayList<PC>();
               PC componentes = null;
               for (int i = 0; i < 99; i++) {
                    componentes = new PC();
                    System.out.println("Insira a Marca:\s");
                    componentes.setMarca(dados.next());
                    System.out.println("Insira o Modelo:\s");
                    componentes.setModelo(dados.next());
                    System.out.println("Insira GB do HDD:\s");
                    componentes.setHdd(dados.nextInt());
                    System.out.println("Insira GB da RAM:\s");
                    componentes.setRam(dados.nextInt());
                    lista.add(componentes);

                    System.out.println("Pretende criar mais algum PC?\n" + "(Sim\\Nao)");
                    String info = dados.next();
                    if (info.equals("Sim")) {
                         continue;
                    } else {
                         dados.close();
                         for (PC str : lista) {
                              // System.out.println("\n" + str);//
                              System.out.println(
                                        "\nMarca: " + str.getMarca() + "\nModelo:\s" + str.getModelo()
                                                  + "\nHdd:\s" + str.getHdd() + "\nMemoria Ram:\s"
                                                  + str.getRam() + "\n\n");

                         }

                         return;
                    }
               }
          }

     }
}
