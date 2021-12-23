package Java.unit6.ex.new_ex.unit6_4생성자_오버로딩.예제;

class Student{
    private int number;
    private String name;
    private int age;

    Student(){
        number =100;
        name = "New Student";
        age = 18;
    }

    Student(int number,String name, int age){
        this.number = number;
        this.name = name;
        this.age = age;  // 매개 변수와 필드가 이름이 같다면 this를 사용하는 것이 좋다.
    }

    public String toString(){
        return "Student [number " + number + " name" + name +" age" + age + "]";
    }
    // tostring메소드를 사용하여 student() 생성자들이 출력된다.
}


public class Studenttest {
    public static void main(String[] args) {
        Student noover = new Student();
        Student over = new Student(101, "김종원", 24);
        System.out.println(noover);
        System.out.println(over);
    }
}

