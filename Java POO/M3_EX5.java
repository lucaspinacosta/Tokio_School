import javax.swing.JOptionPane;

public class M3_EX5 {
}

class A_1 {
     private String nome, morada;
     private int idade, num_agreg;

     public A_1(String nome, String morada, int idade, int num_agreg) {
          this.nome = nome;
          this.morada = morada;
          this.idade = idade;
          this.num_agreg = num_agreg;
     }

     String getNome() {
          return nome;
     }

     String getMorada() {
          return morada;
     }

     int getIdade() {
          return idade;
     }

     int getNum_agreg() {
          return num_agreg;
     }

}

class B_1 {
     protected String nome, morada;
     protected int idade, num_agreg;

     public B_1(String nome, String morada, int idade, int num_agreg) {
          this.nome = nome;
          this.morada = morada;
          this.idade = idade;
          this.num_agreg = num_agreg;
     }

     protected String getNome() {
          return nome;
     }

     protected String getMorada() {
          return morada;
     }

     protected int getIdade() {
          return idade;
     }

     protected int getNum_agreg() {
          return num_agreg;
     }
}

class C extends A_1 {

     public C(String nome, String morada, int idade, int num_agreg) {
          super(nome, morada, idade, num_agreg);
     }

     public String nome, morada;
     public int idade, num_agreg;
}

class Principal {
     public static void main(String[] args) {

          A_1 pessoa1;
          pessoa1 = new A_1("Irene", "Guimaraes", 54, 1);

          B_1 pessoa2;
          pessoa2 = new B_1("Lucas", "Guimarães", 27, 0);

          C pessoa3;
          pessoa3 = new C("Josh", "Lisboa", 32, 0);

          JOptionPane.showMessageDialog(null, pessoa1.getNome() + "\n" + pessoa1.getMorada() + "\n" + pessoa1.getIdade()
                    + "\n" + pessoa1.getNum_agreg(), "Dados class A", JOptionPane.INFORMATION_MESSAGE);

          JOptionPane.showMessageDialog(null,
                    pessoa2.nome + "\n" + pessoa2.morada + "\n" + pessoa2.idade + "\n" + pessoa2.num_agreg,
                    "Dados class B", JOptionPane.INFORMATION_MESSAGE);

          JOptionPane.showMessageDialog(null, pessoa3.getNome() + "\n" + pessoa3.getMorada() + "\n" + pessoa3.getIdade()
                    + "\n" + pessoa3.getNum_agreg(), "Dados class C", JOptionPane.INFORMATION_MESSAGE);

     }
}