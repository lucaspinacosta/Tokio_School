package Packages.Contabilidade;

public class Detalhes_cont extends Pessoas {

     static int num_conta;
     static double despesas, lucros, saldo;

     public Detalhes_cont(String nome,String ult_nome,int num_conta, double despesas, double lucros, double saldo){
          super(nome, ult_nome);
               Detalhes_cont.num_conta = num_conta;
               Detalhes_cont.despesas=despesas;
               Detalhes_cont.lucros=lucros;
               Detalhes_cont.saldo=saldo;
     }
     int getNum_conta(){
          return num_conta;
     }
     int setNum_conta(int num_conta){
          return num_conta;
     }
     double getDespesas(){
          return despesas;
     }
     double setDespesas(double despesas){
          return despesas;
     }
     double getLucro(){
          return lucros;
     }
     double setLucros(double lucros){
          return lucros;
     }

     static String [] users = {};
     public String toString(){
          return "Nome:\s"+Pessoas.nome+"\n"+"Ultimo Nome:\s"+Pessoas.ult_nome+"\n"+"Saldo:\s"+Detalhes_cont.saldo;
     }
}

