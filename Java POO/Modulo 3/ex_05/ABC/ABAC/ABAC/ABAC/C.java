package ABAC;

public class C{
    public int somar;
    double dividir;
    protected float diminuir;

    public void calcular(C c, float x) {

            System.out.println("C calculo:"+c.somar((int) x));
            System.out.println("C diminuir:"+c.diminuir(x));
            System.out.println("C dividir:"+c.dividir(x));
        }
    public int somar (int x){
        return (x*24);
    }


    public float diminuir(float x) {
        return (float) (x*8765.81277);
    }


    public double dividir(float x) {
        return (x*7);
    }

    public String toString(){
        return "\n"+"C diminuir:"+diminuir + "\n" +"C somar:"+ somar +"\n"+"C dividir:"+dividir;
    }
    

}