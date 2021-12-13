package Natureza;

import javax.swing.JOptionPane;



public class App{
     public static void main(String[] args) {

          Gato gato1 = new Gato("Animalia", "Chordata", "Mammalia", "Felidae", "Felis", "F.Silvestris", "Carnivora", 5,
                    "Freddy");

          JOptionPane.showMessageDialog(null,
                    "Reino: " + gato1.reino + "\n" + "Filo: " + gato1.filo + "\n" + "Classe: " + gato1.classe + "\n"
                              + "Familia: " + gato1.familia + "\n" + "Genero: " + gato1.genero + "\n" + "Especie: "
                              + gato1.especie + "\n" + "Ordem: " + gato1.ordem + "\n" + "Idade: " + gato1.idade + "\n"
                              + "Nome: " + gato1.nome,
                    "Dados", JOptionPane.INFORMATION_MESSAGE);

          
     }
}
