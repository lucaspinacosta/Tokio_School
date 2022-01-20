package ABAC;


public class APP{
   
public static void main(String[] args) {

    A testA = new A();
    testA.calcular(testA,5,6);
    System.out.println(testA.somar(5,6)
    +"\n"+testA.diminuir(5,6)
    +"\n"+testA.dividir(5,6)+"\n"
    );

    B testB = new B();
    testB.calcular(testB, 9, 4);
    System.out.println(testB.somar(9,4)
    +"\n"+testB.diminuir(9,6)
    +"\n"+testB.dividir(9,6)+"\n"
    );

    C testC = new C();
    testC.calcular(testC,5);
    System.out.println(testC.somar(5)
    +"\n"+testC.diminuir(5)
    +"\n"+testC.dividir(5)+"\n"
    );

    C test1 = new C();
    test1.calcular(test1, 2);
    
    
}
}



