using System;

namespace human {
//Create a base Human class with five attributes: name, strength, intelligence, dexterity, and health.
    public class Human
    {
        public string Name {get; set; }
        public int Strength { get; set; }  
        public int Intelligence { get; set; }
        public int Dexterity { get; set; }
        public int Health { get; set; }
   
 //Give a default value of 3 for strength, intelligence, and dexterity. Health should have a default of 100.
       
        public Human(string name) 
        {
            Name = name;
            Strength = 3;
            Intelligence = 3;
            Dexterity = 3;
            Health = 100;
        }
// Let's create an additional constructor that accepts 5 parameters, so we can set custom values for every field. 
//When an object is constructed from this class it should have the ability to pass a name   
        public Human(string name, int str, int intel, int dex, int hp)
        {
            Name = name;
            Strength = str;
            Intelligence = intel;
            Dexterity = dex;
            Health = hp;
        }
//Now add a new method called attack, which when invoked, should attack another Human object that is passed as a parameter. The damage done should be 5 * strength (5 points of damage to the attacked, for each 1 point of strength of the attacker).
         public void Attack(Human enemy)
        {
            if(enemy == null)
            {
                Console.WriteLine("Failed Attack");
            }
            else
            {
                enemy.Health -= this.Strength * 5;
            }
        }
    
    
    }
}