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
        Scanner in = new Scanner(System.in);

        System.out.println("login> "); /** Escolha um user */
        String login = in.nextLine();

        System.out.println("senha> "); /** Escolhe a senha */
        String senha = in.nextLine();

        if (login.equals("paodequeijo")
                && senha.equals("12345-abcde")) { /** Aqui armazenamos as variaveis do login e senha */
            /** Verificamos se o login e a senha estao corretos */
            System.out.printf("%s sua senha esta correta.", login); /** Obtemos os resultados caso correctos */
        } else {
            System.out.println("Senha invalida!");
            return;
        }

    }

}
