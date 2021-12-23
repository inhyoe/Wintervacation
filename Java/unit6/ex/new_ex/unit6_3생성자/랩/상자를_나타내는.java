package Java.unit6.ex.new_ex.unit6_3생성자.랩;

class Box{
    private int width;
    private int length;
    private int height;
    private int volume; // 부피

    public int getvolume(){
       volume  = width * height * length;
       return volume;
    }

    public Box(int width,int length,int height){
        this.width =width;
        this.length =length;
        this.height = height;
    }
    
}


public class 상자를_나타내는 {
    public static void main(String[] args) {
        Box b = new Box(10,20,30);
        System.out.println("상자의 부피는 "+ b.getvolume());
        
    }
}
