import javax.print.attribute.standard.JobHoldUntil;
import javax.swing.JOptionPane;

public class M3_EX7 {
}

class Livro {
     private String autor;
     private String titulo;
     private int numero_pag;
     private String isbn;

     public String getAutor() {
          return autor;
     }

     public void setAutor(String autor) {
          this.autor = autor;
     }

     public String getTitulo() {
          return titulo;
     }

     public void setTitulo(String titulo) {
          this.titulo = titulo;
     }

     public String getIsbn() {
          return isbn;
     }

     public void setIsbn(String isbn) {
          this.isbn = isbn;
     }

     public int getNumero_pag() {
          return numero_pag;
     }

     public void setNumero_pag(int numero_pag) {
          this.numero_pag = numero_pag;
     }

     public String toString() {
          return "O Livro com título " + titulo + " e " + isbn + " e autor " + autor + " tem " + numero_pag + ".";

     }

}

class Bibliotecario {
     public static void main(String[] args) {

          Livro livro1 = new Livro();
          Livro livro2 = new Livro();

          livro1.setAutor("Collen McCullough");
          livro1.setIsbn("9789722907972");
          livro1.setNumero_pag(440);
          livro1.setTitulo("Um Passo a Frente");

          livro2.setAutor("James Rollins");
          livro2.setIsbn("9789722529754");
          livro2.setNumero_pag(504);
          livro2.setTitulo("O Mapa dos Osso");

          JOptionPane.showMessageDialog(null, livro1, "Dados", JOptionPane.INFORMATION_MESSAGE);
          JOptionPane.showMessageDialog(null, livro2, "Dados", JOptionPane.INFORMATION_MESSAGE);

          if (livro1.getNumero_pag() > livro2.getNumero_pag()) {
               JOptionPane.showMessageDialog(null,
                         "O livro " + livro1.getTitulo() + " com " + livro1.getNumero_pag() + ". Tem mais paginas que "
                                   + livro2.getTitulo() + ", que só contem " + livro2.getNumero_pag() + " páginas",
                         "Livros", JOptionPane.INFORMATION_MESSAGE);
          } else {
               JOptionPane.showMessageDialog(null,
                         "O livro " + livro2.getTitulo() + " com " + livro2.getNumero_pag() + ". Tem mais paginas que "
                                   + livro1.getTitulo() + ", que só contem " + livro1.getNumero_pag() + " páginas",
                         "Livros", JOptionPane.INFORMATION_MESSAGE);
          }
     }
}
