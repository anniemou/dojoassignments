using System;

namespace Wizard_Ninja_Samural
{
    public class Human
    {
        public string Name { get; set; }

        //The { get; set; } format creates accessor methods for the field specified
        //This is done to allow flexibility
        public int Health { get; set; }
        public int Strength { get; set; }
        public int Intelligence { get; set; }
        public int Dexterity { get; set; }

        public Human(string person)
        {
            Name = person;
            Strength = 3;
            Intelligence = 3;
            Dexterity = 3;
            Health = 100;
        }
        public Human(string person, int str, int intel, int dex, int hp)
        {
            Name = person;
            Strength = str;
            Intelligence = intel;
            Dexterity = dex;
            Health = hp;
        }
        public void attack(object obj)
        {
            Human enemy = obj as Human;
            if (enemy == null)
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