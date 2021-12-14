package ABC;

public class B_1 {
    protected String nome, morada;
    private int idade;
    public int num_agreg;

    public B_1(String nome, String morada, int idade, int num_agreg) {
        this.nome = nome;
        this.morada = morada;
        this.idade = idade;
        this.num_agreg = num_agreg;
        }

     protected String getNome() {
        return nome;
     }

     protected String getMorada() {
        return morada;
     }

     protected void setMorada(String morada) {
        this.morada = morada;
     }

     int getIdade() {
        return idade;
     }

     public int getNum_agreg() {
        return num_agreg;
    }
    
}
