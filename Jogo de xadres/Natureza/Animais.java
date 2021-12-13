package Natureza;

public class Animais extends App {
     /**
      * Dentro da classe Animais, que é uma classe derivada de Natureza, vamos
      * incluir novas informações que seram obtidas somente pelos animais
      */
     String ordem;

     public Animais(String reino, String filo, String classe, String familia, String genero, String especie,
               String ordem) {
          super();
          /**
           * usamos o super para obter os dados ja definidos na classe Mãe, evitanto assim
           * termos de reescrever todas as linhas de codigo novamente
           */
          this.ordem = ordem;
     }

     String getReino() {
          return ordem;
     }

}
