
public class M3_EX3 {

     class Staff {

     }

     class Enfermeiros extends Staff {
          private String nome;
          private int nif;
          private int idade;
          private String func;

          public Enfermeiros(String nome, int nif, int idade, String func) {
               this.nome = nome;
               this.nif = nif;
               this.func = func;
               this.idade = idade;
          }

          public String getNome() {
               return nome;
          }

          public int getNif() {
               return nif;
          }

          public int getIdade() {
               return idade;
          }

          public String getFunc() {
               return func;
          }

          public void setNome(String nome) {
               this.nome = nome;
          }

          public void setNif(int nif) {
               this.nif = nif;
          }

          public void setIdade(int idade) {
               this.idade = idade;
          }

          public void setFunc(String func) {
               this.func = func;
          }

     }

     Enfermeiros enf1 = new Enfermeiros("Irene", 545623148, 54, "Limpeza");
     Enfermeiros enf2 = new Enfermeiros("Josh", 463189755, 18, "Anestesia");

     public static void main(String[] args) {

     }

}
