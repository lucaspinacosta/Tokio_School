import javax.swing.JOptionPane;

public class Perifericos {
     private String marca;
     private int valor;

     public void Hd(String marca, int valor) {
          this.marca = marca;
          this.valor = valor;

     }

     static String Hdd(String marca, int valor) {
          return (marca + "\s" + valor);
     }

     static String Modelo(String marca, int valor) {
          return (marca + "\s" + valor);
     }
}

class Insert_prod {

     public static void main(String[] args) {
          Perifericos.Hdd(marca, valor)
          String mas1 = JOptionPane.showInputDialog(null, "Nome do Produto:");
     }

}
