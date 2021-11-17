import javax.swing.JOptionPane;

public class M3_EX6 {
}

class Natureza {
     /**
      * Dentro da classe Natureza (classe mae), inserimos todos os gerais (que vao
      * ser comuns nas proximas classes derivadas)
      */
     String reino, filo, classe, familia, genero, especie;

     public Natureza(String reino, String filo, String classe, String familia, String genero, String especie) {
          this.reino = reino;
          this.filo = filo;
          this.classe = classe;
          this.familia = familia;
          this.genero = genero;
          this.especie = especie;
     }

     String getReino() {
          return reino;
     }

     String getFilo() {
          return filo;
     }

     String getClasse() {
          return classe;
     }

     String getFamilia() {
          return familia;
     }

     String getGenero() {
          return genero;
     }

     String getEspecie() {
          return especie;
     }
}

class Animais extends Natureza {
     /**
      * Dentro da classe Animais, que é uma classe derivada de Natureza, vamos
      * incluir novas informações que seram obtidas somente pelos animais
      */
     String ordem;

     public Animais(String reino, String filo, String classe, String familia, String genero, String especie,
               String ordem) {
          super(reino, filo, classe, familia, genero, especie);
          /**
           * usamos o super para obter os dados ja definidos na classe Mãe, evitanto assim
           * termos de reescrever todas as linhas de codigo novamente
           */
          this.ordem = ordem;
     }

     String getReino() {
          return ordem;
     }

}

class Felidae extends Animais {

     /**
      * Felidae sendo uma classe que deriva de Animais, tambem ira derivar de
      * Natureza, obtendo assim os dados de Animais e Natureza
      */
     int idade;

     public Felidae(String reino, String filo, String classe, String familia, String genero, String especie,
               String ordem, int idade) {
          super(reino, filo, classe, familia, genero, especie, ordem);
          /**
           * No caso o super irá obter os dados ja definidos da classe Animais e Natureza
           */
          this.idade = idade;
     }

     int getIdade() {
          return idade;
     }

}

class Gato extends Felidae {
     String nome;

     public Gato(String reino, String filo, String classe, String familia, String genero, String especie, String ordem,
               int idade, String nome) {
          super(reino, filo, classe, familia, genero, especie, ordem, idade);
          this.nome = nome;
     }

     String getGato() {
          return nome;
     }

}

/**
 * class Leao extends Felidae { String detalhes;
 * 
 * public Leao(String reino, String filo, String classe, String familia, String
 * genero, String especie, String ordem, int idade, String detalhes) {
 * super(reino, filo, classe, familia, genero, especie, ordem, idade);
 * this.detalhes = detalhes; }
 * 
 * String getDetalhes() { return detalhes; } }
 */

class INFOR {
     public static void main(String[] args) {

          Gato gato1 = new Gato("Animalia", "Chordata", "Mammalia", "Felidae", "Felis", "F.Silvestris", "Carnivora", 5,
                    "Freddy");

          JOptionPane.showMessageDialog(null,
                    "Reino: " + gato1.reino + "\n" + "Filo: " + gato1.filo + "\n" + "Classe: " + gato1.classe + "\n"
                              + "Familia: " + gato1.familia + "\n" + "Genero: " + gato1.genero + "\n" + "Especie: "
                              + gato1.especie + "\n" + "Ordem: " + gato1.ordem + "\n" + "Idade: " + gato1.idade + "\n"
                              + "Nome: " + gato1.nome,
                    "Dados", JOptionPane.INFORMATION_MESSAGE);

          /**
           * Leao leao1 = new Leao("Animalia", "Chordata", "Mammalia", "Felidae",
           * "Panthera", "P.Leo", "Carnivora", 15, "O leão[3] [feminino: leoa]");
           * System.out.println( leao1.reino + "\n" + leao1.filo + "\n" + leao1.classe +
           * "\n" + leao1.familia + "\n" + leao1.genero + "\n" + leao1.especie + "\n" +
           * leao1.ordem + "\n" + leao1.idade + "\n" + leao1.detalhes);
           */
     }
}
