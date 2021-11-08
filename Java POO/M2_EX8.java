////////////////////////////
/// @power_by paodequeijo///
////////////////////////////

import javax.swing.JOptionPane;

public class M2_EX8 {
     public static void main(String[] args) {
          int primo = Integer.parseInt(JOptionPane.showInputDialog(null, "insira um numero"));
          boolean isPrimo = true;
          int divisor;
          for (int i = 2; i <= primo; i++) {
               if (((primo % i) == 0) && (i != primo)) {
                    isPrimo = false;
                    divisor = i;
                    break;
               }
          }
          if (isPrimo) {
               JOptionPane.showMessageDialog(null, "O numero\s" + primo + "\s e Primo", "Primo",
                         JOptionPane.INFORMATION_MESSAGE);
          } else {
               JOptionPane.showMessageDialog(null, "O numero \s" + primo + " nao e Primo", "Nao Primo",
                         JOptionPane.INFORMATION_MESSAGE);
          }
     }
}
