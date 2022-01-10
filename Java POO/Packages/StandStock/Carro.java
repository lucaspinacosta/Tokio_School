package StandStock;

public class Carro extends Produtores {
        public String modelo;
        public double valor;
        private int kmh, num_portas;
   
        public Carro(String marca,String modelo, double valor, int kmh, int num_portas){
            super (marca);
             this.modelo=modelo;
             this.valor=valor;
             this.kmh=kmh;
             this.num_portas=num_portas;
        }
   
        
        
        String setModelo(){
             return modelo;
        }
        String getModelo(){
             return modelo;
        }
        double setValor(){
             return valor;
        }
        double getValor(){
             return valor;
        }
        int setKmh(){
             return kmh;
        }
        int getKmh(){
             return kmh;
        }
        int setNum_portas(){
             return num_portas;
        }
        int getNum_portas(){
             return num_portas;
        }
        
    public String toString(){
         return "Marca:\s"+marca+"\nModelo:\s"+modelo+"\nValor:\s"+valor+"\nKm:\s"+kmh+"\nPortas:\s"+num_portas;
    }
}
