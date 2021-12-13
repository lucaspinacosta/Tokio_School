package Natureza;

public class Felidae extends App{

     /**
      * Felidae sendo uma classe que deriva de Animais, tambem ira derivar de
      * Natureza, obtendo assim os dados de Animais e Natureza
      */
     int idade;

     public Felidae(String reino, String filo, String classe, String familia, String genero, String especie,
               String ordem, int idade) {
          super();
          /**
           * No caso o super irá obter os dados ja definidos da classe Animais e Natureza
           */
          this.idade = idade;
     }

     int getIdade() {
          return idade;
     }

}
