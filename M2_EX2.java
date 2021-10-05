
import java.security.Principal;
import java.util.Scanner;




/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Pao de Queijo(Lucas Costa)
 */
public class M2_EX2 {

    public static void main(String args[]) {
        Scanner in = new Scanner (System.in);


        String senhaOriginal  = "123456-ABCdef";
        
        int tentativas = 3;
        int chances = 0;

        System.out.println("senha> ");
        String senha = in.nextLine();

        
        while (tentativas > chances);
        if (senha.equals(senhaOriginal))
        {
            System.out.println("Senha Correta");
            return;
            
        }else{
            System.out.println("Senha Incorreta");
            tentativas--;
            
        }


        }
}



