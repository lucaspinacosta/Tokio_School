package Packages.Contabilidade;

import java.util.Scanner;



public class App{
     public static void main(String[] args) {
          try (Scanner input_detail = new Scanner(System.in)) {
               System.out.println("1 - Destalhes da Conta\n2 - Definições de Utilizador");
               int imp_imp = input_detail.nextInt();
               
               

               if (imp_imp == 1){
                    
                    System.out.print(Detalhes_cont.users);
               }
               if (imp_imp==2){
                    System.out.print("1- Novo Utilizador \n2- Configuração de Utilizador \n3- Voltar\n");
                    
                    Scanner dados = new Scanner(System.in);
                    int imp_impp=input_detail.nextInt();
                    
                    if (imp_impp == 1){
                         Scanner other = new Scanner(System.in);
                         Detalhes_cont users= new Detalhes_cont(dados.next(), dados.next(), input_detail.nextInt(), other.nextDouble(), other.nextDouble(), other.nextDouble());
                         other.close();
                         System.out.println(users);
                         
                    
                         for (int i = 0; i < Detalhes_cont.users.length; i++){
                              System.out.print(Detalhes_cont.users);
                         }

                    }
                    if(imp_impp==2){
                         System.out.println("ln");
                    }
                    if(imp_impp==3){
                         System.out.print("obj");
                    }
                    dados.close();
                    
               }
          }
          
          

}
}