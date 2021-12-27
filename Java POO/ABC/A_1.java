package ABC;

class A_1 extends App{
    private String nome;
    protected int idade;
    public String morada;
    public int num_agreg;

    public A_1(String nome, String morada, int idade, int num_agreg) {
          this.nome = nome;
          this.morada = morada;
          this.idade = idade;
          this.num_agreg = num_agreg;
    }

    private String getNome() {
         return nome;
    }

    public String getMorada() {
         return morada;
    }

    protected int getIdade() {
         return idade;
    }

    public int getNum_agreg() {
         return num_agreg;
    }

}
