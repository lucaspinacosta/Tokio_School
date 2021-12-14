package Contabilidade;

public class Pessoas extends App {
     static String nome;
     static String ult_nome;

     public Pessoas (String nome,String ult_nome){
          Pessoas.nome = nome;
          Pessoas.ult_nome = ult_nome;
     }

     public String setNome(){
          return nome;
     }
     public String getNome(){
          return nome;
     }
     public String setUlt_nome(){
          return ult_nome;
     }
     public String getUlt_nome(){
          return ult_nome;
     }
     
}
