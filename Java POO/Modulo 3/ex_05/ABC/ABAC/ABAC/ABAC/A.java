package ABAC;

public class A{
    int somar;
    double dividir;
    protected float diminuir;


    public void calcular(A a, double x, double y) {
        System.out.println("A calculo:"+a.somar((int)x, (int)y));
        System.out.println("A diminuir:"+a.diminuir(x, y));
        System.out.println("A dividir:"+a.dividir(x, y));
    }

    public int somar(int x, int y) {
        return x+y;
    }

    protected float diminuir(double x, double y) {
        return (float) (x-y);
    }
    
    public double dividir(double x, double y) {
        return (x/y);
    }


    public String toString(){
        return "\n"+"A diminuir:"+diminuir + "\n" +"A somar:"+ somar +"\n"+"A dividir:"+dividir;
    }
}


    
