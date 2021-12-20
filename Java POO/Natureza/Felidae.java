package Natureza;

public class Felidae extends Animais{

     /**
      * Felidae sendo uma classe que deriva de Animais, tambem ira derivar de
      * Natureza, obtendo assim os dados de Animais e Natureza
      */
     int idade;

     public Felidae(String reino, String filo, String classe, String familia, String genero, String especie,
               String ordem, int idade) {
          super(reino, filo, classe, familia, genero, especie,ordem);
          /**
           * No caso o super irá obter os dados ja definidos da classe Animais e Natureza
           */
          this.idade = idade;
     }

     int getIdade() {
          return idade;
     }
     int setIdade(int idade){
          return this.idade= idade;
     }

}
