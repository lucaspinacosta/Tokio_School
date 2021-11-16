import javax.swing.JOptionPane;

public class M3_EX4 {
}

class PC {

     private String modelo, marca;
     private int ram, hdd;

     public PC(String modelo, String marca, int hdd, int ram) {
          this.modelo = modelo;
          this.marca = marca;
          this.hdd = hdd;
          this.ram = ram;
     }

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

          PC perifericos1;
          perifericos1 = new PC("Desktop", "Asus", 560, 16);

          PC perifericos2;
          perifericos2 = new PC("Laptop", "Gygabyte", 1, 32);

          String modelo_inp = JOptionPane.showInputDialog("PC: " + "\n" + "(perifericos1/perifericos2)");

          if (modelo_inp.equals("perifericos1")) {
               JOptionPane.showMessageDialog(null,
                         "O seu modelo: " + perifericos1.getModelo() + "\n" + perifericos1.getMarca() + "\n"
                                   + perifericos1.getHdd() + "GB" + "\n" + perifericos1.getRam() + "GB",
                         "Modelo", JOptionPane.INFORMATION_MESSAGE);
               return;

          }
          if (modelo_inp.equals("perifericos2")) {
               JOptionPane.showMessageDialog(null,
                         "Modelo: " + perifericos2.getModelo() + "\n" + "Marca: " + perifericos2.getMarca() + "\n"
                                   + "Memoria Ram: " + perifericos2.getRam() + "GB" + "\n" + "Tamanho HD: "
                                   + perifericos2.getHdd() + "TB",
                         "Informação", JOptionPane.INFORMATION_MESSAGE);

          } else {
               System.out.println("Erro!");
          }

     }

}
