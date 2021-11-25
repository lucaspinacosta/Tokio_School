
public class M3_EX6 {
}

class Natureza {
     static String reino;
     static String filo;
     static String classe;
     static String familia;
     static String genero;
     static String especie;

     public Natureza(String reino, String filo, String classe, String familia, String genero, String especie) {
          Natureza.reino = reino;
          Natureza.filo = filo;
          Natureza.classe = classe;
          Natureza.familia = familia;
          Natureza.especie = especie;
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