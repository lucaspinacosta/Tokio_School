package Natureza;

public class Gato extends Felidae{
     String nome;

     public Gato(String reino, String filo, String classe, String familia,
     String genero, String especie, String ordem,
               int idade, String nome) {
          super(reino, filo, classe, familia, genero, especie,ordem, idade);
     }

     
     public String getNome() {
          return nome;
     }
     public void setNome(String nome){
          this.nome = nome;
     }

     public String toString(){
          return "Reino:\s"+reino+"\nFilo:\s"+filo+"\nClasse:\s"+classe+"\nFamilia:\s"+familia+"\nGenero:\s"+genero+"\nEspecie:\s"+especie+"\nOrdem:\s"+ordem+"\nNome:\s"+nome+"\nIdade:\s"+idade;
     }

}