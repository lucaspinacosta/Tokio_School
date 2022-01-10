package Packages.ABC;

import javax.swing.JOptionPane;

public class App{
    public static void main(String[] args) {
        A_1 pessoa1;
        pessoa1 = new A_1("Irene", "Guimaraes", 54, 1);

        B_1 pessoa2;
        pessoa2 = new B_1("Lucas", "Guimarães", 27, 0);

        C_1 pessoa3 = new C_1("Josh", "Inglaterra", 32, 1, "Trabalhador", 234234765, "Casado");

        JOptionPane.showMessageDialog(null,
                  pessoa1.getNome() + "\n" + pessoa1.morada + "\n" + pessoa1.idade + "\n" + pessoa1.getNum_agreg(),
                  "Dados class A", JOptionPane.INFORMATION_MESSAGE);

        JOptionPane.showMessageDialog(null,
                  pessoa2.nome + "\n" + pessoa2.morada + "\n" + pessoa2.getIdade() + "\n" + pessoa2.num_agreg,
                  "Dados class B", JOptionPane.INFORMATION_MESSAGE);

        JOptionPane.showMessageDialog(null,
                  pessoa3.getNome() + "\n" + pessoa3.morada + "\n" + pessoa3.idade + "\n" + pessoa3.num_agreg + "\n"
                            + pessoa3.getEst_soci() + "\n" + pessoa3.getVisa_num() + "\n" + pessoa3.getVisa(),
                  "Dados class C", JOptionPane.INFORMATION_MESSAGE);

   }
    
}