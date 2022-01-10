package StandStock;

public class App{

     public static void main(String[] args) {
          Carro alfa= new Carro("Renault", "clio", 32_000, 123000, 4);
          System.out.print("\nMarca:\s"+alfa.marca+"\n");

          Carro beta= new Carro("Seat", "Ibiza", 3_000, 250_000, 3);
          System.out.print(beta);
     }
}