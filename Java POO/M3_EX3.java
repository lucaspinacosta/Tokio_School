public class M3_EX3 {

}

class Carro {
     int preco, iva;
     String golf, polo, astra, seat;

     public void valor(String golf, int preco, int iva) {
          System.out.println("Carro:\s" + golf + "\nValor:" + preco + "\nIva:" + iva);
     }

     public void valor(int iva, int preco, String seat) {
          System.out.println("Carro:\s" + seat + "\nValor:" + preco + "\nIva:" + iva);
     }

     public void valor(int preco, String astra) {
          System.out.println("Carro:\s" + astra + "\nValor: " + preco);
     }

     public void valor(double iva, int preco, String polo) {
          System.out.println("Carro:\s" + polo + "\nValor:" + preco + "\nIva: " + iva);
     }

     public void valor(String polo, int valor) {
          System.out.println("Carro:\s" + polo + "\nValor:\s" + valor);
     }
}

class Exec {
     public static void main(String[] args) {
          Carro astra = new Carro();
          astra.valor(17_000, "Opel Astra");/// int, string//

          Carro seat = new Carro();
          seat.valor(2300, 12_000, "Seat Leon");/// int, int, String//

          Carro polo = new Carro();
          polo.valor(154.52, 10_000, "Volkswagen Polo");/// double, int, String//

     }
}