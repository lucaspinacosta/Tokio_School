package StandStock;

public class App{

     public static void main(String[] args) {
          Carro alfa= new Carro("Renault", "clio", 32_000, 123000, 4);
          Produtores alfa1 = new Produtores ("Lambo");
          System.out.print(alfa +"\n"+alfa1);
     }
}