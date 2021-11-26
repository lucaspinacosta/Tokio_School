
public class M3_EX6 {
}

class Natureza {
     String reino, filo, classe, familia, genero, especie;

     public Natureza(String reino, String filo, String classe, String familia, String genero, String especie) {
          this.reino = reino;
          this.filo = filo;
          this.classe = classe;
          this.familia = familia;
          this.especie = especie;
     }

     String getReino() {
          return reino;
     }

     String getFilo() {
          return filo;
     }

     String getClasse() {
          return classe;
     }

     String getFamilia() {
          return familia;
     }

     String getGenero() {
          return genero;
     }

     String getEspecie() {
          return especie;
     }

}

class Animais extends Natureza {

     String ordem;

     public Animais(String reino, String filo, String classe, String familia, String genero, String especie,
               String ordem) {
          super(reino, filo, classe, familia, genero, especie);
          this.ordem = ordem;
     }

     public String getOrdem() {
          return ordem;
     }
}

class Felidae extends Animais {
     int idade;

     public Felidae(String ordem, int idade) {
          super(ordem);
          this.idade = idade;
     }

     public int setIdade() {
          return idade;
     }

}

class show_data {

     public static void main(String[] args) {

     }
}