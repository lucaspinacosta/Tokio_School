import java.io.IOException;

import javax.swing.JOptionPane;


public class M2_EX2 {

    public static void main(String args[]) throws IOException {

        String senha = "pãodequeijo";

        int tentativas = 0;
        int chances = 3;

        while (tentativas < chances) {

            chances--;
            String inpsenha = JOptionPane.showInputDialog("Digite a senha");
            if (inpsenha.equals(senha)) {
                JOptionPane.showMessageDialog(null, "Senha correta", inpsenha, JOptionPane.PLAIN_MESSAGE);
                return;
            } else {
                JOptionPane.showMessageDialog(null, "Senha Errada", "Senha inserida " + inpsenha,
                        JOptionPane.PLAIN_MESSAGE);
            }

        }
        JOptionPane.showMessageDialog(null, "Ficou sem tentativas");
        return;

    }

}