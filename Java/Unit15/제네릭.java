package Java.Unit15;

class SimplePair<T>{
    private T data1;
    private T data2;

    public SimplePair(T data1, T data2){
        this.data1 = data1;
        this.data2 = data2;
    }
    T getFirst(){
        return data1;
    }

    T getSecond(){
        return data2;
    }

    void setFirst(T data1){
        this.data1 = data1;
        
    }
    void setSecond(T data2){
        this.data2 = data2;
    }
}


public class 제네릭 {
public static void main(String[] args) {
    SimplePair<String> pair = new SimplePair<String>("apple","tomato");
    System.out.println(pair.getFirst());
    System.out.println(pair.getSecond());
}

    
}
