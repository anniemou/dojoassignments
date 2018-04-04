using System;

namespace Wizard_Ninja_Samural
{
    class Ninja : Human
    {
        // To Ninja klhrwnomei apo to Human. To "base" anaferete sthn class Human, h opoia exei constructor me to toulaxiston 1 parametro
        // opote kaloume thn "base" me thn parametro pou diabazoume sto Ninja, kai ononmazete "name"
        public Ninja(string name) : base(name)
        {
            this.Dexterity = 175;
        }

        public void Steal(object target)
        {
            Human enemy = target as Human;
            if (enemy == null)
            {
                Console.WriteLine("Failed Attack");
            }
            else
            {
                this.Health += 10;
            }
        }
    }
}