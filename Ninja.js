
class Ninja{
    constructor(name, health){
        this.name = name;
        this.health = health;
        this.speed = 3;
        this.strength = 3;
    }
    sayName(){
    console.log(this.name);
}
    showStats(){
    console.log(this.name);
    console.log(this.strength);
    console.log(this.health);
    console.log(this.speed);
}
    drinkSake(){
    console.log(this.health += 10);
}
}
class Sensei extends Ninja{
    constructor(name){
        super(name);
        this.health = 200;
        this.speed = 10;
        this.wisdom = 10;
    }
    speakWisdom(){
    this.drinkSake();
    console.log("whatever");
}
}
const ninja1 = new Ninja("Hyabusa", 10);
ninja1.sayName();
ninja1.showStats();
ninja1.drinkSake();

const Sensei1 = new Sensei("Master Splinter");
Sensei1.speakWisdom();
// -> "What one programmer can do in one month, two programmers can do in two months."
Sensei1.showStats();
