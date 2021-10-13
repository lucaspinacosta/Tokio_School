import javax.swing.JOptionPane;


public class M2_EX5 {
     public static void main(String[] args) {
          String numero = JOptionPane.showInputDialog("Insira um numero:");
          
          int numero_conv = Integer.parseInt(numero);
          
          if (numero_conv >= 0){
               JOptionPane.showMessageDialog(null, "Numero Postivo");
          }else{
               JOptionPane.showMessageDialog(null, "Numero Negativo");
          }
          
     }
}
