import java.io.IOException;

import javax.swing.JOptionPane;

public class M2_EX2 {

    public static void main(String args[]) throws IOException {

        String senha = "12345";

        int tentativas = 0;
        int chances = 3;

        while (tentativas < chances) {
            chances--;
            String inpsenha = JOptionPane.showInputDialog("Digite a senha");
            if (inpsenha == senha) {
                JOptionPane.showMessageDialog(null, "Senha correta");
                break;
            } else {
                JOptionPane.showMessageDialog(null, "Senha Errada");
            }

        }
        JOptionPane.showMessageDialog(null, "Ficou sem tentativas");

    }

}
