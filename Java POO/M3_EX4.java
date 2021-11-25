
import java.util.Scanner;

public class M3_EX4 {
}

class PC {

     private String marca, modelo;
     private int ram, hdd;

     public String getModelo() {
          return modelo;
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

     public void setModelo(String modelo) {
          this.modelo = modelo;
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

}

class Insert_prod {

     public static void main(String[] args) {

          Scanner dados = new Scanner(System.in);

          boolean criar = true;
          PC perifericos = new PC();

          while (criar == true) {

               System.out.println("Insira a Marca:\s");
               perifericos.setMarca(dados.next());

               System.out.println("Insira GB do HDD:\s");
               perifericos.setHdd(dados.nextInt());

               System.out.println("Insira o Modelo:\s");
               perifericos.setModelo(dados.next());

               System.out.println("Insira GB da RAM:\s");
               perifericos.setRam(dados.nextInt());

               System.out.println("Marca: " + perifericos.getMarca() + "\nModelo:\s" + perifericos.getModelo()
                         + "\nHdd:\s" + perifericos.getHdd() + "\nMemoria Ram:\s" + perifericos.getRam() + "\n");

               System.out.println("Pretende criar mais algum PC?\n" + "S\\N");

               String info = dados.next();
               if (info.equals("S")) {
                    continue;
               } else {
                    dados.close();
                    break;
               }

          }
     }
}
