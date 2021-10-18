////////////////////////////
/// @power_by paodequeijo///
////////////////////////////

import javax.swing.JOptionPane;

public class M2_EX7 {
     public static void main(String[] args) {

          String nota_aluno = JOptionPane.showInputDialog("Insira a nota do aluno (0/10)");
          int nota_de_ava = Integer.parseInt(nota_aluno);

          if (nota_de_ava <= 2) {
               JOptionPane.showMessageDialog(null, "Insuficiente", "Nota do Aluno", JOptionPane.INFORMATION_MESSAGE);
          }
          if (nota_de_ava >= 3 && nota_de_ava <= 5) {
               JOptionPane.showMessageDialog(null, "Suficiente", "Nota do Aluno", JOptionPane.INFORMATION_MESSAGE);
          }
          if (nota_de_ava >= 6 && nota_de_ava <= 7) {
               JOptionPane.showMessageDialog(null, "Bom", "Nota do Aluno", JOptionPane.INFORMATION_MESSAGE);
          }
          if (nota_de_ava >= 8 && nota_de_ava <= 9) {
               JOptionPane.showMessageDialog(null, "Notalvel", "Nota do Aluno", JOptionPane.INFORMATION_MESSAGE);
          }
          if (nota_de_ava == 10) {
               JOptionPane.showMessageDialog(null, "Muito Bom", "Nota Do Aluno", JOptionPane.INFORMATION_MESSAGE);
          }
     }
}
