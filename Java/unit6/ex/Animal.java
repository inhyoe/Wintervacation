
package Java.unit6.ex;

class Action{
    public void eat(){
        System.out.println("eat() 호출됨. " );
    }
    public void sleep(){
        System.out.println("sleep() 호출됨.");
    }

}

class Lion extends Action{
    private int leg = 4;

    void roar(){
        System.out.println("roar() 호출됨.");
    }
    void whatleg(){
        System.out.println("다리는 : "+ leg);
    }
}

class Eagle extends Action{
    private int wings = 2;

    void fly(){
        System.out.println("fly() 호출");
    }
    void whatwing(){
        System.out.println("다리는 : "+ wings);
    }
}


public class Animal {
   public static void main(String[] args) {

       Lion L = new Lion();
       L.roar();
       L.sleep();
       Eagle E = new Eagle();
       E.fly();
       E.sleep();
   } 
}
