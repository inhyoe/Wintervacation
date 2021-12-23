package Java.unit6.Lab;

class Animal {
    public void sound() {
        System.out.println("소리를 낸다.");
    }
}

class Dog extends Animal {
    public void sound() {
        System.out.println("멍멍"); // 메소드 오버라이드
    }
}

class Cat extends Animal {
    public void sound() {
        System.out.println("야옹"); // 메소드 오버라이드
    }
}

public class 동적_메소드_호출 {
    public static void main(String[] args) {
        Animal an = new Animal(); // 참조 변수는 an
        Dog dog = new Dog(); // 참조 변수는 dog
        Cat cat = new Cat(); // 참조 변수는 cat

        an.sound();
        dog.sound();
        cat.sound();

        Animal obj; // obj라는 참조변수를 생성한 후

        obj = an; // 각 타입의 객체를 대입.
        an.sound();

        obj = dog;
        obj.sound();

        obj = cat;
        obj.sound();

    }
}
