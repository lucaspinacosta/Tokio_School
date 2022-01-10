package Natureza;

public class Animais extends Natureza_ex {
     /**
      * Dentro da classe Animais, que é uma classe derivada de Natureza, vamos
      * incluir novas informações que seram obtidas somente pelos animais
      */
     String ordem;

     public Animais(String reino, String filo, String classe, String familia, String genero, String especie,
               String ordem) {
          super(reino, filo, classe, familia, genero, especie);
          /**
           * usamos o super para obter os dados ja definidos na classe Mãe, evitanto assim
           * termos de reescrever todas as linhas de codigo novamente
           */
          this.ordem = ordem;
     }

     String getReino() {
          return ordem;
     }
     public String setOrdem(String ordem) {
         return this.ordem = ordem;
     }

     public String toString(){
          return "Reino:\s"+reino+"\nFilo:\s"+filo+"\nClasse:\s"+classe+"\nFamilia:\s"+familia+"\nGenero:\s"+genero+"\nEspecie:\s"+especie+"\nOrdem:\s"+ordem;
     }
}
