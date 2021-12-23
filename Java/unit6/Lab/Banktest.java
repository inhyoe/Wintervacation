package Java.unit6.Lab;;
class Bank{
    double rate;
    double setInterestRate(double rate){
        return rate;
    }
    void setRate(double rate){
        this.rate = rate;
    }
    void print(){
        System.out.println(rate);
    }
}
class BadBank extends Bank{
    
}

class NormalBank extends Bank{
    
}

class GoodBank extends Bank{

}
public class Banktest {
    public static void main(String[] args) {
        BadBank bad = new BadBank();
        NormalBank normal = new NormalBank();
        GoodBank Good = new GoodBank();
        bad.setRate(10.0);
        normal.setRate(5.0);
        Good.setRate(1.0);
        bad.print();
        normal.print();
        Good.print();
    }
}
