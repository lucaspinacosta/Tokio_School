package Packages.ABC;

public class C_1 extends A_1{
    private String visa;
    protected int visa_num;
    public String est_soci;

    public C_1(String nome, String morada, int idade, int num_agreg, String visa, int visa_num, String est_soci) {
        super(nome, morada, idade, num_agreg);
        this.visa = visa;
        this.est_soci = est_soci;
        this.visa_num = visa_num;
    }

    String getVisa() {
        return visa;
    }

    protected int getVisa_num() {
        return visa_num;
    }

    public String getEst_soci() {
        return est_soci;
    }

}
