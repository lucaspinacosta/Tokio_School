package Natureza;


public class Natureza_ex {
     /**
      * Dentro da classe Natureza (classe mae), inserimos todos os gerais (que vao
      * ser comuns nas proximas classes derivadas)
      */
     String reino, filo, classe, familia, genero, especie;

     

     public Natureza_ex(String reino, String filo, String classe, String familia, String genero, String especie) {
          this.reino = reino;
          this.filo = filo;
          this.classe = classe;
          this.familia = familia;
          this.genero = genero;
          this.especie = especie;
     }

     String getReino() {
          return reino;
     }
     String setReino(String reino){
          return reino;
     }

     String getFilo() {
          return filo;
     }
     String setFilo(String filo){
          return filo;
     }

     String getClasse() {
          return classe;
     }
     String setClasse(String classe){
          return classe;
     }

     String getFamilia() {
          return familia;
     }
     String setFamilia(String familia){
          return familia;
     }

     String getGenero() {
          return genero;
     }
     String setGenero(String genero){
          return genero;
     }

     String getEspecie() {
          return especie;
     }
     String setEspecies(String especies){
          return especie;
     }


}