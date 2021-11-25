import javax.swing.JOptionPane;

public class M3_EX5 {
}

class A_1 {
     private String nome;
     protected int idade;
     public String morada;
     public int num_agreg;

     public A_1(String nome, String morada, int idade, int num_agreg) {
          this.nome = nome;
          this.morada = morada;
          this.idade = idade;
          this.num_agreg = num_agreg;
     }

     String getNome() {
          return nome;
     }

     public String getMorada() {
          return morada;
     }

     protected int getIdade() {
          return idade;
     }

     public int getNum_agreg() {
          return num_agreg;
     }

}

class B_1 {
     protected String nome, morada;
     private int idade;
     public int num_agreg;

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

     int getIdade() {
          return idade;
     }

     public int getNum_agreg() {
          return num_agreg;
     }
}

class C_1 extends A_1 {
     private String visa;
     protected int visa_num;
     public String estado_civ;

     public C_1(String nome, String morada, int idade, int num_agreg, String visa, int visa_num, String estado_civ) {

          super(nome, morada, idade, num_agreg);
     }

     public String getVisa() {
          return visa;
     }

     protected int getVisa_num() {
          return visa_num;
     }

     protected void setVisa_num() {
          this.visa_num = visa_num;
     }

     public String getEstado_civ() {
          return estado_civ;
     }

}

class Principal {
     public static void main(String[] args) {

          A_1 pessoa1;
          pessoa1 = new A_1("Irene", "Guimaraes", 54, 1);

          B_1 pessoa2;
          pessoa2 = new B_1("Lucas", "Guimarães", 27, 0);

          C_1 pessoa3;
          pessoa3 = new C_1("Josh", "England", 46, 1, "Trabalhador", 1651320, "Casado");

          JOptionPane.showMessageDialog(null,
                    pessoa1.getNome() + "\n" + pessoa1.morada + "\n" + pessoa1.idade + "\n" + pessoa1.getNum_agreg(),
                    "Dados class A", JOptionPane.INFORMATION_MESSAGE);

          JOptionPane.showMessageDialog(null,
                    pessoa2.nome + "\n" + pessoa2.morada + "\n" + pessoa2.getIdade() + "\n" + pessoa2.num_agreg,
                    "Dados class B", JOptionPane.INFORMATION_MESSAGE);

          JOptionPane.showMessageDialog(null,
                    pessoa3.getNome() + "\n" + pessoa3.morada + "\n" + pessoa3.idade + "\n" + pessoa3.getNum_agreg()
                              + "\n" + pessoa3.getVisa() + "\n" + pessoa3.getVisa_num() + "\n" + pessoa3.estado_civ,
                    "Dados class C", JOptionPane.INFORMATION_MESSAGE);

     }
}