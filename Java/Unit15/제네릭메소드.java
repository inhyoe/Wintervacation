package Java.Unit15;

class MyArrayAlg{
    public static <T> T getLast(T[] a){
        return a[a.length - 1];
    }
}

public class 제네릭메소드 {
    public static void main(String[] args) {
        String[] language = {"C++","C#","JAVA"};
        String last = MyArrayAlg.getLast(language);
        System.out.println(last);
    }
    
}
