package Natureza;

public class Gato extends Felidae{
     String nome;

     public Gato(String reino, String filo, String classe, String familia,
     String genero, String especie, String ordem,
               int idade, String nome) {
          super(reino, filo, classe, familia, genero, especie,ordem, idade);
          this.nome = nome;
     }

     String getGato() {
          return nome;
     }

}