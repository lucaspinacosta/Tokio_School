

public class LIVRO {
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
          return "\nO Livro com título " + titulo + " e isbn " + isbn + " e autor " + autor + " tem " + numero_pag + " páginas.";

     }

     public static void main(String[] args) {

          LIVRO livro1 = new LIVRO();
          LIVRO livro2 = new LIVRO();

          livro1.setAutor("Collen McCullough");
          livro1.setIsbn("9789722907972");
          livro1.setNumero_pag(440);
          livro1.setTitulo("Um Passo a Frente");

          livro2.setAutor("James Rollins");
          livro2.setIsbn("9789722529754");
          livro2.setNumero_pag(504);
          livro2.setTitulo("O Mapa dos Osso");

          System.out.println("\nAutor:\s"+livro1.getAutor()+"\nTitulo:\s"+livro1.getTitulo()+"\nISBN:\s"+livro1.getIsbn()+"\nNº de Paginas:\s"+livro1.getNumero_pag());     
          System.out.println("\nAutor:\s"+livro2.getAutor()+"\nTitulo:\s"+livro2.getTitulo()+"\nISBN:\s"+livro2.getIsbn()+"\nNº de Paginas:\s"+livro2.getNumero_pag());
          
          System.out.println(livro1);
          System.out.println(livro2);
          
          if (livro1.getNumero_pag() > livro2.getNumero_pag()) {
               System.out.println(
                         "\nO livro " + livro1.getTitulo() + " com " + livro1.getNumero_pag() + ". Tem mais paginas que "
                                   + livro2.getTitulo() + ", que só contem " + livro2.getNumero_pag() + " páginas"
                         );
          } else {
               System.out.println(
                         "\nO livro " + livro2.getTitulo() + " com " + livro2.getNumero_pag() + ". Tem mais paginas que "
                                   + livro1.getTitulo() + ", que só contem " + livro1.getNumero_pag() + " páginas\n");
          }
     }
}
