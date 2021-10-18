/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Pao de Queijo(Lucas Costa)
 */
import javax.swing.JOptionPane;
public class M2_EX1 {

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        // TODO code application logic here
        
        
        int n1, n2, n3, n4, n5, n6, total;  /** */
        
        String msn1, msn2, msn3, msn4, msn5, msn6;
        
        msn1 = JOptionPane.showInputDialog("Entre o 1� numero");
        msn2 = JOptionPane.showInputDialog("Entre o 2� numero");
        msn3 = JOptionPane.showInputDialog("Entre o 3� numero");
        msn4 = JOptionPane.showInputDialog("Entre o 4� numero");
        msn5 = JOptionPane.showInputDialog("Entre o 5� numero");
        msn6 = JOptionPane.showInputDialog("Entre o 6� numero");
        
        
        n1 = Integer.parseInt(msn1);
        n2 = Integer.parseInt(msn2);
        n3 = Integer.parseInt(msn3);
        n4 = Integer.parseInt(msn4);
        n5 = Integer.parseInt(msn5);
        n6 = Integer.parseInt(msn6);
        
        
        total = (n1 + n2 + n3 + n4 + n5 + n6) /6;
        JOptionPane.showMessageDialog(null, "media: "+ total, "Media dos 6 numeros", JOptionPane.PLAIN_MESSAGE);
        System.out.println("Media dos 6 numeros = " + total);
        System.exit(0);
                
    }
}
