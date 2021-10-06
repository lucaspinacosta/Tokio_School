import java.io.IOException;
import java.lang.invoke.VarHandle;

import javax.swing.JOptionPane;
import javax.swing.JPasswordField;
import javax.swing.JTextPane;

public class M2_EX2 {

    public static void main(String args[]) throws IOException {

        
        String senha = "paodequeijo";
        
        int tentativas = 0;
        int chances = 3;

        while (tentativas < chances) {
            
            chances--;
            String ippsenha = JOptionPane.showInputDialog(null, "senha");
            
            if (ippsenha == senha) {
                JOptionPane.showMessageDialog(null, "Senha correta", ippsenha, JOptionPane.PLAIN_MESSAGE);
                return;
            } else {
                JOptionPane.showMessageDialog(null, "Senha Errada", "Senha inserida " + ippsenha, JOptionPane.PLAIN_MESSAGE);
            }

        }JOptionPane.showMessageDialog(null, "Ficou sem tentativas");
        return;
        
        
        

    }

}