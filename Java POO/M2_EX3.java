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
          private String titular;
          private int numero_conta;
          private double quantidade;

          public Conta(String titular,int numero_conta,  double quantidade){
               this.titular = titular;
               this.numero_conta = numero_conta;
               this.quantidade = quantidade;

               }
          public String getTitular() {  return titular; }
          public int getNumero_conta() { return numero_conta; }
          public double getQuantidade() { return quantidade; }

          public void setTitular(String titular) {this.titular = titular;}
          public void setNumero_conta(int numero_conta) { this.numero_conta = numero_conta;}
          public void setQuantidade(double quantidade) { this.quantidade = quantidade;}
     


     public static void main(String[] args) {

          
          Conta minhaConta1;
          minhaConta1 = new Conta("Irene", 347854, 32784.23);
          
          Conta minhaConta2;
          minhaConta2 = new Conta("Pão de Queijo", 982457, 100000.99);
               
          
          if (minhaConta1.quantidade < minhaConta2.quantidade){
               System.out.printf("Titular:\s"+minhaConta2.titular+'\n'+"ID:\s"+minhaConta2.numero_conta +'\n'+ "Quantidade:\s"+minhaConta2.quantidade+"€");
               
          }else{
               System.out.printf("Titular:\s"+minhaConta1.titular+'\n'+"ID:\s"+minhaConta1.numero_conta+'\n'+"Quantidade:\s"+minhaConta1.quantidade+"€");
          }

          
     

     }
}



