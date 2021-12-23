package Java.unit6.ex;

class Animal2{
    public void sound(){
        System.out.println("Bark");
    }
}

class Dog extends Animal2{
    public void sound(){
        super.sound();
        System.out.println("Bark Bark");
    }
}
public class Overriding {
    public static void main(String[] args) {
        Dog d = new Dog();
        
        d.sound();
    }
}
