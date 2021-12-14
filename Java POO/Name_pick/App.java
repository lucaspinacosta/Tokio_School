package Name_pick;

public class App{
    public static void mostrarCalculo(OperacaoMats operacao , double x, double y){

        System.out.println("\nResultado:\s"+operacao.calcular(x, y));
    }
    public static void main(String[] args) {

        App.mostrarCalculo(new Soma(), 10, 10);
        App.mostrarCalculo(new Divis(), 5, 2);
        App.mostrarCalculo(new Resto(), 5, 2);

        
    }
}