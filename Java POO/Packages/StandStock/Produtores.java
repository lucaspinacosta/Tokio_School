package Packages.StandStock;
public class Produtores {
     public String marca;
     
     public Produtores(String marca){
          this.marca=marca;
     }

     String setMarca(){
          return marca;
     }
     String getMarca(){
          return marca;
     }

     public String toString(){
          return "\nMarca:\s"+marca;
     }

     
}
