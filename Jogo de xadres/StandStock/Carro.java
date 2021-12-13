package StandStock;
import StandStock.Produtores;

public class Carro {
     public String marca, modelo;
     public double valor;
     private int kmh, num_portas;

     public Carro(String marca, String modelo, double valor, int kmh, int num_portas){

          this.marca=marca;
          this.modelo=modelo;
          this.valor=valor;
          this.kmh=kmh;
          this.num_portas=num_portas;
     }

     String setMarca(){
          return marca;
     }
     String getMarca(){
          return marca;
     }
     String setModelo(){
          return modelo;
     }
     String getModelo(){
          return modelo;
     }
     double setValor(){
          return valor;
     }
     double getValor(){
          return valor;
     }
     int setKmh(){
          return kmh;
     }
     int getKmh(){
          return kmh;
     }
     int setNum_portas(){
          return num_portas;
     }
     int getNum_portas(){
          return num_portas;
     }
     

     public static void main(String[] args) {
          Carro alfa= new Carro(marca, modelo, valor, kmh, num_portas)
          Produtores alfa1 = new Produtores
     }
}