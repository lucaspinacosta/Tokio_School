package ABAC;


public class B extends A {
    

    public int somar;
    private float dividir;
    protected double diminuir;

    public void calcular(B o, double x, double y) {   
        System.out.println("B calculo:"+ o.somar((int)x, (int)y));
        System.out.println("B diminuir:"+ o.diminuir(x, y));
        System.out.println("B dividir:"+o.dividir(x, y));
    }

    protected float somar (float x,float y){
        return (float) x*y;
    }
    public float diminuir (float x, float y){
        return x-y;
    }
    float dividir(float x, float y){
        return x/y;
    }

    public String toString(){
        return "\n"+"B diminuir:"+diminuir + "\n" +"B somar:"+ somar +"\n"+"B dividir:"+dividir;
    }

}