/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Pao de Queijo(Lucas Costa)
 */



/**
 * M2_EX3
 */
public class M2_EX3 {

}
     class Conta{
                    String titular;
                    int numero_conta;
                    double quantidade;
               
     

     public static void main(String[] args) {
          


               Conta minhaConta1;
               minhaConta1 = new Conta();

               minhaConta1.titular = "Duke";
               minhaConta1.quantidade = 1500.50;
               minhaConta1.numero_conta = 54612;


               Conta minhaConta2;
               minhaConta2 = new Conta();

               minhaConta2.titular = "Irene";
               minhaConta2.numero_conta = 54156;
               minhaConta2.quantidade = 15464.54;

               if (minhaConta1.quantidade > minhaConta2.quantidade){
                    System.out.printf(
                         "Titular: " + minhaConta1.titular + '\n' +
                         "Quantidade: "+ minhaConta1.quantidade +"€" + '\n'+
                         "Numero de Conta: " + minhaConta1.numero_conta 
                    );
               } else {
                    System.out.println(
                         "Titular: " + minhaConta2.titular + '\n'+
                         "Quantia: " + minhaConta2.quantidade + "€" + '\n'+
                         "Numero de Conta: " + minhaConta2.numero_conta
                         );
               }

               

          
          

          
     

     }
}


