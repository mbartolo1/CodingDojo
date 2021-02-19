public class Bat extends Mammal{
    public Bat(){
        super(300);
    }
    public void fly(){
        System.out.println("babda o weee");
        energyLevel -= 50; 
    }
    public void eatHumans(){
        System.out.println("yummy");
        energyLevel += 25;
    }
    public void attackTown(){
        System.out.println("AAAAAA");
        energyLevel -= 100;
    }
}